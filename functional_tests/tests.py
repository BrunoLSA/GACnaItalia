from django.test import LiveServerTestCase
from selenium import webdriver
import unittest


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_can_select_a_point_and_drive_to_it(self):
        # Bruno has heard about a cool new website that shows
        # points in Italy with historical content of 1GAVCA
        # He goes to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and the header mention GAC na Itália
        self.assertIn('GAC na Itália', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('1ºGAVCA na Itália', header_text)
        #self.fail('Finish the test!')

        # He sees the Italy map

        # He sees some historical points on the map

        # He clicks on one point and it shows its
        # information: coordinates, title, description, picture(s)

        # He select another point and the information of the first point
        # is hidden

        # He choose to drive to the selected point

        # Satisfied, he goes back to sleep
