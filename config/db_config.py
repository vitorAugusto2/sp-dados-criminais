import psycopg2

def get_db_config():
    conn = psycopg2.connect(
        dbname="*****",           
        user="*****",             
        password="*****",       
        host="*****",             
        port="*****"           
    )
    
    return conn