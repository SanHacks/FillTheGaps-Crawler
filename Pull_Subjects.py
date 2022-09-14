from selenium import webdriver
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# 3. Send get() Request and fetch the webpage contents
driver.get("https://www.game.co.za/Groceries/Pantry/l/c/G2064")
#browser = start_chrome(url, headless=True)

print(driver.title)