""" Module to test the running the application """
from flask import url_for, abort
from flask_testing import TestCase

from .basetest import TestBase


class TestAppRun(TestBase):
    """Test the running of the application"""

    def test_index(self):
        """Test the loading of the landing_page"""
        response = self.client.get(url_for('landing_page.landing'))
        self.assert200(response)

    def test_404_not_found(self):
        """Method to test page not """
        response = self.client.get('/nonesense')
        self.assert404(response)

    def test_500_internal_server_error(self):
        """Method to test server errors"""
        @self.app.route('/500')
        def internal_server_error():
            """Raise server eeeor"""
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)

    def test_login_page_without_auth(self):
        """Test the loading of login page"""
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_register_page_without_auth(self):
        """Test the loading of signup page"""
        response = self.client.get(url_for('auth.register'))
        self.assert200(response)

    def test_logout_view(self):
        """Test logout link """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login')
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
