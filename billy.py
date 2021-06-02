import os 
import discord
from discord.ext import commands 
from datetime import timedelta
from dotenv import load_dotenv
from music_controller import music_controller
from idk import get_newest, get_top, get_topS, get_newestS

load_dotenv() 
TOKEN = 'ODQ5MTIzMzg4NTY2Nzk4MzY4.YLWlxw.pyJX_ePIxIP9ynOAWQHijndJ450'

client = commands.Bot(command_prefix="#")

song_queue = {} 
controller = music_controller()
command_count = 0 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


            
@client.command()
async def play(ctx, arg):
        content = controller.get_info(arg) 
          #  if controller.get_queue_size() > 1: 
          #      ctx.send('added to queue')
        controller.add_to_queue(content) 
        if not(controller.check_state()):
            print('gothere') 
            await controller.play_song(ctx, client)
            print(content) 
            embed=discord.Embed(title=content[1], color=0xFF5733)
            embed.set_thumbnail(url=content[2])
            embed.add_field(name='Duration: ', value=str(timedelta(seconds = int(content[3]))), inline=True)
            embed.add_field(name='Queue: ', value=str(controller.get_queue_size()), inline=True)
            await ctx.send(embed=embed) 
        else: 
            await ctx.send('added to queue xoxo')  
            embed=discord.Embed(title=content[1], color=0xFF5733)
            embed.set_thumbnail(url=content[2])
            embed.add_field(name='Duration: ', value=str(timedelta(seconds = int(content[3]))), inline=True)
            embed.add_field(name='Queue: ', value=str(controller.get_queue_size()), inline=True)
            await ctx.send(embed=embed)  

@client.command()
async def skip(ctx):
        if (controller.check_state()):
            controller.stop_music()
            await controller.play_song(ctx, client)    



@client.command()
async def stop(ctx):
        await controller.stop_music(ctx)  



@client.command()
async def sam(ctx, arg):
        if (arg == 'top'): 
            content = await get_top() 
            if (content[0][0].endswith('jpg') or content[0][0].endswith('png')): 
                embed=discord.Embed(title=content[0][1], url=content[0][0], color=0xFF5733)
                embed.set_image(url=content[0][0])
                embed.set_footer(text='u/' + content[0][2])
            else: 
                embed=discord.Embed(title=content[0][1], description=content[0][0], color=0xFF5733)
                embed.set_footer(text='u/' + content[0][2])
            await ctx.send(embed=embed)         
  

        elif (arg == 'new'): 
            content = await get_newest()  
            if (content[0][0].endswith('jpg') or content[0][0].endswith('png')): 
                embed=discord.Embed(title=content[0][1], url=content[0][0], color=0xFF5733)
                embed.set_image(url=content[0][0])
                embed.set_footer(text='u/' + content[0][2])
            else: 
                embed=discord.Embed(title=content[0][1], description=content[0][0], color=0xFF5733)
                embed.set_footer(text='u/' + content[0][2])
            await ctx.send(embed=embed)       

@client.command()
async def subway(ctx, arg):
        if (arg == 'top'): 
            content = await get_topS() 
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