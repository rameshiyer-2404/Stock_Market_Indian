from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


SITE_URL = "https://www.nseindia.com/get-quotes/equity?symbol=RECLTD&series=EQ"
#Setting up the webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(SITE_URL)

#waiting for the page to load
time.sleep(10)

last_price = driver.find_element(By.CSS_SELECTOR, "span#quoteLtp").text
# print(last_price)

row_head = driver.find_element(By.CSS_SELECTOR,value="thead tr")
columns_head = row_head.find_elements(By.TAG_NAME,"th")
head_list = [column.text for column in columns_head]
# print(head_list)


row = driver.find_element(By.CSS_SELECTOR,value="tbody tr")
columns = row.find_elements(By.TAG_NAME,"td")
price_list = [column.text for column in columns]
# print(price_list)

keys = head_list
values = price_list

stock_price_dict = dict(zip(keys,values))
# print(stock_price_dict)


volume = driver.find_element(By.CSS_SELECTOR, value="table.card-table tbody td.text-end span#orderBookTradeVol.bold").text
# print(volume)

stock_data = {
    "Stock Name" : "RECLTD",
    "LTP" : last_price,
    "Volume": volume
}

stock_data.update(stock_price_dict)
# print(stock_data)

df = pd.DataFrame([stock_data])
df.to_csv('rec_stock_data.csv',index=False)

driver.quit()