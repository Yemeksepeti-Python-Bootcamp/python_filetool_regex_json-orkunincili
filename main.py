
from os.path import dirname
from sys import path
from geopy.geocoders import Nominatim
from database.database import Database
from datamanager.data_manager import DataManager
from regex.regextool import RegexTool
from model.models import User
import os
from pathlib import Path
path.insert( 0 , dirname( __file__ ) )

def main():
    Database.create_connection()
    Database.create_table(Database.generate_table_name())
    datamanager = DataManager(Path(os.getcwd()) / 'dataregex.json')

    for data in datamanager.get_data():
        required_data = datamanager.required_data(data)

        user = User(required_data)
        user.save()
    






if __name__ == "__main__":
    main()
