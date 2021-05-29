import sqlite3

def execute_query(sql_query):
    with sqlite3.connect("Data.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result

def add_content(content_name,content_post):
    sql_query = "INSERT INTO Data(content_name,content_post) VALUES('%s','%s')" %(content_name,content_post)
    execute_query(sql_query)
    
def get_content_name():
    sql_query = "SELECT content_name FROM Data"
    content = execute_query(sql_query)
    return [content_name[0] for content_name in content.fetchall()]

def get_content_post():
    sql_query = "SELECT content_post FROM Data"
    content = execute_query(sql_query)
    return [content_post[0] for content_post in content.fetchall()]

