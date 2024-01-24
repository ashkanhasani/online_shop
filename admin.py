import uuid
from users import User


class Admin(User):
    username_list = []

    def __init__(self, first_name, last_name, phone, username, password, position):
        super().__init__(first_name, last_name, phone)
        self.username = username
        self.password = password
        self.position = position
        self.user_id = uuid.uuid4()
