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
                "name": "groceries",
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
            2, final_users-initial_users, 'User not created')

    def test_add_shoppinglist(self):
            """Test for adding  shoppinglist functionality"""
            self.test_store.add_user('mash', 'mash@mash1.com', 'mash_pass')
            test_user = self.test_store.get_single_user(1)
            initial_shoppinglists = len(test_user['shopping_lists'])
            self.test_store.add_shoppinglist(1, 'groceries')
            final_shoppinglists = len(test_user['shopping_lists'])
            self.assertEquals(
                1, final_shoppinglists-initial_shoppinglists,
                'shoppinglist item not created properly')

    def test_get_shoppinglist(self):
        """Test whether we can get a single shoppinglist"""
        self.test_store.add_user('mash', 'mash@mash2.com', 'mash_pass')
        self.test_store.add_shoppinglist(3, "hardware")
        test_item = self.test_store.get_shoppinglist(3, 1)
        self.assertEquals(
            test_item,
            {
                "id": 1,
                "name": "hardware",
                "items": [],
            }, "Item not found"
        )

    def test_delete_shoppinglist(self):
        """Test to see whether we can delete a shoppinglist"""
        self.test_store.add_user('mash', 'mash@mash3.com', 'mash_pass')
        self.test_store.add_shoppinglist(1, "Utensils")
        test_user = self.test_store.get_single_user(1)
        initial_shoppinglists = len(test_user['shopping_lists'])
        self.test_store.remove_shoppinglist(1, 1)
        final_shoppinglists = len(test_user['shopping_lists'])
        self.assertEquals(
            1,
            initial_shoppinglists-final_shoppinglists,
            'Items not removed'
        )
