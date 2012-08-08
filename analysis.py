from models import *
import urllib2


def login():
    data = "api_type=json&user=doyourworkk&passwd=123456"
    headers = {"Content-Length": len(data)}
    url = "http://www.reddit.com/api/login/doyourworkk"
    
    req = urllib2.Request(url, data, headers)
    f = urllib2.urlopen(req)
    return f.read()
    

if __name__ == "__main__":
    session = Session()
 #   ret_list = session.query(Comment).filter(Comment.user_name == "TOPMACHINE").all()
#    print ret_list
    print login()
    
def submit
    cookie = cookie["json"]["data"]["cookie"]          
    modhash = modhash["json"]["data"]["modhash"]                             
     data = "uh=" + modhash + "&kind=self&url=testpost1&sr=political_economy&title=herp_a_derp"
     headers = {"cookie": cookie, "Content-Length": len(data)}      
     url = "http://www.reddit.com/api/submit"
     req = urllib2.Request(url,data,headers)    
      f = urllib2.urlopen(req)

