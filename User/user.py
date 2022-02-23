"""
VALIDATIONS for users

Login
Can only contain letters (a-z), numbers (0-9) and the underscore (_)
Length must be between 1 and 20 characters

Email
Must be a valid email address

Password
Length must be between 5 and 120 characters
"""


class User:

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    @staticmethod
    def default_users():
        login = 'DefaultUser'
        password = 'qwertyuio'
        email = 'default@gmail.com'
        return User(login, password, email)