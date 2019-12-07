from pyrogram import Client

api_id = 1161446
api_hash = "58d126a0659f34cca2a0c08270d4b909"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
