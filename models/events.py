import psycopg2, os
from datetime import datetime
from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])


def create_event(category,event_title,sub_title,posted_by,content,location,event_date,event_time,duration):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    
    '''category = int(input("Category : "))
    event_title = input("Event Title : ")
    sub_title = input("Sub Title : ")
    posted_by = input("Posted By : ")
    content = input("Content : ")
    location = input("Location : ")
    event_date = input("Date of event : ")
    event_time = input("Enter event time : ")'''
    event_timestamp = event_date + " " + event_time
    event_at = datetime.strptime(event_timestamp, "%d/%m/%Y %H:%M:%S")
    #duration = input("Duration of event : ")
    try :    
        cur.execute("insert into events (category,event_title,sub_title,posted_by,posted_at,content,location,event_at,duration) values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(category, event_title, sub_title, posted_by, datetime.now(), content, location, event_at, duration))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    #print("Inserted")
    

def edit_event(event_id,category,event_title,sub_title,posted_by,content,location,event_date,event_time,duration):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    '''
    event_id = int(input("ID : "))
    category = int(input("Category : "))
    event_title = input("Event Title : ")
    sub_title = input("Sub Title : ")
    posted_by = input("Posted By : ")
    content = input("Content : ")
    location = input("Location : ")
    event_date = input("Date of event : ")
    event_time = input("Enter event time : ")
    duration = input("Duration of event : ")
    '''
    event_timestamp = event_date + " " + event_time
    event_at = datetime.strptime(event_timestamp, "%d/%m/%Y %H:%M:%S")
    try :
        cur.execute("update events set category={0}, event_title='{1}', sub_title='{2}', posted_by='{3}', posted_at='{4}', content='{5}', location='{6}', event_at='{7}', duration='{8}' where id = {9}".format(category, event_title, sub_title, posted_by, datetime.now(), content, location, event_at, duration, event_id))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    #print("Updated")
    
def delete_event(event_id):
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()
    #event_id = int(input("id : "))
    try:
        cur.execute("delete from events where id = {0}".format(event_id))
        #print("{0} event deleted".format(event_id))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
