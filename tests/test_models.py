"""Module for testing application's models"""

from unittest import TestCase

from app.models import User, ShoppingList, ShoppingItem
from .basetest import TestBase


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


class TestShoppingItemModel(TestCase):
    """ Class containing tests for ShoppingList Model """

    def setUp(self):
        self.shoppingitem_instance = ShoppingItem('carrots', 5)

    def tearDown(self):
        del self.shoppingitem_instance

    def test_shoppingitem_instance(self):
        """Test instantiation of shoppingitem objects"""
        self.assertEqual(
            self.shoppingitem_instance.get_details(),
            {
                "name": "carrots",
                "quantity": 5,
                "bought": False
            },
        )


class TestStorage(TestBase):
    """Class to test storage model"""

    def test_create_user(self):
        """Test if we can add new users into the system"""
        initial_users = len(self.test_store.users)
        self.test_store.add_user('test', 'test@test.com', 'test')
        final_users = len(self.test_store.users)
        self.assertEqual(
            1, final_users-initial_users, 'User not created')

    def test_add_shoppinglist(self):
        """Test for adding  shoppinglist functionality"""
        initial_shoppinglists = len(self.test_user['shopping_lists'])
        added = self.test_store.add_shoppinglist(1, 'groceries')
        final_shoppinglists = len(self.test_user['shopping_lists'])
        self.assertEqual(
            1, final_shoppinglists-initial_shoppinglists,
            'shoppinglist item not created properly')
        message = "Shopping list groceries Created"
        self.assertEqual(added, message)
        added2 = self.test_store.add_shoppinglist(1, 'groceries')
        message2 = "Shopping list groceries exits. Try editing it"
        self.assertEqual(added2, message2)

    def test_get_shoppinglist(self):
        """Test whether we can get a single shoppinglist"""
        test_item = self.test_store.get_shoppinglist(1, 1)
        self.assertEqual(
            test_item,
            {
                "id": 1,
                "name": "Holiday Shopping",
                "items": [],
            }, "Item not found"
        )

    def test_delete_shoppinglist(self):
        """Test to see whether we can delete a shoppinglist"""
        initial_shoppinglists = len(self.test_user['shopping_lists'])
        self.test_store.remove_shoppinglist(1, 2)
        final_shoppinglists = len(self.test_user['shopping_lists'])
        self.assertEqual(
            1,
            initial_shoppinglists-final_shoppinglists,
            'Items not removed'
        )

    def test_add_shoppingitem(self):
        """Test adding of items"""
        initial_shoppingitems = len(self.test_shoppinglist['items'])
        added = self.test_store.add_shoppingitems(1, 1, 'sun glasses', 1)
        final_shoppingitems = len(self.test_shoppinglist['items'])
        message = "sun glasses has been added"
        self.assertEqual(
            1,
            final_shoppingitems - initial_shoppingitems,
            'Shopping Item not created properly')
        self.assertEqual(added, message)
        added2 = self.test_store.add_shoppingitems(1, 1, 'sun glasses', 1)
        self.assertNotEqual(added2, message)

    def test_added_get_shoppingitem(self):
        """Test getting a single item from a shopping list"""
        test_item = self.test_store.get_shoppingitem(1, 1, 1)
        self.assertEqual(
            test_item,
            {
                "id": 1,
                "name": "sun glasses",
                "quantity": 1,
                'bought': False
            }
        )

    def test_delete_shoppingitem(self):
        """Test deleting shopping items"""
        initial_shoppingitems = len(self.test_shoppinglist['items'])
        self.test_store.remove_shoppingitem(1, 1, 1)
        final_shoppingitems = len(self.test_shoppinglist['items'])
        self.assertEqual(
            1,
            initial_shoppingitems-final_shoppingitems,
            'Items not removed'
        )

    def test_buy_shoppinlistitem(self):
        """Test indication of a bought item"""
        self.test_store.buy_shoppingitem(1, 1, 1)
        bought_item = self.test_store.get_shoppingitem(1, 1, 1)
        self.assertEqual(
            bought_item,
            {
                "id": 1,
                "name": "sun glasses",
                "quantity": 1,
                'bought': True
            }
        )
