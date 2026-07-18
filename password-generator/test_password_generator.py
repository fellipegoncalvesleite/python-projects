import string
import unittest
from contextlib import redirect_stdout
from io import StringIO

from password_generator import SYMBOLS, generate_password, main


class PasswordGeneratorTests(unittest.TestCase):
    def test_default_password_has_expected_length_and_character_types(self):
        password = generate_password()

        self.assertEqual(len(password), 16)
        self.assertTrue(any(character in string.ascii_uppercase for character in password))
        self.assertTrue(any(character in string.ascii_lowercase for character in password))
        self.assertTrue(any(character in string.digits for character in password))
        self.assertTrue(any(character in SYMBOLS for character in password))

    def test_disabled_character_types_are_excluded(self):
        password = generate_password(
            24, uppercase=False, digits=False, symbols=False
        )

        self.assertTrue(set(password).issubset(set(string.ascii_lowercase)))

    def test_rejects_length_too_short_for_enabled_types(self):
        with self.assertRaisesRegex(ValueError, "Length must be at least 4"):
            generate_password(3)

    def test_rejects_disabling_every_character_type(self):
        with self.assertRaisesRegex(ValueError, "Enable at least one"):
            generate_password(
                uppercase=False, lowercase=False, digits=False, symbols=False
            )

    def test_cli_generates_requested_number_and_length(self):
        output = StringIO()
        with redirect_stdout(output):
            exit_code = main(["--length", "20", "--count", "3"])

        passwords = output.getvalue().splitlines()
        self.assertEqual(exit_code, 0)
        self.assertEqual(len(passwords), 3)
        self.assertTrue(all(len(password) == 20 for password in passwords))


if __name__ == "__main__":
    unittest.main()
