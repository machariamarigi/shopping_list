"""
    Module for the application's User, ShoppingList, ShoppingItems and Storage
    models
"""


class User():
    """Class modeling a real world user"""

    def __init__(self, username, email, password):
        """Constructor for user object"""
        self.username = username
        self.email = email
        self.password = password
        self.shopping_list = []

        self.details = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'shopping_lists': self.shopping_list
        }

    def get_details(self):
        return self.details


class ShoppingList(object):
    """Class modeling a shopping list with CRUD operations"""

    def __init__(self, name, items=None):
        """Create shoppinglist item"""
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items

        self.details = {
            'name': self.name,
            'items': self.items
        }

    def get_details(self):
        """Method to return the shoppinglist details"""
        return self.details


class ShoppingItem(object):
    """Class modeling a shopping items with CRUD operations"""

    def __init__(self, name, quantity, bought=False):
        self.name = name
        self.quantity = quantity
        self.bought = bought

        self.details = {
            'name': self.name,
            'quantity': self.quantity,
            'bought': self.bought
        }

    def get_details(self):
        """Method to return the shoppingitems details"""
        return self.details


class Storage():
    """Class will handle volatile storage of the application's data"""

    users = [{
        'email': None,
        'password': None,
        'username': None,
        'shopping_list': None,
        'id': 0
    }]

    current_user = {}

    def add_user(self, username, email, password):
        """Method to register users to the application"""

        new_user = User(username, email, password)
        new_user_details = new_user.get_details()
        for user in self.users:
            if new_user_details['email'] == user['email']:
                break
                return False
            else:
                new_user_details['id'] = len(self.users)
                self.users.append(new_user_details)

    def get_single_user(self, id):
        """Method to return a single user base on a given id"""
        for user in self.users:
            if user['id'] == id:
                return user

    def add_shoppinglist(self, user_id, name):
        """
            Method to add shoppinglists to a user given the id of the
            user
        """
        new_shoppinglist = ShoppingList(name)
        new_shoppinglist_details = new_shoppinglist.get_details()
        user = self.get_single_user(user_id)
        new_shoppinglist_details['id'] = len(user['shopping_lists']) + 1
        for item in user['shopping_lists']:
            if new_shoppinglist_details['id'] == item['id']:
                new_shoppinglist_details['id'] = new_shoppinglist_details['id'] + 1
        user['shopping_lists'].append(new_shoppinglist_details)

    def get_shoppinglist(self, user_id, item_id):
        """
            Method to return a single user item based on the user 
            item's id and its user's id
        """
        single_user = self.get_single_user(user_id)
        for item in single_user['shopping_lists']:
            if item['id'] == item_id:
                return item

    def remove_shoppinglist(self, user_id, item_id):
        """
            Method to delete a user item based on its id and its
            user's id
        """
        single_user = self.get_single_user(user_id)
        for item in single_user['shopping_lists']:
            if item['id'] == int(item_id):
                single_user['shopping_lists'].remove(item)
