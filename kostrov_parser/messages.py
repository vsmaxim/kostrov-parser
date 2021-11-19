import time
from typing import Iterable

import telegram
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from telegram import InputMediaPhoto
from tenacity import retry, wait_fixed

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)


@retry(wait=wait_fixed(60))
def send_message(text: str, link: str, imgs: Iterable[str]):
    if len(imgs) == 0:
        return

    post_text = f"{text}\n\n{link}"
    imgs_media = [
        InputMediaPhoto(media=url) for url in imgs if isinstance(url, str)
    ]
    imgs_media[0].caption = post_text
    bot.send_media_group(chat_id=TELEGRAM_CHAT_ID, media=imgs_media)
