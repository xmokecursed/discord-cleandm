# Cleans dm with all users
# Made by Xm0k3

import os
os.system("pip install discord.py-self")
import discord
from discord import commands
import asyncio
import random

#VALUES TO FILL
token = "" #discord user token
prefix = "" #prefix ex. (! ? .)
limit = "" #amount of messages to delete | default is 1

#delays
min = 2
max = 5

client = discord.Client()

@client.event
async def on_ready():
    print(f"logged as {client.user}")

@client.event
async def on_message(message):
    if message.author != client.user:
        return
    elif message.content.startswith(f"{prefix}cleandm"):
        total = 0
        for dms in client.private_channels:
            deleted = 0
            async for msg in dms.history(limit=1):
                if msg.author == client.user:
                    try:
                        await msg.delete()
                        deleted += 1
                        if deleted > 0:
                            try:
                                print(f"deleted {deleted} messages with {dms.recipients}")
                                continue
                            except:
                                print(f"deleted {deleted} messages with {dms.recipient}")
                                continue
                        await asyncio.sleep(random.uniform(min, max))
                    except discord.errors.HTTPException as e:
                        if e.status == 429:
                            print(f"rate limited stopping command")
                            break
                        else:
                            print("some error occured stopping command")
                            break
            total += deleted
        print(f"total deleted: {total}")

client.run(token)
