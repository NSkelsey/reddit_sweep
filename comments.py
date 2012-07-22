import urllib2
import pprint
import json
from datetime import datetime
from IPython import embed
from models import Comment, User, session
from time import sleep

url = "http://www.reddit.com/r/news/comments/wyo6w/anaheim_pd_fires_on_crowd_of_women_and_small/"

def addToSubComments(subComments, id_c, i):
    print "it kind of worked"
    sleep(3)
    subUrl = url + id_c
    bd = getJson(subUrl)
    subComments[i] = bd[1]["data"]["children"]




def buildTree(subtree):

    subComments = subtree["data"]["children"]
    
    for i in range(len(subComments)):
        
        if subComments[i].get("data").get("children") and type(subComments[i]["data"]["children"].get()) == unicode:
            #embed()
            addToSubComments(subComments, subComments[i], i)
        
        print i
        #embed()
        if subComments[i]["data"]["replies"] != "":
            buildTree(subComments[i]["data"]["replies"])





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
    url = url + ".json"
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    rawText = opener.open(url).read()
    return json.loads(rawText)
    



if __name__ == "__main__":
    
    p = pprint.PrettyPrinter(indent=4)
    
       
    bd = getJson(url)
    c = bd[1]
    parent = Comment(user_name = "Ale and Nick", upvotes = int(9999999))
    
    buildTree(c)
    #addToDatabase(parent, c, 0)
    #session.add(parent)
    #session.commit()
    printComments(c, 0)

