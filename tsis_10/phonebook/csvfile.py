import psycopg2
import csv
from config import load_config
from connect import connect

def insert_conacts():
    config = load_config()
    filename = "contacts.csv"
    with connect(config) as conn:
        with conn.cursor() as cur:
            with open(filename,"r") as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    name = row[0]
                    phone_num = row[1]
                    cur.execute("""
                                INSERT INTO contacts (name,phone_number)
                                VALUES ('{}','{}')
                                """.format(name,phone_num))
                    conn.commit()

def insert_conacts_location():
    config = load_config()
    filename = "contacts.csv"
    with connect(config) as conn:
        with conn.cursor() as cur:
            with open(filename,"r") as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    name = row[0]
                    city = row[2]
                    address = row[3]
                    cur.execute("""
                                INSERT INTO contacts_location (name,city,address)
                                VALUES ('{}','{}','{}')
                                """.format(name,city,address))
                    conn.commit()

if __name__ == "__main__" :
    insert_conacts()
    insert_conacts_location()