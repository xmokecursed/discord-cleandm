# Cleans dm with all users
# Made by Xm0k3

import os
os.system("pip install discord.py-self")
import discord
import asyncio
import random
import json

# VALUES TO FILL
token = ""   # discord user token
prefix = ""  # prefix ex. (! ? .)
limit = ""   # amount of messages to delete | default is 1

# delays
min_delay = 2
max_delay = 5

#after cleaning dm user's id gets add to this file and wont be cleaned again if this program is run again.
skips = "deleted_users.json"

def load_deleted_users():
    if os.path.exists(skips):
        with open(skips, "r") as f:
            data = json.load(f)
            return set(data.get("deleted_user_ids", []))
    return set()

def save_deleted_user(user_id: int):
    deleted = load_deleted_users()
    deleted.add(user_id)
    with open(skips, "w") as f:
        json.dump({"deleted_user_ids": sorted(list(deleted))}, f, indent=2)
    print(f"Saved user ID {user_id} to {skips}")

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author != client.user:
        return
    elif message.content.startswith(f"{prefix}cleandm"):
        total = 0
        deleted_users = load_deleted_users()
        for dms in client.private_channels:
            try:
                recipient = dms.recipient
                recipient_id = recipient.id if recipient else None
            except AttributeError:
                try:
                    recipient_id = dms.recipients[0].id if dms.recipients else None
                except (AttributeError, IndexError):
                    recipient_id = None
            if recipient_id and recipient_id in deleted_users:
                print(f"Skipping {recipient_id} — already cleaned previously.")
                continue
            deleted = 0
            async for msg in dms.history(limit=1):
                if msg.author == client.user:
                    try:
                        await msg.delete()
                        deleted += 1
                        await asyncio.sleep(random.uniform(min_delay, max_delay))
                    except discord.errors.HTTPException as e:
                        if e.status == 429:
                            print("Rate limited — stopping command.")
                            break
                        else:
                            print("Some error occurred — stopping command.")
                            break
            if deleted > 0:
                try:
                    print(f"Deleted {deleted} messages with {dms.recipients}")
                except AttributeError:
                    print(f"Deleted {deleted} messages with {dms.recipient}")
                if recipient_id:
                    save_deleted_user(recipient_id)

            total += deleted

        print(f"Total deleted: {total}")

client.run(token)
