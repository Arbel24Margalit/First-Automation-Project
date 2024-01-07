import time

from AutomationProject.Tests.selenium_base import SeleniumBase
from AutomationProject.pages.CategoryPage import CategoryPage
from AutomationProject.pages.MainZapPage import MainZapPage


class TVByCategory:
    base = SeleniumBase()
    driver = base.selenium_init('https://zap.co.il/')
    main_page = MainZapPage(driver)
    main_page.all_category()
    category_page = CategoryPage(driver)
    category_page.select_tv_category()
    time.sleep(3)
    base.selenium_end(driver)
