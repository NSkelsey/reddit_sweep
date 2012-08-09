from models import *
import urllib2
import json
from sqlalchemy import and_ , desc

   
def submit(cookie, modhash):
    data = "uh=" + modhash + "&kind=self&url=testpost1&sr=political_economy&title=herp_a_derp"
    headers = {"cookie":  "reddit_session="+ cookie, "Content-Length": len(data)}      
    url = "http://www.reddit.com/api/submit"
    req = urllib2.Request(url,data,headers)    
    f = urllib2.urlopen(req)
    return f.read()

def login():
    data = "api_type=json&user=acccurrent&passwd=123456"
    headers = {"Content-Length": len(data)}
    url = "http://www.reddit.com/api/login/acccurrent"
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    s = f.read()
    print s
    return json.dumps(s)


def solve_captcha():
    url = "http://www.reddit.com/api/new_captcha"
    #headers = {'User-agent': 'Mozilla/5.0', }
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    print f.read()

if __name__ == "__main__":
    session = Session()
    ret_list = session.query(Comment).filter(and_(Comment.user_name != "TOPMACHINE")).order_by(desc(Comment.weight)).limit(25).all()
    s = [(comment.text[:50], comment.post.name[:10], comment.weight) for comment in ret_list]
    for i in s:
        print i

    print "="*600
    ret_list = session.query(Comment).filter(Comment.user_name != "TOPMACHINE").order_by(desc(Comment.upvotes)).limit(25).all()
    s = [(comment.text[:50], comment.post.name[:10], comment.upvotes) for comment in ret_list]
    for i in s:
        print i










    """#d = login()
    #d = {"json": {"errors": [], "data": {"modhash": "jbu6i3run06743b6d765429d6fd5785fbc92da44481e8f239d", "cookie": "6326653,2012-08-08T14:53:39,f61d1ccef7d6063882e54a73a6b2b22be31e8e04"}}}
    #cookie = d["json"]["data"]["cookie"]
    #modhash = d["json"]["data"]["modhash"]
    #print cookie, modhash
    print submit(cookie, modhash)"""



