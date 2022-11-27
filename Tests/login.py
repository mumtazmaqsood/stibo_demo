from selenium import webdriver
import unittest
import time
import HtmlTestRunner

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from Pages.contact_us import ContactUs

class LoginTest(unittest.TestCase):
    driver = None

#setupclass method run once, thats why website open once and
    @classmethod
    def setUpClass(cls):
        # path = "C:\\python310\\libs\\chromedriver.exe"
        # cls.driver = webdriver.Chrome(path)
        #If chrome browser is not opened then comment the below line and un-comment the upper 2 lines
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get(" https://www.stibosystems.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)

    # Home Page
    """
    1- Open the website
    2- Accepting Cookies
    3- Click on the Demo Button 
    """
    def test_a_home_page(self):
        self.login = HomePage(self.driver)
        self.login.enter_coke_btn()
        self.login.click_on_demo_btn()
        time.sleep(2)

    # Contact Us page
    """
    2.1-Verifying Text: 'Book a free product demo today.' present on the page or not
    2.2- Verifying error msg:'Please complete this required field.': is present or not
    2.3- Click on Logo
    2.4- Verifying- After clicking on logo > Page redirected to home page:https://www.stibosystems.com/
    """
    def test_b_contact_us_page(self):
        self.contact_us = ContactUs(self.driver)
        self.contact_us.validate_text()
        self.contact_us.book_demo()
        self.contact_us.click_on_logo()
        self.contact_us.verify_home_page_url()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\MumtazMaqsood\\Desktop\\Technical Docs\\own learning\\stibo_demo\\Reports"))
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))


