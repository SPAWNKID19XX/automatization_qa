import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL_TEST = "http://www.python.org"
URL_TEST1 = "http://www.google.com"
URL_TEST3 = "https://pythonbasics.org/selenium-get-html/"



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get(URL_TEST)
print(URL_TEST ,' Opened')

driver.get(URL_TEST1)
print(URL_TEST1 ,' Opened')

driver.back()
print(URL_TEST ,' Opened back')

driver.forward()
print(URL_TEST1 ,' Opened forward')

driver.get(URL_TEST3)
print(URL_TEST3 ,' Opened')

url3_title = driver.title
url3 = driver.current_url

print(url3_title)
print(url3)

print('Expected page. Checking if url and title is expected: ', url3 == URL_TEST3 and url3_title =='Selenium get HTML source in Python - Python Tutorial')





