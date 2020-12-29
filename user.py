from datetime import datetime


class User:
    user_count = 0
    user_list = list()

    def __init__(self, first_name, last_name, username, password, age, email, phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = self.get_user_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.date = datetime.now()
        User.user_list.append(self)

    @staticmethod
    def get_user_id():
        User.user_count += 1
        return User.user_count

    @classmethod
    def create(cls, fname, lname, username, password, age, email, phone):
        result = {
            'first_name': fname,
            'last_name': lname,
            'username': username,
            'password': password,
            'age': age,
            'email': email,
            'phone_number': phone
        }
        return result

    @classmethod
    def __check_input(cls, *args):

        for item in args:
            if item is not None:
                return True
        return
