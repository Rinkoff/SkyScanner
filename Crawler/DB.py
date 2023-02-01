import mysql.connector as connector

from read_db_config import read_db_config



class DB():
    def __init__(self):
        # Read config.ini file and take database information
        mysql_config=read_db_config("../config.ini","MySQL")

        # Check that database is connected
        try:
            self.connector=connector.connect(mysql_config)

        except connector.Error as error:
            print(error)


    def create_table(self):
        # Query for create new table in database
        mysql="""
            CREATE TABLE IF NOT EXISTS Scanner(
            id INT AUTO_INCREMENT PRIMARY KEY,
            Country VARCHAR(100) NOT NULL,
            City VARCHAR(100) NOT NULL,
            Price VARCHAR(10) NOT NULL,
            );
        """

        # Establish a cursor to interact with database
        with self.connector.cursor() as cursor:
            # Execute query in mysql variable and commit it
            cursor.execute(mysql)
            self.connector.commit()

    def remove_table(self):
        # Query for remove table in database
        mysql="DROP TABLE IF EXISTS Scanner;"

        # Establish a cursor to interact with database
        with self.connector.cursor() as cursor:
            # Execute query in mysql variable and commit it
            cursor.execute(mysql)
            self.connector.commit()


