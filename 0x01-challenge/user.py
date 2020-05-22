#!/usr/bin/python3
""" 
User class
"""
if __name__ == "__main__":

    class User():
        """ Documentation """

        def __init__(self, email):
            """ Documentation """
            if type(email) is not str:
                raise TypeError("email must be a string")
            else:
                self.__email = email

        @property
        def email(self):
            """ Documentation """
            return self.__email

        @email.setter
        def email(self, value):
            """ Documentation """
            if type(value) is not str:
                raise TypeError("email must be a string")
            self.__email = value


#if __name__ == "__main__":

    u = User("john@snow.com")
   # u.email = "john@snow.com"
    print(u.email)
