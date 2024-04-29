import psycopg2
from connect import connect
from config import load_config

def delete_contact(name):
    command = """
            DELETE FROM contacts
            WHERE name = %s 
                """
    try:
        config = load_config()
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(command,(name,))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



name = input("Input name to delete from both tables :")
if __name__ == "__main__" :
    delete_contact(name)