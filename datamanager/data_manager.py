
import json
import sys
from regex.regextool import RegexTool
class DataManager(RegexTool):


    def __init__(self,file_path):

        self.file_path= file_path



    def get_data(self):
        """
            This method is created to return all data from json file
        """
        with open(self.file_path, 'r') as json_data:
            data = json.load(json_data)

        return data

    def get_main_keys(self):
        """
            This method is created to return keys of data
            *Note : Not very useful
        """
        data = self.get_data()[0]

        return data.keys()

    def get_emails(self):
        """
            This method is created to return emails of users as a list
        """
        data = self.get_data()
        emails = [email.get('email',None) for email in data]

        return emails

    def get_profiles(self):
        """
            This method is created to return profile informations of user as a list
        """
        data = self.get_data()

        profiles = [profile.get('profile',None) for profile in data]

        return profiles

    def get_profile_by_index(self,index):
        """
            This method returns a single user's profile by index
        """
        data = self.get_data()

        return data[index].get('profile',None)

    def get_usernames(self):
        """
            This method is created to return all user's usernames as a list
        """
        data = self.get_data()

        usernames = [username.get('username',None) for username in data]

        return usernames

    def get_email(self,data):

        return data.get('email')

    def get_email_username(self,email):

        return email.split("@")[0]

    def get_username(self,data):

        return data.get('username')

    def get_name(self,data):
        return data.get('profile').get('name')

    def get_country(self,data):
        return data.get('profile').get('address').split(",")[-1]

    def get_parsed_date(self,data):

        parsed_date = data.get('profile').get('dob').split("-")
        parsed_date_dict = {'year':parsed_date[0],'month':parsed_date[1],'day':parsed_date[2]}

        return parsed_date_dict

    def get_emails_username(self):
        """
            This method is created to return email's usernames as a list


            email : example@mail.com
            email_username : example
        """
        data = self.get_data()

        emails_username = [single_data.get('email',None).split("@")[0] for single_data in data]

        return emails_username

    def required_data(self,data):
            """
                This method returns only requested data
            """
            email = self.get_email(data)
            username = self.get_username(data)
            name = self.get_name(data)
            country = self.get_country(data)
            email = self.get_email(data)
            email_username = self.get_email_username(email)
            email_username_similarity = self.compare_email_username(email_username,username)
            username_name_similarity = self.compare_username_name(username,name)
            parsed_date = self.get_parsed_date(data)
            boy = parsed_date.get('year')
            bom = parsed_date.get('month')
            bod = parsed_date.get('day')


            return (email,username,name,email_username_similarity,username_name_similarity,boy,bom,bod,country,)
