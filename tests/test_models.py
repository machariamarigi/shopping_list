"""Module for testing application's models"""

from unittest import TestCase

from app.models import User, Storage, ShoppingList, ShoppingItem


class TestBase(TestCase):
    def setUp(self):
        self.test_store = Storage()
        self.test_store.add_user('test', 'test6@test.com', 'test')
        self.test_user = self.test_store.get_single_user(1)
        self.test_store.add_shoppinglist(1, 'Holiday Shopping')
        self.test_shoppinglist = self.test_store.get_shoppinglist(1, 1)


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
            6, final_users-initial_users, 'User not created')

    def test_add_shoppinglist(self):
            """Test for adding  shoppinglist functionality"""
            initial_shoppinglists = len(self.test_user['shopping_lists'])
            added = self.test_store.add_shoppinglist(1, 'groceries')
            final_shoppinglists = len(self.test_user['shopping_lists'])
            self.assertEquals(
                1, final_shoppinglists-initial_shoppinglists,
                'shoppinglist item not created properly')
            message = "Shopping list groceries Created"
            self.assertEquals(added, message)
            added2 = self.test_store.add_shoppinglist(1, 'groceries')
            message2 = "Shopping list groceries exits. Try editing it"
            self.assertEquals(added2, message2)

    def test_get_shoppinglist(self):
        """Test whether we can get a single shoppinglist"""
        test_item = self.test_store.get_shoppinglist(1, 1)
        self.assertEquals(
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
        self.assertEquals(
            1,
            initial_shoppinglists-final_shoppinglists,
            'Items not removed'
        )

    def test_add_shoppingitem(self):
        initial_shoppingItems = len(self.test_shoppinglist['items'])
        self.test_store.add_shoppingitems(1, 1, 'sun glasses', 1)
        final_shoppingItems = len(self.test_shoppinglist['items'])
        self.assertEquals(
            1,
            final_shoppingItems - initial_shoppingItems,
            'Shopping Item not created properly')

    def test_added_get_shoppingitem(self):
        test_item = self.test_store.get_shoppingitem(1, 1, 1)
        self.assertEquals(
            test_item,
            {
                "id": 1,
                "name": "sun glasses",
                "quantity": 1,
                'bought': False
            }
        )

    def test_delete_shoppingitem(self):
        initial_shoppingItems = len(self.test_shoppinglist['items'])
        self.test_store.remove_shoppingitem(1, 1, 1)
        final_shoppingItems = len(self.test_shoppinglist['items'])
        self.assertEquals(
            1,
            initial_shoppingItems-final_shoppingItems,
            'Items not removed'
        )

    def test_buy_shoppinlistitem(self):
        self.test_store.buy_shoppingitem(1, 1, 1)
        bought_item = self.test_store.get_shoppingitem(1, 1, 1)
        self.assertEquals(
            bought_item,
            {
                "id": 1,
                "name": "sun glasses",
                "quantity": 1,
                'bought': True
            }
        )
