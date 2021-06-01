import os 
import discord
from discord.ext import commands 
from dotenv import load_dotenv
from music_controller import music_controller
from idk import get_newest, get_top 

load_dotenv() 
TOKEN = 'ODQ5MTIzMzg4NTY2Nzk4MzY4.YLWlxw.pyJX_ePIxIP9ynOAWQHijndJ450'

client = commands.Bot(command_prefix="#")

song_queue = {} 




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


            
@client.command()
async def play(ctx, arg):
        controller = music_controller() 
        content = controller.get_info(arg) 
        print(content)
        controller.add_to_queue(content) 
        print('gothere')
        
        if not(controller.check_state()):
            print('gothere') 
            await controller.play_song(ctx, client)


@client.command()
async def bill(ctx, arg):
        if (arg == 'top'): 
            content = await get_top() 
            print(content)
            print('i got here')
            embed=discord.Embed(title=content[0][1], url=content[0][0], description='u/' + content[0][2], color=0xFF5733)
            embed.set_image(url=content[0][0])
            await ctx.send(embed=embed)           

        elif (arg == 'new'): 
            content = await get_newest()  
            
            embed=discord.Embed(title=content[0][1], url=content[0][0], description="This is an embed that will show how to build an embed and the different components", image=content[0][0], color=0xFF5733)
            embed.set_image(url=content[0][0])
            await ctx.send(embed=embed)       



client.run(TOKEN)