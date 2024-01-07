from selenium.webdriver.common.by import By


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def results_titles(self):
        results_titles = self.driver.find_elements(By.CLASS_NAME, 'ModelTitle')
        i = 1
        for result_title in results_titles:
            print(f'{i}. {result_title.text}')
            i += 1

    def specific_result_info(self, number):
        specific_result = self.driver.find_element(By.CSS_SELECTOR, f"[data-index = '{number}']")
        specific_result_title = specific_result.find_element(By.CLASS_NAME, 'ModelTitle')
        specific_result_price = specific_result.find_element(By.CSS_SELECTOR, 'span')
        print(f'Title: {specific_result_title.text}, Price: {specific_result_price.text}')

    def specific_result_title(self, number):
        specific_result = self.driver.find_element(By.CSS_SELECTOR, f"[data-index = '{number}']")
        specific_result_title = specific_result.find_element(By.CLASS_NAME, 'ModelTitle')
        print(f'title: {specific_result_title.text}')

    def specific_result_price(self, number):
        specific_result = self.driver.find_element(By.CSS_SELECTOR, f"[data-index = '{number}']")
        result_price = specific_result.find_element(By.CSS_SELECTOR, 'span')
        print(result_price.text)

    def select_result(self, number):
        specific_result = self.driver.find_element(By.CSS_SELECTOR, f"[data-index = '{number}']")
        specific_result_title = specific_result.find_element(By.CLASS_NAME, 'ModelTitle')
        result_link = specific_result.find_element(By.LINK_TEXT, f'{specific_result_title.text}')
        result_link.click()
