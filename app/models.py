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
    """Class modeling a bucket list with CRUD operations"""

    def __init__(self, name, items=None):
        """Create bucketlist item"""
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
        """Method to return the bucketlist details"""
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
