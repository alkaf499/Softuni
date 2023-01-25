import unittest

class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
        self.assertEqual(str(ve.exception), "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')

if __name__ == "__main__":
    unittest.main()
