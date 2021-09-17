# Kostrov Store parser

## About

Simple docker image to run parser on the [kostrov store](http://kostrovstore.com/) and publish fresh posts to telegram 
chat via bot API. Only men's wear is supported for now, sorry. 

## How to run

Execute the following to run with Docker:
```bash
docker run \
  -v $(pwd)/db:/app/db \
  -e "TELEGRAM_CHAT_ID=<YOUR CHAT ID>" \
  -e "TELEGRAM_BOT_TOKEN=<YOUR BOT TOKEN>" \
  -d --restart always ghcr.io/vsmaxim/kostrov-parser:latest
```

## Environment parameters

- `TELEGRAM_BOT_TOKEN` - Token from telegram bot API
- `TELEGRAM_CHAT_ID` - Target chat ID
 