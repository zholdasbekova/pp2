import psycopg2
from connect import connect
from config import load_config

def update_contact(name,phone_number):
    command = """
            UPDATE contacts
            SET phone_number = %s
            WHERE name = %s 
                """
    try:
        config = load_config()
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(command,(phone_number,name))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_contact_location(name,city,address):
    upd_both = """
            UPDATE contacts_location
            SET city = %s, address=%s
            WHERE name = %s 
                """
    try:
        config = load_config()
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(upd_both,(city,address,name))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

name = input("Input name to update :")
phone_number = input("Input phone number for updating  :")
city = input("Input city  for updating  :")
address = input("Input phone address for updating  :")
if __name__ == "__main__" :
    update_contact(name, phone_number)
    update_contact_location(name, city, address)