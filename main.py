#Simple assignment
from time import sleep
from selenium import webdriver

#driver = Chrome(executable_path='C://WebDriver/bin/chromedriver')
#driver = Chrome()


options = webdriver.ChromeOptions()
options.add_argument("--incogito")
options.add_argument("--start-maximized")
#options.add_argument("--headless")

#Or use the context manager

driver = webdriver.Chrome("C://WebDriver/bin/chromedriver.exe", options = options)


    #your code inside this indent
driver.get("https://www.google.com")
print(driver.title)
sleep(5)
print(driver.title)
#driver.get("https://www.facebook.com")