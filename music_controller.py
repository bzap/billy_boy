from math import e
import discord 
from discord.ext import commands 
from youtube_dl import YoutubeDL 

class music_controller(): 
    def __init__(self):  
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        self.state = False 
        self.song_queue = [] 
        self.song_info = [] 
        self.vc = '' 
        self.voice = ''

    def check_state(self): 
        return self.state

    def add_to_queue(self, song): 
        self.song_queue.append(song) 

    def get_info(self, info): 
        yt = YoutubeDL({'format': 'bestaudio', 'noplaylist':'True', 'match_filter' : '!is_live'})
        try: 
            yt_details = yt.extract_info("ytsearch:%s" % info, download = False)['entries'][0]
        except Exception: 
            return False 

        url = yt_details.get("url", None)
        title = yt_details.get("title", None)
        self.song_info = [url, title]
        return self.song_info
        
    def next_song(self): 
        if len(self.song_queue) > 0 and self.vc.is_connected():
            self.state = True 
            url = self.song_queue[0][0]
            self.song_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(url, **self.FFMPEG_OPTIONS), after=lambda e: self.next_song())
        else: 
            self.state = False 

    async def play_song(self, ctx, client): 
        if (len(self.song_queue) > 0): 
            self.state = True 
            url = self.song_queue[0][0]

            if (ctx.voice_client): 
                await ctx.guild.voice_client.disconnect()

            if (ctx.author.voice):
                channel = ctx.author.voice.channel 
                self.vc = await channel.connect()
                self.vc.play(discord.FFmpegPCMAudio(url, **self.FFMPEG_OPTIONS), after=lambda e: self.next_song())
            else: 
                await ctx.send("pls join a voice channel to use this this xoxo")

            #if self.vc != '' or self.vc != None: 
            #    self.vc = await discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel)).disconnect()

            #elif self.vc == "" or not self.vc.is_connected() or self.vc == None:
            #    self.vc = await discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel)).connect()
            #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            #if (voice.is_connected()):
            #    voice.play(discord.FFmpegPCMAudio(url, **self.FFMPEG_OPTIONS), after=lambda e: self.next_song(voice))
            #elif(self.vc == None or not voice.is_connected()):
            #    voice.disconnect()
        else: 
            self.state = False 




#test = music_controller() 
#print(test.get_info('https://www.youtube.com/watch?v=gkxGs4ETeg4'))
