import psycopg2
from connect import connect
from config import load_config

def get_contact():
    command = """ 
                SELECT name, phone_number 
                FROM contacts 
                ORDER BY name
            """
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                rows = cur.fetchall()

                print("Number of Contacts: ", cur.rowcount)
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_contact_location():
    command = """ 
                SELECT name, city, address 
                FROM contacts_location
                ORDER BY name
            """
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                rows = cur.fetchall()

                print("Number of Contacts: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    get_contact()
    get_contact_location()