import discord
import os
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()

TOKEN = os.getenv("TOKEN")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hey there! welcome to CP Algorithm Group")
    if message.content == "hi!":
        await message.author.send("Hey there! welcome to CP Algorithm Group private message ")


@client.event
async def on_connect():
    print("Bot is connecting to server")
    channel = client.get_channel(862313199353331762)
    await channel.send("connect to bot_command")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'welcome {member}')

client.run(TOKEN)
