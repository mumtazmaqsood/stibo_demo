from selenium.webdriver.common.by import By
import time
from Locators.utitlites import window_store
from Locators.utitlites import switch_window


# window_store = []

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # cookies locators
        self.accept_cookie_btn = "//button[text()='Accept all']"
        #demo button
        self.demo_btn = "//a[contains(text(),'BOOK A DEMO')]"

    def enter_coke_btn(self):
        try:
            self.driver.find_element(By.XPATH, self.accept_cookie_btn).click()
            print(f"<b> 1.1- Website opened & Cookies accepted </b><br>")
        except:
            print(f"<b><font color='red'> 1.1- Website not opened & Cookies not accepted </b></font><br>")


    def click_on_demo_btn(self):
        '''
        This function is clicking on the Demo Button and
        capturing the windows id & store in public list window store
        :return: nothing return
        '''
        try:
            home_window_id = self.driver.window_handles[0]
            window_store.append(home_window_id)
            print(f"home_window_id:{home_window_id}<br>")
            self.driver.find_element(By.XPATH, self.demo_btn).click()
            print("<b>1.2-Verified 'Book Demo' button clicked </b></font><br>")

            contact_us_window_id = self.driver.window_handles[1]
            window_store.append(contact_us_window_id)
            print(f"contact_us_window_id:{contact_us_window_id}<br>")
        except:
            print(f"<b><font color='red'> Not Verified 'Book Demo' button clicked </b></font><br>")
