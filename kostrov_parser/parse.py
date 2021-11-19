from typing import Iterable

import requests
from database import Database
from schemas import Item


def construct_image_link(id: int) -> str:
    return f"http://kostrovstore.com/_820_1220/{id}?crop=true"


def construct_item_link(id: int) -> str:
    return f"http://kostrovstore.com/products?FolderId=2&Id={id}"


def parse_degenerate_price(s: str) -> int:
    return int(s.split()[0]) if s else 0


def parse_items() -> Iterable[Item]:
    with requests.Session() as session:
        current_page = 1
        total_pages = 2
        items_per_page = 19

        while current_page < total_pages:
            response = session.post(
                "http://kostrovstore.com/productfolders/productsread",
                json={
                    "currency": "0",
                    "Id": 2,
                    "Tags": [5],
                    "Page": current_page
                },
            )
            data = response.json()

            total_pages = data["Pagging"]["TotalItems"] // items_per_page
            current_page += 1

            yield from (Item(
                id=i["Id"],
                name=i["Name"],
                active_quantity=i["ActiveQuontity"],
                images=[construct_image_link(it) for it in i["ImageIds"]],
                price=parse_degenerate_price(i["Price"]),
                currency=i["Currency"],
                sale_price=parse_degenerate_price(i["SalePrice"]),
                item_link=construct_item_link(i["Id"]),
            ) for i in data["Data"])


def parse_only_new_items(db: Database) -> Iterable[Item]:
    for item in parse_items():
        if db.item_exists(item):
            continue
        yield item
        db.insert_item(item)
