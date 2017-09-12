"""Module comtaining common test cases"""
from flask_testing import TestCase

from app import create_app
from app.models import Storage


class TestBase(TestCase):
    """Base class test to be inheritted by other tests"""

    def create_app(self):
        """Create test instance of the application"""
        config_name = 'testing'
        app = create_app(config_name)
        app.config['SECRET_KEY'] = 'sekrit!'
        return app

    def setUp(self):
        self.test_store = Storage()
        self.test_store.add_user('test', 'test6@test.com', 'test')
        self.test_user = self.test_store.get_single_user(1)
        self.test_store.add_shoppinglist(1, 'Holiday Shopping')
        self.test_shoppinglist = self.test_store.get_shoppinglist(1, 1)

    def tearDown(self):
        self.test_store = None
        self.test_user = None
        self.test_shoppinglist = None
