import string


class PasswordValidator:
    def __init__(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")
        self.password = password

    def is_valid(self) -> bool:
        return (
            len(self.password) >= 8
            and any(char.islower() for char in self.password)
            and any(char.isupper() for char in self.password)
            and any(char.isdigit() for char in self.password)
            and any(char in string.punctuation for char in self.password)
        )