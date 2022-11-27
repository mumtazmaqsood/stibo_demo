import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.utitlites import *


class ContactUs:

    def __init__(self, driver):
        self.driver = driver
        #text locotor
        self.text_css = "fieldset>div>h2"
        #logo locator
        self.logo_css = "a.sb-nav-logo"
        #form locators
        self.textarea_xpath = "//textarea[@name='message']"
        self.submit_link_xpath = "//input[@type='submit']"
        self.err_msg_xpath = "//label[contains(text(), 'Please complete this required field.')]"

    def validate_text(self):
        switch_window(self.driver,1)
        try:
            is_text = verify_text(self.driver,By.CSS_SELECTOR, self.text_css)
            assert is_text == "Book a free product demo today."
            print("<b>2.1-Verified Text: 'Book a free product demo today.' present on the page<b><br>")
        except:
            print("<b><font color='red'>2.1-Not Verified Text: 'Book a free product demo today.' is not present on the page<b></font><br>")

    def book_demo(self):
        switch_window(self.driver,1)
        try:
        #select country
            country_dropdown = self.driver.find_element_by_name('country')
            select = Select(country_dropdown)
            select.select_by_value("Denmark")
            time.sleep(2)
        #textarea
            textarea_ele = self.driver.find_element(By.XPATH, self.textarea_xpath)
            textarea_ele.send_keys("test message")
            time.sleep(2)
        #click on submit
            self.driver.find_element(By.XPATH, self.submit_link_xpath).click()
            time.sleep(5)
        #checking error msg under lastname
            err_msg = self.driver.find_elements(By.XPATH, self.err_msg_xpath)
            assert err_msg[1].text == "Please complete this required field."
            print(f"<b>2.2- Verified error msg:'{err_msg[1].text}': is present<b><br>")
        except:
            pass

    def click_on_logo(self):
        try:
            # switch_window(self.driver,0)
            # clicking on the logo
            self.driver.find_element(By.CSS_SELECTOR, self.logo_css).click()
            print("<b>2.3- Verified Click on Logo: True<b><br>")
        except:
            print("<b><font color='red'>2.3-Not Verified Click on Logo: False<b></font><br>")

    def verify_home_page_url(self):
        currentURL = self.driver.current_url
        try:
            assert currentURL == "https://www.stibosystems.com/"
            print(f"<b>2.4- Verified- After clicking on logo > Page redirected to home page:{currentURL}<br>")
            time.sleep(2)
        except:
            print(f"<b><font color='red'>2.4- Not Verified- After clicking on logo > Page not redirected to home page:{currentURL}</b></font><br>")











