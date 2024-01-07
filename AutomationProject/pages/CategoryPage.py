from selenium.webdriver.common.by import By


class CategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def select_tv_category(self):

        tv_category_link = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="טלויזיות"]')
        print(f'Category: {tv_category_link.text}')
        tv_category_link.click()
