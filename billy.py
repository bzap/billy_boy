import os 
import discord
from discord.ext import commands 
from dotenv import load_dotenv
from music_controller import music_controller
from idk import get_newest, get_top, get_topS, get_newestS

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
async def sam(ctx, arg):
        if (arg == 'top'): 
            content = await get_top() 
            print(content)
            print('i got here')
            embed=discord.Embed(title=content[0][1], url=content[0][0], description='u/' + content[0][2], color=0xFF5733)
            embed.set_image(url=content[0][0])
            await ctx.send(embed=embed)           

        elif (arg == 'new'): 
            content = await get_newest()  
            if (content[0][0].endswith('jpg') or content[0][0].endswith('png')): 
                embed=discord.Embed(title=content[0][1], url=content[0][0], description='u/' + content[0][2], color=0xFF5733)
                embed.set_image(url=content[0][0])
            else: 
                embed=discord.Embed(title=content[0][1], description=content[0][0], color=0xFF5733)
            await ctx.send(embed=embed)       

@client.command()
async def subway(ctx, arg):
        if (arg == 'top'): 
            content = await get_topS() 
            print(content)
            print('i got here')
            embed=discord.Embed(title=content[0][1], url=content[0][0], description='u/' + content[0][2], color=0xFF5733)
            embed.set_image(url=content[0][0])
            await ctx.send(embed=embed)           

        elif (arg == 'new'): 
            content = await get_newestS()  
            if (content[0][0].endswith('jpg') or content[0][0].endswith('png')): 
                embed=discord.Embed(title=content[0][1], url=content[0][0], description='u/' + content[0][2], color=0xFF5733)
                embed.set_image(url=content[0][0])
            else: 
                embed=discord.Embed(title=content[0][1], description=content[0][0], color=0xFF5733)
            await ctx.send(embed=embed)     

client.run(TOKEN)