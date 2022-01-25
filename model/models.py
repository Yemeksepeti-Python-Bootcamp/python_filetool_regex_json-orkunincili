
from database.database import Database

from regex.regextool import RegexTool
class User(RegexTool):

    def __init__(self,required_data,ap=1):

        self.required_data = required_data +(ap,)

    def save(self):
        
        Database.insert_data(self.required_data)
