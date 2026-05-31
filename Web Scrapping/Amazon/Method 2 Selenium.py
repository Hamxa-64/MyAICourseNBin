from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import time

URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

service = Service("C:\\Users\\Hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(URL)
time.sleep(5)   

products = []

items = driver.find_elements(By.CSS_SELECTOR,"._Y29ud_bxcGridImage_mukPG._Y29ud_bxcGridHalign_3QrYc._Y29ud_bxcGridHalignCenter_YYl_I")


for item in items:
    try:
        product_url = item.get_attribute("href")

        img = item.find_element(By.CSS_SELECTOR,"._Y29ud_bxcGridImage_mukPG._Y29ud_bxcGridHalign_3QrYc._Y29ud_bxcGridHalignCenter_YYl_I")
        product_name = img.get_attribute("alt")
        product_img = img.get_attribute("src")

        products.append([product_name, product_url, product_img])

    except:
        continue

driver.quit()

# CSV write
with open("amazon_smart_home.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product Name", "Product URL", "Product Image"])
    writer.writerows(products)

print("✅ CSV file created successfully")
