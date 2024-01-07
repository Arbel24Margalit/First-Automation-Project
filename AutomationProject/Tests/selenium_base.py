from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class SeleniumBase:
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.driver = driver

    def selenium_init(self, url):
        print(f'test start')
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium_end(self, driver):
        driver.quit()
        print(f'Test End')
