
from os.path import dirname
from sys import path
import sys
from database.database import Database
from datamanager.data_manager import DataManager
from regex.regextool import RegexTool
from model.models import User
import os,collections
from pathlib import Path
path.insert( 0 , dirname( __file__ ) )

def main():


    opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "--file" in opts:

        pass
    elif "--db" in opts:
        pass


    else:
        pass
        #raise SystemExit(f"Usage: {sys.argv[0]} (--file | --db ) <arguments>...")

    Database.create_connection()
    Database.create_table(Database.generate_table_name())
    datamanager = DataManager(Path(os.getcwd()) / 'dataregex.json')

    for data in datamanager.get_data():
        required_data = datamanager.required_data(data)

        user = User(required_data)
        user.save()







if __name__ == "__main__":
    main()
