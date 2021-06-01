import os 
import discord

from dotenv import load_dotenv

load_dotenv() 
TOKEN = 'ODQ5MTIzMzg4NTY2Nzk4MzY4.YLWlxw.pyJX_ePIxIP9ynOAWQHijndJ450'

client = discord.Client() 


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
            
    elif message.content == ('!b'):
        await message.channel.send("bill gates ain't no spot up shooter he aint gotta run to the corner to shoot like hes some 3rd option bitch this aint jj redick this is a fuckin god human steph curry come again only this time hes not a fuckin pussy pull up from the fuckin logo and fight you at the same time")




client.run(TOKEN)