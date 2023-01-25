class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, username):
        if not 5 < len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = username

    @password.setter
    def password(self, password):
        contains_uppercase = any(char.isupper() for char in password)
        contains_digit = any(char.isdigit() for char in password)
        if len(password) != 8 or not contains_uppercase or not contains_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = password

    def __str__(self):
        a = '"'
        return f"You have a profile with username: {a}{self.__username}{a} and password: {'*'*len(self.__password)}"

