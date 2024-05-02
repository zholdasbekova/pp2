import psycopg2
from connect import connect
from config import load_config

def create_tables ():
    # creating tables commands
    commands = (
        """
        CREATE TABLE contacts (
            name VARCHAR (50) PRIMARY KEY,
            phone_number VARCHAR (20) NOT NULL
        );
        """,
        """
        CREATE TABLE contacts_location (
            name VARCHAR (50) PRIMARY KEY,
            city VARCHAR(100),
            address VARCHAR(255),
            FOREIGN KEY (name) REFERENCES contacts (name)
        );
        """
    )
    try:
        config = load_config()
        with connect(config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ =="__main__" :
    create_tables()