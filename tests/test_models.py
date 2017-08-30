"""Module for testing application's models"""

from unittest import TestCase

from app.models import User, Storage, ShoppingList


class TestUserModel(TestCase):
    """Class containing tests for a user"""

    def setUp(self):
        self.user_instance = User('mash', 'mash@mash.com', 'mash_pass')

    def test_user_get_details(self):
        """Method to test if user instantiates correctly"""
        self.assertEqual(self.user_instance.get_details(), {
            "username": "mash",
            "email": "mash@mash.com",
            "password": "mash_pass",
            "shopping_lists": []
        })


class TestShoppinglistModel(TestCase):
    """ Class containing tests for ShoppingList Model """

    def setUp(self):
        self.shoppinglist_instance = ShoppingList('groceries')

    def tearDown(self):
        del self.shoppinglist_instance

    def test_shoppinglist_instance(self):
        """Test instantiation of shoppinglist objects"""
        self.assertEqual(
            self.shoppinglist_instance.get_details(),
            {
                "name": "Holiday",
                "items": []
            },
        )


class TestStorage(TestCase):
    """Class to test storage model"""

    def setUp(self):
        self.test_store = Storage()

    def test_create_user(self):
        """Test if we can add new users into the system"""
        initial_users = len(self.test_store.users)
        self.test_store.add_user('test', 'test@test.com', 'test')
        final_users = len(self.test_store.users)
        self.assertEquals(
            1, final_users-initial_users, 'User not created')
