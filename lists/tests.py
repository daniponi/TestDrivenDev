from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        #Django uses internally to resolve URLs resolve
        found = resolve('/')
        self.assertEqual(found.func, home_page)
