from contextlib import contextmanager
import json
from sqlite3 import connect, Cursor
from typing import ContextManager

from schemas import Item


class Database:
    def __init__(self, path: str):
        self.con = connect(path)
        self.init_db()

    def close(self):
        self.con.commit()
        self.con.close()

    @contextmanager
    def cursor(self) -> ContextManager[Cursor]:
        cursor = self.con.cursor()
        yield cursor
        cursor.close()


    def init_db(self):
        with self.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER,
                    name TEXT,
                    active_quantity INTEGER,
                    images TEXT,
                    price INTEGER,
                    currency TEXT,
                    sale_price INTEGER,
                    item_link TEXT
                );
                """
            )

    def insert_item(self, item: Item):
        with self.cursor() as cur:
            cur.execute(
                """
                INSERT INTO items (id, name, active_quantity, images, price, currency, sale_price, item_link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.id,
                    item.name,
                    item.active_quantity,
                    json.dumps(item.images),
                    item.price,
                    item.currency,
                    item.sale_price,
                    item.item_link,
                )
            )

    def item_exists(self, item: Item) -> bool:
        with self.cursor() as cur:
            cur.execute("SELECT count(*) FROM items WHERE id = :id", {"id": item.id})
            count, = cur.fetchone()
            return count == 1

