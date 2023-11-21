import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_add_to_basket()
    page.should_see_success_adding_msg()
    page.should_see_basket_price_msg()
    page.should_see_benefit_applying_msg()
    page.should_be_right_price_in_msg()
    page.should_be_right_product_name_msg()
    # time.sleep(10)
    # page.solve_quiz_and_get_code()
    time.sleep(2)
