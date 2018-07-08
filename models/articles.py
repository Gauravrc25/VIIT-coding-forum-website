import psycopg2, os
from datetime import datetime
from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])


def create_article(category,article_title,sub_title,posted_by,content):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    '''category = int(input("Category : "))
    article_title = input("Article Title : ")
    sub_title = input("Sub Title : ")
    posted_by = input("Posted By : ")
    content = input("Content : ")'''
    try:
        cur.execute("insert into articles (category,article_title,sub_title,posted_by,content) values({0},'{1}','{2}','{3}','{4}')".format(category, article_title, sub_title, posted_by, content))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    #print("Inserted")


def delete_article(article_id):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    #article_id = int(input("id : "))
    try:
        cur.execute("delete from articles where id = {0}".format(article_id))
        #print("{0} article deleted".format(article_id))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

    
def edit_article(article_id,article_title,sub_title,posted_by,content):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    #article_id = int(input("ID : "))
    #article_title = input("Article Title : ")
    #sub_title = input("Sub Title : ")
    #posted_by = input("Posted By : ")
    #content = input("Content : ")
    try :
        cur.execute("update articles set article_title = '{0}', sub_title = '{1}', posted_by = '{2}', content = '{3}' where id = {4}".format(article_title, sub_title, posted_by, content, article_id))
        conn.commit()
        #print("Inserted")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    
