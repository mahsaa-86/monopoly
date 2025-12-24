from typing import  Optional

class User:
    def __init__(self,username,password_hash):
        self.username = username
        self.password = password_hash

    def __str__(self) -> str:
        return self.username
    def __repr__(self):
        return f"<User {self.username}>"