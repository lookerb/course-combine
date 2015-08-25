import unittest
from paste.deploy.loadwsgi import appconfig
from pyramid import testing
from webtest import TestApp

from coursecombine import main


class ViewTests(unittest.TestCase):
    def setUp(self):
        from pyramid.registry import Registry
        registry = Registry('development.ini')
        print(registry.settings)
        self.config = testing.setUp(registry=registry)

    def tearDown(self):
        testing.tearDown()

    '''def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'CourseCombine')'''

    def test_login_view(self):
        from .views import login
        request = testing.DummyRequest()
        print(request.registry.settings)
        info = login(request)
        self.assertEqual(info['project'], 'CourseCombine')