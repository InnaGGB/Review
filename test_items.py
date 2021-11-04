import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")