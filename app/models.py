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
