import psycopg2
from config import load_config
from connect import connect

def insert_conacts(tup ):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO contacts (name,phone_number)
                            VALUES {}
                            """.format(tup))
                conn.commit()
    except (psycopg2.DatabaseError,Exception) as error:
        print (error)

def insert_contacts_location(tup):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO contacts_location (name, city, address)
                            VALUES {}
                            """.format(tup))
                conn.commit()
    except (psycopg2.DatabaseError,Exception) as error:
        print (error)

# entering user name, phone ,etc  from console
name = input("Input name :")
phone_num = input("Input phone number :")  
city = input("Input city :")
address = input("Input address :")
if __name__ == '__main__' :
    insert_conacts(tuple((name, phone_num)))
    insert_contacts_location(tuple((name, city, address)))