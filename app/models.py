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
                new_shoppinglist_details['id'] = new_shoppinglist_details['id']
                + 1
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

    def add_shoppingitems(self, user_id, shoppinglist_id, name, quantity):
        """
            Method to add shopping items to a shopping list
        """
        new_shoppingitem = ShoppingItem(name, quantity)
        new_shoppingitem_details = new_shoppingitem.get_details()
        user = self.get_single_user(user_id)
        for shopinglist in user['shopping_lists']:
            if shopinglist['id'] == int(shoppinglist_id):
                curr_shopinglist = shopinglist
                new_shoppingitem_details['id'] = len(curr_shopinglist['items']) + 1
                for item in curr_shopinglist['items']:
                    if new_shoppingitem_details['id'] == item['id']:
                        new_shoppingitem_details['id'] = new_shoppingitem_details['id'] + 1
                curr_shopinglist['items'].append(new_shoppingitem_details)

    def get_shoppingitem(self, user_id, shoppinglist_id, item_id):
        """Method to get a single item from the shopping list"""
        shoppinglist = self.get_shoppinglist(user_id, shoppinglist_id)
        for item in shoppinglist['items']:
            if item['id'] == item_id:
                return item

    def remove_shoppingitem(self, user_id, shoppinglist_id, item_id):
        """Method to delete an item from the shoppinglist"""
        shoppinglist = self.get_shoppinglist(user_id, shoppinglist_id)
        for item in shoppinglist['items']:
            if item['id'] == int(item_id):
                shoppinglist['items'].remove(item)

    def buy_shoppingitem(self, user_id, shoppinglist_id, item_id):
        """Method to indicate bought items"""
        item = self.get_shoppingitem(user_id, shoppinglist_id, item_id)
        if item['bought']:
            item['bought'] = False
        elif not item['bought']:
            item['bought'] = True
