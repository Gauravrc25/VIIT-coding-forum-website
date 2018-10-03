import psycopg2, os
from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])


def check_admin_credentials(email,key):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    email = email.lower()
    
    uid = 0
    cur = conn.cursor()
    
    try :
        cur.execute("select id from admin where admin_name = '{0}'".format(email))
        data = cur.fetchone()
        if data == None:
            return False,-1
        
        cur.execute("select id from admin where admin_name='{0}' and key = '{1}'".format(email,key))
        data = cur.fetchone()
        if data == None:
            return False,-1
        else:
            uid = data[0]
            return True,uid

    except Exception as e:
        print(e)
        
    finally:
        cur.close()
        conn.close()
