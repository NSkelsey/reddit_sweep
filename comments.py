import urllib2
import pprint
import json
from datetime import datetime
from IPython import embed
from models import Comment, User, session
from time import sleep

url = "http://www.reddit.com/r/gaming/comments/vnwl7/skyrim_logic/"

def addToSubComments(subComments, id_c, i, length):
    sleep(1)
    subUrl = url + id_c["data"]["id"]
    bd = getJson(subUrl)
    new_comm_list = bd[1]["data"]["children"]
    
    for j in range(len(new_comm_list)):
        
        subComments[i] = new_comm_list[j]
        
        print len(subComments)




def buildTree(subtree):

    subComments = subtree["data"]["children"]
    length = range(len(subComments))
    for i in length:
        if subComments[i]["data"].get("replies") is None and subComments[i]["data"].get("children") is not None:
            #embed()
            addToSubComments(subComments, subComments[i], i, length)
            buildTree(subtree)
            break
        #embed()
        if subComments[i]["data"].get("replies") is not None and subComments[i]["data"]["replies"] != "":
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
    addToDatabase(parent, c, 0)
    session.add(parent)
    session.commit()
   # printComments(c, 0)

