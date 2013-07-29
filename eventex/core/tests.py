"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_get(self):
        'GET / must return status code 200'
        response = self.client.get('/')
        self.assertEqual(200,response.status.code)

    def test_template(self):
    	'Home must use template index.html'
        self.assertTemplateUsed(response, 'index.html')
