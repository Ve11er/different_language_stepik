from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30.0)
    add_to_cart = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert add_to_cart != None, "Add to Cart button is not found"