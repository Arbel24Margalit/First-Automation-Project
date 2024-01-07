from selenium.webdriver.common.by import By


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

    def compare_prices(self):
        self.driver.implicitly_wait(5)
        print("Price Comparison: ")
        companies_table = self.driver.find_element(By.CLASS_NAME, 'compare-items-group')
        item_rows = companies_table.find_elements(By.CLASS_NAME, 'compare-item-row ')
        i = 1
        for item_row in item_rows:
            company_name = item_row.find_element(By.CLASS_NAME, 'model-page-site-name')
            company_price = item_row.find_element(By.CLASS_NAME, 'total')
            print(f'{i}. {company_name.text}: {company_price.text}')
            i += 1

    def item_specs(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CLASS_NAME, 'technical-details').click()
        print("Item's Specification:")
        specs = self.driver.find_element(By.CLASS_NAME, 'specificationContainer').find_elements(By.CLASS_NAME, 'item')
        for spec in specs:
            print(spec.text)
        tabs_manu = self.driver.find_element(By.CLASS_NAME, 'model-page-tabs-menu')
        tabs_manu.find_element(By.PARTIAL_LINK_TEXT, 'השוואת מחירים').click()
