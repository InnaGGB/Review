import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "No 'Add to basket' button"
