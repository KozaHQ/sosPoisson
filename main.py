from telethon import TelegramClient, events
import json
import os

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

# Fichier pour stocker les conversations déjà répondues
responded_file = 'responded_users.json'

# Charger la liste des utilisateurs déjà répondues
def load_responded_users():
    if os.path.exists(responded_file):
        with open(responded_file, 'r') as f:
            return json.load(f)
    return []

# Sauvegarder la liste des utilisateurs déjà répondues
def save_responded_users(users):
    with open(responded_file, 'w') as f:
        json.dump(users, f)

# Création du client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # On ignore les messages des groupes, on répond seulement aux DM
    if event.is_private:
        sender = await event.get_sender()
        user_id = str(sender.id)
        
        # Charger la liste des utilisateurs déjà répondues
        responded_users = load_responded_users()
        
        print(f"Message reçu de {sender.first_name}: {event.text}")
        
        # Si c'est le premier message de cet utilisateur, on répond automatiquement
        if user_id not in responded_users:
            print(f"Premier message de {sender.first_name}, envoi de la réponse automatique")
            await event.reply(message_auto)
            # Ajouter l'utilisateur à la liste des répondues
            responded_users.append(user_id)
            save_responded_users(responded_users)
        else:
            print(f"Message de {sender.first_name} ignoré (déjà répondu)")

print("🤖 Auto-répondeur actif... (Ctrl+C pour arrêter)")
client.start()
client.run_until_disconnected()
