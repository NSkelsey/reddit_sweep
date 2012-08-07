from models import *

if __name__ == "__main__":
    session = Session()
    ret_list = session.query(Comment).filter(Comment.user_name == "Ale and Nick").all()
    print ret_list

