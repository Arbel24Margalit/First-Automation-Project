from webdriver_manager.chrome import ChromeDriverManager    #imports
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By

service=ChromeService(executable_path=ChromeDriverManager().install())  #driver setup
driver=webdriver.Chrome(service=service)
  
driver.get("https://www.zap.co.il/")    #opening the "Zap" website
driver.maximize_window()
print("Opend Website")

search_bar = driver.find_element(By.ID, "acSearch-input")   #searched item
search_bar.send_keys("Iphone 15 plus")
submit= driver.find_element(By.ID, "acSubmitSearch")
submit.click()
print("Searched For Item")

item = driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone 15 Plus")  #found item + redirected
item.click()

print("Companies: ")    #lists compmanies
i = 1
company_names = driver.find_elements(By.CLASS_NAME, "model-page-site-name")
for company_name in company_names:
    print(str(i) +". "+ company_name.text)
    i+= 1
    
i=1
print("Total Price: ")  #Total prices
total_prices = driver.find_elements(By.CLASS_NAME, "total")
for total_price in total_prices:
    print(str(i) +". "+ total_price.text)
    i+=1
    
driver.quit()