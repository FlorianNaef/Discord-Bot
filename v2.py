import discord
import os
import requests

client = discord.Client()

with open("api_file.bin", encoding="utf-8") as binary_file:
    api_key = binary_file.read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('done')

@client.event
async def on_message(message):  
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
            await message.channel.send("Hello!")
    else:
        await message.channel.send("sorry command not found!")

client.run(api_key)

