from typing import Optional


class User:
    def __init__(
        self, email, name, last_name, birth, permission, id: Optional[int] = None
    ):
        self.id = id
        self.email = email
        self.name = name
        self.last_name = last_name
        self.birth = birth
        self.permission = permission
