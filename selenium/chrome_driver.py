import time
from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL_TEST = "http://www.python.org"
URL_TEST1 = "http://www.google.com"
URL_TEST3 = "https://pythonbasics.org/selenium-get-html/"
URL_TEST4 = "https://olx.pt/"
URL_TEST5 = "https://webtech87.pt/"



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
'''


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

driver.get(URL_TEST4)
print(URL_TEST4 ,' Opened')


button_accept_pp = driver.find_element('id', 'onetrust-accept-btn-handler')
button_accept_pp.click()
print(f'Element button {button_accept_pp.text} finded and clicked')

print('===============find elements==================='.upper())

driver.get(URL_TEST5)
a = driver.find_elements("class name", "nav-links")[0].find_elements("tag name","a")

print(len(a))
for obj in a:
    print(obj.accessible_name)
    obj.click()
    sleep(2)

'''

driver.get(URL_TEST4)
button_coockies_accept = driver.find_element('xpath', "//button[@id='onetrust-accept-btn-handler']")
print(button_coockies_accept)
button_coockies_accept.click()
sleep(3)
login_link = driver.find_element('xpath', "//a[@data-cy='myolx-link']").click()
sleep(2)
input_fields = driver.find_elements("tag name", "input")
print(len(input_fields))
input_fields[0].send_keys("Pupsik")
input_fields[1].send_keys("Pupsik")


username_field = driver.find_element("xpath", "//input[@id='username']")
password_field = driver.find_element("xpath", "//input[@id='password']")
#username_field.send_keys("borisisac@gmail.com")
#password_field.send_keys("spawnkid1")
sleep(3)


#<a href="http://www.olx.pt/account/?ref[0][params][url]=http%3A%2F%2Fwww.olx.pt%2F&amp;ref[0][action]=redirector&amp;ref[0][method]=index" data-cy="myolx-link" data-testid="myolx-link" class="css-12l1k7f"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" class="css-12my6f1"><path fill="currentColor" fill-rule="evenodd" d="M12 12c4.963 0 9 4.038 9 9l-1 1H4l-1-1c0-4.962 4.037-9 9-9zm0 2c-3.52 0-6.442 2.613-6.929 6H18.93c-.487-3.387-3.409-6-6.93-6zm0-12c2.481 0 4.5 2.019 4.5 4.5 0 2.482-2.019 4.5-4.5 4.5a4.505 4.505 0 0 1-4.5-4.5C7.5 4.019 9.519 2 12 2zm0 2a2.503 2.503 0 0 0-2.5 2.5C9.5 7.878 10.621 9 12 9s2.5-1.122 2.5-2.5S13.379 4 12 4z"></path></svg>A tua conta<div class="css-oedrow"></div></a>



