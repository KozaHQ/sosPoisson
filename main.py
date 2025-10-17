from telethon import TelegramClient, events

# Remplace par tes infos
api_id = 21486180
api_hash = 'fccefe99acb76669e86c4c09664b4ebb'
message_auto = """Hey there! 👋
This is an automatic reply — thanks for reaching out! I'll get back to you soon.

⚠️ Important:

This is my only official account.

I don't use WhatsApp or any other communication platforms.

I was recently raided, so from now on I'll be using Telegram only for communication and orders.

📦 How to check products:

You can see available items in my stories, or

Send me directly what you're looking for, and I'll let you know if I have it.

Thanks for your understanding and patience 🙏"""

# Création du client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # On ignore les messages des groupes, on répond seulement aux DM
    if event.is_private:
        sender = await event.get_sender()
        print(f"Message reçu de {sender.first_name}: {event.text}")
        await event.reply(message_auto)

print("🤖 Auto-répondeur actif... (Ctrl+C pour arrêter)")
client.start()
client.run_until_disconnected()
