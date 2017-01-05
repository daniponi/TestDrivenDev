from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #tells browser to wait a few seconds if it needs to.
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    # Dani has heard about a new web app for todo list and
    # she goes to their homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# She is invited to enter a to-do item right away

# she types "buy cats" into a textbox

# On hitting enter the page updates and it lists "1: buy cats"

# There is still a text box inviting her to add another item.

# She enters "buy cat toilet" and now both items are in the list

# Dani wonders if the site will remember her list. Then she
# notices that the site has generated an unique URL for header

# she visits this url and her list is still There

# she goes away from computer

if __name__== '__main__':
    unittest.main()
