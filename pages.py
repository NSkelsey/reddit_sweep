from comments import *
from models import Post, session


url = "http://www.reddit.com/r/Python/"


def addPostToDatabase(thread):
    post = Post()
    post.name =  thread["data"]["title"]
    post.url =  "http://www.reddit.com" + thread["data"]["permalink"]
    post.upvotes =  thread["data"]["ups"]
    post.downs = thread["data"]["downs"]
    session.add(post)
    return post


def scrapeThreads(threads):
        
    counter = 0
    for thread in threads:
        print thread["data"]["title"], "\n"
        sleep(1)
        post = addPostToDatabase(thread)
        scrapeThread(post)
        counter += 1
    
    print counter


if __name__ == "__main__":
    bd = getJson(url)
    p = pprint.PrettyPrinter(indent=4)
    scrapeThreads(bd["data"]["children"])    

    #p.pprint(bd)    






""""
EXAMPLE POST JSON
{   u'data': {u'approved_by': None,
           u'author': u'ben_liles',
           u'author_flair_css_class': None,
           u'author_flair_text': None,
           u'banned_by': None,
           u'clicked': False,
           u'created': 1343189535.0,
           u'created_utc': 1343164335.0,
           u'domain': u'pytexas.org',
           u'downs': 5,
           u'edited': False,
           u'hidden': False,
           u'id': u'x3eab',
           u'is_self': False,
           u'likes': None,
           u'link_flair_css_class': None,
           u'link_flair_text': None,
           u'media': None,
           u'media_embed': {   },
           u'name': u't3_x3eab',
           u'num_comments': 0,
           u'num_reports': None,
           u'over_18': False,
           u'permalink': u'/r/Python/comments/x3eab/pytexas_2012_call_for_proposals/',
           u'saved': False,
           u'score': 8,
           u'selftext': u'',
           u'selftext_html': None,
           u'subreddit': u'Python',
           u'subreddit_id': u't5_2qh0y',
           u'thumbnail': u'',
           u'title': u'PyTexas 2012 Call for Proposals',
           u'ups': 13,
           u'url': u'http://www.pytexas.org/chance/1/talks/'},
u'kind': u't3'}

"""


