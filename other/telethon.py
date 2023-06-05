from telethon.sync import TelegramClient

with TelegramClient("name", api_id, api_hash) as client:
    channel = client.gey_input_entity(channel_id)
    client.senf_file(channel, "exports/screen_1234.pdf")
    client.run_until_disconnected()
