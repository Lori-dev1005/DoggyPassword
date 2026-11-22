import html
import re
import string
import unittest

from app import app
from password_generator import PasswordGenerator
from password_validator import PasswordValidator


class PasswordGeneratorTests(unittest.TestCase):
    def test_generated_password_has_requested_length_and_required_characters(self):
        password = PasswordGenerator(12).generate()

        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertTrue(PasswordValidator(password).is_valid())

    def test_rejects_lengths_outside_supported_range(self):
        for length in (9, 51, True, "12"):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    PasswordGenerator(length)


class PasswordValidatorTests(unittest.TestCase):
    def test_rejects_passwords_missing_required_character_types(self):
        passwords = (
            "AB1!BCDEFG",
            "ab1!bcdefg",
            "Abc!defghi",
            "Ab1abcdefg",
            "Aa1!abcde",
        )

        for password in passwords:
            with self.subTest(password=password):
                self.assertFalse(PasswordValidator(password).is_valid())

    def test_rejects_non_string_password(self):
        with self.assertRaises(TypeError):
            PasswordValidator(None)


class PasswordAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_form_generates_and_validates_password(self):
        response = self.client.post("/", data={"length": "17"})
        page = response.get_data(as_text=True)
        match = re.search(r"<strong>(.*?)</strong>", page)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(match)
        self.assertEqual(len(html.unescape(match.group(1))), 17)
        self.assertIn("Password validation: passed", page)

    def test_form_rejects_out_of_range_length(self):
        response = self.client.post("/", data={"length": "4"})

        self.assertIn(b"Choose a length from 10 to 50.", response.data)


if __name__ == "__main__":
    unittest.main()
