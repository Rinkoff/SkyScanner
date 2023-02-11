import mysql.connector as connector

from Crawler.read_db_config import read_db_config



class DB():
    def __init__(self):
        # Read config.ini file and take database information
        mysql_config=read_db_config("../config.ini","MySQL")

        # Check that database is connected
        try:
            self.connector=connector.connect(
                user=mysql_config['user'],
                password=mysql_config['password'],
                database=mysql_config['database'],
                host=mysql_config['host'],
                port=mysql_config['port']
            )

        except connector.Error as error:
            print(error)


    def create_table(self):
        # Query for create new table in database
        mysql="""
               CREATE TABLE IF NOT EXISTS scanner(
                id INT AUTO_INCREMENT PRIMARY KEY,
                Country VARCHAR(100) NOT NULL,
                City VARCHAR(100) NOT NULL,
                Price INT NOT NULL
                );
        """

        try:
            # Establish a cursor to interact with database
            with self.connector.cursor() as cursor:
                # Execute query in mysql variable and commit it
                cursor.execute(mysql)
                self.connector.commit()
        except:
            print("There is an issue with table creating")

    def remove_table(self):
        # Query for remove table in database
        mysql="DROP TABLE IF EXISTS scanner;"

        # Establish a cursor to interact with database
        with self.connector.cursor() as cursor:
            # Execute query in mysql variable and commit it
            cursor.execute(mysql)
            self.connector.commit()

    def insert_row(self,offer):
        mysql = """
                INSERT IGNORE INTO scanner
                (Country,City,Price)
                VALUES (%s, %s, CONCAT(%s, "€"))
            """
        try:
            #Insert one row in table
            with self.connector.cursor(prepared=True) as cursor:
                # Execute query in mysql and take data from external variable
                cursor.execute(mysql,offer)
                self.connector.commit()
        except:
            print("There is an issue with inserting rows in table")
    def intert_rows(self,offers):       #Looping all taken offers
        for offer in offers:
            self.insert_row(offer)


    def select_offers(self):                  ###Select whole table
        mysql = "SELECT id,Country,City,Price FROM scanner"

        with self.connector.cursor(prepared=True) as cursor:
            # Execute query in mysql variable,fetch all rows and return them
            cursor.execute(mysql)
            result=cursor.fetchall()
        return result







