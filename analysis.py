from models import *

if __name__ == "__main__":
    session = Session()
    ret_list = session.query(Comment).filter(Comment.user_name == "TOPMACHINE").all()
    print len(ret_list)

