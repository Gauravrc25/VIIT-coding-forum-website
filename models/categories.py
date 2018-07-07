import os, psycopg2
from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

def insert_category(category):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cid = 0
    cur = conn.cursor()
    category = category.lower()
    try:
        cur.execute("Select id from categories where category_title='{0}'".format(category))
        data = cur.fetchone()
        cid = data[0]
        
        if cur.rowcount == 0:
            cur.execute("insert into categories(category_title) values('{0}')".format(category))
            conn.commit()
            #print("inserted")
            cur.execute("select id from categories where category_title='{0}'".format(category))
            data = cur.fetchone()
            cid = data[0]
        
        else:
            print("Category Exists already")
        print(cid)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        

def delete_category(category):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    
    try:
        cur.execute("delete from categories where category_title='{0}'".format(category))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
