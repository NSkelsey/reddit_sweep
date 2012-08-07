import urllib2
import pprint
import json
from datetime import datetime
from IPython import embed
from models import Comment, User, session
from time import sleep



def addToSubComments(post, subComments, id_c, i, length):
    sleep(1)
    bd = getJson(post.url)
    new_comm_list = bd[1]["data"]["children"]
    
    for j in range(len(new_comm_list)):
        
        subComments[i] = new_comm_list[j]
        
        #print len(subComments)




def buildTree(post, subtree):

    subComments = subtree["data"]["children"]
    length = range(len(subComments))
    for i in length:
        if subComments[i]["data"].get("replies") is None and subComments[i]["data"].get("children") is not None:
            #embed()
            addToSubComments(post, subComments, subComments[i], i, length)
            buildTree(post, subtree)
            break
        #embed()
        if subComments[i]["data"].get("replies") is not None and subComments[i]["data"]["replies"] != "":
            buildTree(post, subComments[i]["data"]["replies"])




def addToDatabase(parent, subtree, i):

    subComments = subtree["data"]["children"]
    if len(subComments) == 0:
        pass
        #print "List EMPTY"

    for j in subComments:
        comment = Comment()
        comment.reddit_id = j["data"]["id"]
        comment.text = j["data"]["body"]
        comment.user_name = j["data"]["author"]
        comment.upvotes = int(j["data"]["ups"])
        comment.downvotes = j["data"]["downs"]
        comment.date_of_last_sweep = datetime.now()
        comment.parent = parent
        comment.post_id = parent.post_id
        session.add(comment)

        if j["data"]["replies"] == "":
            pass
            #print "Dict Empty"
            #print type(j["data"]["replies"])

        else:
            addToDatabase(comment, j["data"]["replies"], i + 1)
    
    
    """
    text = body
    user = author
    upvotes = ups

    """

def printComments(subtree, i):
    try:
        subComments = subtree["data"]["children"]
    except:
        pass

    #i += 2
    for j in subComments:
        #print i*" ",j["data"]["body"], "\n"
        
        global c1
        c1 += 1
        print c1
        print j["data"]["body"], "\n"
        try:
            printComments(j["data"]["replies"], i)
        except:
            pass
     
def getJson(url):
    url = url + ".json"
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    rawText = opener.open(url).read()
    return json.loads(rawText)
    

def scrapeThread(post):
    bd = getJson(post.url)
    c = bd[1]
    parent = Comment(post_id=post.id, user_name="TOPMACHINE")
    buildTree(post, c)
    addToDatabase(parent, c, 0)
    
    session.add(parent)
    session.commit()

if __name__ == "__main__":
    url = "http://www.reddit.com/r/videos/comments/x98mj/5_minute_extended_trailer_for_the_new_wachowskis/"
    bd = getJson(url)
    c = bd[1]
    parent = Comment(reddit_id="YESYES", user_name = "Ale and Nick", upvotes=0, date_of_last_sweep=datetime.now())
    addToDatabase(parent, c, 0)


    buildTree(url, c)
    addToDatabase(parent, c, 0)
    session.add(parent)



    session.commit()
"""
p = pprint.PrettyPrinter(indent=4)
p = pprint.PrettyPrinter(indent=4)
p = pprint.PrettyPrinter(indent=4)
p = pprint.PrettyPrinter(indent=4)
i = 0
printComments(c, i)
global c1
print c1
"""


#p = pprint.PrettyPrinter(indent=4)
#p.pprint(bd)


"""
EXAMPLE COMMENT DATA
{ u'data': {u'approved_by': None,
           u'author': u'UUGE_ASSHOLE',
           u'author_flair_css_class': None,
           u'author_flair_text': None,
           u'banned_by': None,
           u'body': u'A 5 minute trailer is one of the 3 worst ideas I have ever heard of',
           u'body_html': u'&lt;div class="md"&gt;&lt;p&gt;A 5 minute trailer is one of the 3 worst ideas I have ever heard of&lt;/p&gt;\n&lt;/div&gt;',
           u'created': 1343452921.0,
           u'created_utc': 1343427721.0,
           u'downs': 5,
           u'edited': False,
           u'id': u'c5kfzfc',
           u'likes': None,
           u'link_id': u't3_x98mj',
           u'name': u't1_c5kfzfc',
           u'num_reports': None,
           u'parent_id': u't3_x98mj',
           u'replies': u'',
           u'subreddit': u'videos',
           u'subreddit_id': u't5_2qh1e',
           u'ups': 1},
u'kind': u't1'}
"""
