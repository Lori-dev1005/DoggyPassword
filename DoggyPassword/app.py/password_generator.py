import secrets
import string


class PasswordGenerator:
    MIN_LENGTH = 10
    MAX_LENGTH = 50

    def __init__(self, length: int = 12) -> None:
        if (
            not isinstance(length, int)
            or isinstance(length, bool)
            or not self.MIN_LENGTH <= length <= self.MAX_LENGTH
        ):
            raise ValueError(
                f"Password length must be between {self.MIN_LENGTH} and {self.MAX_LENGTH}."
            )
        self.length = length

    def generate(self) -> str:
        characters = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation),
        ]
        alphabet = string.ascii_letters + string.digits + string.punctuation
        characters.extend(
            secrets.choice(alphabet) for _ in range(self.length - len(characters))
        )
        secrets.SystemRandom().shuffle(characters)
        return "".join(characters)