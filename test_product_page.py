import time

from .pages.product_page import ProductPage
import pytest
@pytest.mark.quiz
def test_guest_can_add_product_applied_sales(browser):
    new_link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, new_link)
    page.open()
    page.should_be_added()

# @pytest.mark.parametrize('link', [str(i) for i in range(10)])
@pytest.mark.parametrize('link', [pytest.param("7", marks=pytest.mark.xfail) if i == 7 else str(i) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    new_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, new_link)
    page.open()
    page.should_be_added()
@pytest.mark.product
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added()
    page.should_not_be_success_msg()
    time.sleep(5)

@pytest.mark.product
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_msg()
    time.sleep(5)

@pytest.mark.product
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added()
    page.should_be_dissapeared_msg()
    time.sleep(5)

