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
        if len(self.music_queue) > 0:
            self.state = True 
            url = self.song_queue[0][0]
            self.song_queue.pop(0)
        else: 
            self.state = False 

    async def play_song(self, ctx, client): 
        if (len(self.song_queue) > 0): 
            self.state = True 
            url = self.song_queue[0][0]
            print("LOLOlolOLl")
            print(type(ctx.author.voice.channel))
            self.vc = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel))
            await self.vc.connect() 
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio(url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else: 
            self.state = False 




#test = music_controller() 
#print(test.get_info('https://www.youtube.com/watch?v=gkxGs4ETeg4'))
