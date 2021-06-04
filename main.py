import secret

from telethon import TelegramClient, events, sync

client = TelegramClient("test_session", secret.api_id, secret.api_hash)

client.start()

client.send_file(secret.phone_number_to_be_send, "file-url")
