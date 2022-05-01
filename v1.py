import discord
import os
import requests

client = discord.Client()


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

client.run('ODQxNzQ5Mzk3MzA2MjEyMzcy.YJrSNw._LN0UYK3CXXDo9guZsEp_uwIRPE')

