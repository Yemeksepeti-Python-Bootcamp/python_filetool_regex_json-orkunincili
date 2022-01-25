import re
import sys

class RegexTool:



    def mail_validation(self):
        """
         This method is created to check the email is valid or not
         :email:<str>
         :return:<boolean>
        """
        pattern = '$U/emshs/+)'

        is_valid = re.pattern(pattern,email)

        return is_valid


    def compare_email_username(self,email_username,username):

        if email_username[:3] == username[:3]:
            return "1"
        else:
            return "0"





    def normalize_name(self,name):
            """
                This method is created to normalize user's names

                :name:<str> :"Orkun Incili"

                :return:<str>:"orkunincili"
            """
            return "".join(name.split(" ")).lower()


    def compare_username_name(self,username,name):

        normalized_name = self.normalize_name(name)

        if username[:4] == normalized_name[:4]:
            return "1"
        else:
            return "0"

        #print(re.findall([name],username))
