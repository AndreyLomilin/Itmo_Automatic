import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


#
# def test_site_visit():
#
#     driver = webdriver.Chrome()
#     driver.get('https://www.saucedemo.com')
#
#     try:
#         user_name = driver.find_element(By.CSS_SELECTOR,  '#user-name')
#
#     except NoSuchElementException:
#         assert False
#     assert True
# time.sleep(4)



def test_search_img():

    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')

    try:
        driver.find_element(By.CSS_SELECTOR, '#app > header > a > img')
        driver.find_element(By.CSS_SELECTOR, '#user-name')


    except NoSuchElementException:
        assert False
    assert True

def test_clic():


    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')

    try:
        a = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div')


    except NoSuchElementException:
        assert False
    assert True
    a.click()
    time.sleep(3)
    assert driver.current_url == 'https://demoqa.com/elements'

# driver = webdriver.Chrome()





