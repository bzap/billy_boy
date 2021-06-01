import discord 
import asyncpraw 
import asyncio

reddit = asyncpraw.Reddit(client_id='9bfw125sbnQY9Q', client_secret='dX7Xnh1xDJVKaLqAm4dgobmim68S6w', user_agent='my_user_agent')


#hot_posts = reddit.subreddit('SamsungGirlr34').hot(limit=10)
#for post in hot_posts: 
#    print(post.url)


async def get_newest():
    post_info = []
    newest1 = await reddit.subreddit('SamsungGirlr34')
    newest = newest1.new(limit=1)
    async for post in newest: 
        print(post.url)
        if (post.url.endswith('jpg') or post.url.endswith('png')): 
            print(post.url)
            post_info.append([post.url, post.title, post.author.name])
            return post_info 
        else: 
            post_info.append([post.selftext, post.title, post.author.name])
            return post_info 


async def get_top(): 
    post_info = []
    current_top1 = await reddit.subreddit('SamsungGirlr34')
    current_top = current_top1.top(limit=1)
   #subreddit = await reddit.subreddit("SamsungGirlr34")
    async for post in current_top: 
        print(post.url)
        
        if (post.url.endswith('jpg') or post.url.endswith('png')): 
            print(post.url)
            post_info.append([post.url, post.title, post.author.name])
            return post_info 
        else: 
            post_info.append([post.selftext, post.title, post.author.name])
            return post_info 
         
async def get_newestS():
    post_info = []
    newest1 = await reddit.subreddit('SubwayHentai')
    newest = newest1.new(limit=1)
    async for post in newest: 
        print(post.url)
        if (post.url.endswith('jpg') or post.url.endswith('png')): 
            print(post.url)
            post_info.append([post.url, post.title, post.author.name])
            return post_info 
        else: 
            post_info.append([post.selftext, post.title, post.author.name])
            return post_info 


async def get_topS(): 
    post_info = []
    current_top1 = await reddit.subreddit('SubwayHentai')
    current_top = current_top1.top(limit=1)
   #subreddit = await reddit.subreddit("SamsungGirlr34")
    async for post in current_top: 
        print(post.url)
        
        if (post.url.endswith('jpg') or post.url.endswith('png')): 
            print(post.url)
            post_info.append([post.url, post.title, post.author.name])
            return post_info 
        else: 
            post_info.append([post.selftext, post.title, post.author.name])
            return post_info 
#loop = asyncio.get_event_loop()
#loop.run_until_complete(get_top())

