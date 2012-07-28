from comments import *
from models import Post, session


url = "http://www.reddit.com/r/Python/"


def addPostToDatabase(thread):
    post = Post()
    post.name =  thread["data"]["title"]
    post.url =  "http://www.reddit.com" + thread["data"]["permalink"]
    post.upvotes =  thread["data"]["ups"]


def scrapeThreads(threads):
        
    counter = 0
    for thread in threads:
        print thread["data"]["title"], "\n"
        url = "http://www.reddit.com" + thread["data"]["permalink"]
        sleep(1)
        scrapeThread(url, thread["data"]["title"])
        counter += 1
    
    print counter


if __name__ == "__main__":
    bd = getJson(url)
    p = pprint.PrettyPrinter(indent=4)
    #scrapeThreads(bd["data"]["children"])    

    p.pprint(bd)    


    
