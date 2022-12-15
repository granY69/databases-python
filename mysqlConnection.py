import mysql.connector

class DatabaseConnection():

    def __init__(self, database : str, host : str="localhost"):
        self.host = host
        self.database = database

    def connection(self):
        db = mysql.connector.connect(
            host=self.host,
            user="",#username
            port=3306,
            password="",#password
            charset='utf8mb4',
            database=self.database
        )

        if db.is_connected():
            print("You're connected to database!")
        else:
            print("Error Connection!")
        cursor = db.cursor(buffered=True)
        return cursor, db

    def close_connection(self, cursor, db):
        cursor.close()
        db.close()
        if not db.is_connected():
            print("MySQL connection is closed")
        else:
            print("Connection is not closed Successfully!")