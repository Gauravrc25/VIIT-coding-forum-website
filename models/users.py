import psycopg2, os
from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

def check_key(key):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    

    cur = conn.cursor()
    
    try:
        cur.execute("select id from post where key ='{0}'".format(key))
        if cur.rowcount != 0:
            return True
        else :
            return False
    except Exception as e:
        print(e)
        
    finally:
        cur.close()
        conn.close()
# email key type
def new_post(email,typel,key):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    cur = conn.cursor()
    #email = input("Email : ")
    email = email.lower()
    #typel = input("type : ")
    typel = typel.lower()
    #key = "12345697"
    user_id = 0
    try:
        cur.execute("select id from users where username='{0}'".format(email))
        data = cur.fetchone()
        #while data is not None:
        user_id = data[0]
            
        if cur.rowcount == 0:
            cur.execute("insert into users(username) values('{0}')".format(email))
            conn.commit()
            print("Inserted")
            cur.execute("select id from users where username='{0}'".format(email))
            data = cur.fetchone()
            #while data is not None:
            user_id = data[0]
        
        cur.execute("insert into post(type,key,isactive,user_id) values('{0}','{1}','t',{2})".format(typel,key,user_id))
        conn.commit();       
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    #print("Inserted")

#new_post()

