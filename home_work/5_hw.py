import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# def test_search():

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

    # try:
username_field = driver.find_element(By.ID, 'user-name')
password_field = driver.find_element(By.CSS_SELECTOR, '#passwor')
button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if username_field and password_field and button_submit:
        print('Элемент найден')
# else:
#         print('Элемент не найден')





    # except NoSuchElementException:
    #     assert False
    # assert True


