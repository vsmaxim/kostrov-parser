from typing import NamedTuple


class Item(NamedTuple):
    id: int
    name: str
    active_quantity: int
    images: list[int]
    price: int
    currency: str
    sale_price: int
    item_link: str
