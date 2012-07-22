import urllib2
import pprint
import json
from datetime import datetime
from IPython import embed
from models import Comment, User, session

url = "http://www.reddit.com/r/Python/comments/wpl1h/what_are_some_little_known_features_in_python/.json"
def addToDatabase(parent, subtree, i):

    #try:
    
    subComments = subtree["data"]["children"]
    if len(subComments) == 0:
        print "List EMPTY"
    #except:
    #    pass

    for j in subComments:
        comment = Comment()
        comment.text = j["data"]["body"]
        comment.user_name = j["data"]["author"]
        comment.upvotes = int(j["data"]["ups"])
        comment.date_of_last_sweep = datetime.now()
        comment.parent = parent
        session.add(comment)
        print i    
        #embed()
        #   try:

        if j["data"]["replies"] == "":
            print "Dict Empty"
            #print type(j["data"]["replies"])

        else:
            addToDatabase(comment, j["data"]["replies"], i + 1)
        #except:
         #   pass
    
    
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

    i += 2
    for j in subComments:
        print i*" ", j["data"]["body"], "\n"

        try:
            printComments(j["data"]["replies"], i)
        except:
            pass
     
def getJson(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    rawText = opener.open(url).read()
    return json.loads(rawText)
    



if __name__ == "__main__":
    
    p = pprint.PrettyPrinter(indent=4)
    
       
    bd = getJson(url)
    c = bd[1]
    parent = Comment(user_name = "Ale and Nick", upvotes = int(9999999))


    addToDatabase(parent, c, 0)
    session.add(parent)
    session.commit()
   # printComments(c, 0)

