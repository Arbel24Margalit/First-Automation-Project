from AutomationProject.Tests.selenium_base import SeleniumBase
from AutomationProject.pages.ItemPage import ItemPage
from AutomationProject.pages.MainZapPage import MainZapPage
from AutomationProject.pages.SearchResultsPage import SearchResultsPage


class IPhonePriceComparison:
    base = SeleniumBase()
    driver = base.selenium_init('https://zap.co.il/')
    main_page = MainZapPage(driver)
    main_page.search_for_text('IPhone 15 plus')

    search_results_page = SearchResultsPage(driver)
    search_results_page.results_titles()

    select_result = 2
    search_results_page.specific_result_info(select_result)
    # search_results_page.specific_result_title(select_result)
    # search_results_page.specific_result_price(select_result)
    search_results_page.select_result(select_result)

    item_page = ItemPage(driver)
    item_page.item_specs()
    item_page.compare_prices()

    base.selenium_end(driver)

