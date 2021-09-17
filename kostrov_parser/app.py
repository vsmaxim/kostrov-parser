from database import Database
from messages import send_message
from parse import parse_only_new_items
from tenacity import retry, TryAgain, wait_fixed
from utils import first

BATCH_SIZE = 5
WAIT_TIME = 60


@retry(wait=wait_fixed(60))
def run():
    db = Database("db/db.sqlite")
    print("items started")
    for item in first(BATCH_SIZE, parse_only_new_items(db)):
        print(f"got {item.name} for ya")
        send_message(f"{item.name} {item.price}{item.currency}", item.item_link, item.images)
    print("items ended")
    db.close()
    raise TryAgain
