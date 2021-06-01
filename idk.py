import discord 
import praw 


reddit = praw.Reddit(client_id='9bfw125sbnQY9Q', client_secret='dX7Xnh1xDJVKaLqAm4dgobmim68S6w', user_agent='my_user_agent')


#hot_posts = reddit.subreddit('SamsungGirlr34').hot(limit=10)
#for post in hot_posts: 
#    print(post.url)

post_info = []
def get_newest(): 
    newest = reddit.subreddit('SamsungGirlr34').new(limit=1)
    for post in newest: 
        #print(post.url)
        if (post.url.endswith('jpg') or post.url.endswith('png') == True): 
            print(post.url)
            post_info.append([post.url, post.title])
            return post_info 
        else: 
            post_info.append([post.body, post.title])
            return post_info 


def get_top(): 
    current_top = reddit.subreddit('SamsungGirlr34').top(limit=1)
    for post in current_top: 
        #print(post.url)
        if (post.url.endswith('jpg') or post.url.endswith('png') == True): 
            print(post.url)
            post_info.append([post.url, post.title, post.author.name])
            return post_info 
        else: 
            post_info.append([post.body, post.title, post.author.name])
            return post_info 

print(get_top())
