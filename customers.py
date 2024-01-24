import uuid
from users import User


class Customer(User):
    username_list = []

    def __init__(self, first_name, last_name, phone, username, password):
        super().__init__(first_name, last_name, phone)
        self.username = username
        self.password = password
        self.user_id = uuid.uuid4()
        Customer.username_list.append(self.username)

    @classmethod
    def signin(cls):
        fname = input(">>> Enter your first name: ")
        lname = input(">>> Enter your last name: ")
        phone = input(">>> Enter your phone number")
        while True:
            username = input(">>> Enter username: ")
            if username not in Customer.username_list:
                break
            else:
                print("your username is exist, Try another one")
        password = input(">>> Enter password")
        return cls(fname, lname, phone, username, password)
