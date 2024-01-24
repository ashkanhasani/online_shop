import uuid
from users import User


class Customer(User):
    def __init__(self, first_name, last_name, phone, username, password):
        super().__init__(first_name, last_name, phone)
        self.username = username
        self.password = password
        self.user_id = uuid.uuid4()
