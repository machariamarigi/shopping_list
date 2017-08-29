"""Module for testing application's models"""

from unittest import TestCase

from app.models import User


class TestUserModel(TestCase):
    """Class containing tests for a user"""

    def setUp(self):
        self.user_instance = User('mash', 'mash@mash.com', 'mash_pass')

    def test_user_get_details(self):
        """Method to test if user instantiates correctly"""
        self.assertEqual(self.user_instance.get_details(), {
            "username": "mash",
            "email": "mash@mash.com",
            "password": "mash_pass"
        })
