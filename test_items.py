from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


try:
    def test_guest_should_see_button_france_lang_website(browser):
        browser.get(link)
        time.sleep(2)
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket") is not None, "button is not found"
    
except NoSuchElementException:
    print("button is not found")
