from sqlite3 import Error
from datetime import date
import sqlite3


class DatabaseManager:


    def get_db_model(self):

        return Database()



class Database:
    db_name = "dataregex.db"
    def __init__(self,db_path=None):

        self.db_path = db_path

    objects = DatabaseManager()
    @classmethod
    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            #print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
    @classmethod
    def open_connection(self):
        conn = None
        conn = sqlite3.connect(self.db_name)

        return conn

    @classmethod
    def generate_table_name(self):
            """
                bugünün tarihine göre tablo adı oluşturdan sınıf metodu

                *join tek bir argüman kabul ettiği için tarih değerleri tuple
                olarak ve stringe çevrilerek gönderildi
            """
            current_day = date.today()
            merged_date = "".join((str(current_day.year),str(current_day.month),str(current_day.day)))

            return f"data_{merged_date}"
    @classmethod
    def create_table(self,table_name):


        conn = self.open_connection()
        im = conn.cursor()

        query = f"CREATE TABLE IF NOT EXISTS {table_name} (email,username,full_name,emailuserlk,usernamelk,birth_year,birth_month,birth_day,country,ap)"

        im.execute(query)
        conn.commit()

    @classmethod
    def insert_data(self,data):
            table_name = self.generate_table_name()
            conn = self.open_connection()
            im = conn.cursor()
            query = f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?,?,?)"

            im.execute(query,data)
            conn.commit()
