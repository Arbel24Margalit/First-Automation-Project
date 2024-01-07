import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class MainZapPage:
    def __init__(self, driver):
        self.driver = driver
        self.search = self.driver.find_element(By.ID, "acSearch-input")
        print(f'into init')

    def search_for_text(self, text_for_search):
        print(f'Try to search {text_for_search}')
        self.search.click()
        self.search.send_keys(text_for_search)
        self.search.send_keys(Keys.ENTER)

    def all_category(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-cat='catall']").click()
