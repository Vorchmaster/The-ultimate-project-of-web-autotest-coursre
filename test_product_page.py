from pages.product_page import ProductPage

def test_guest_should_see_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()

def test_guest_can_summon_and_accept_alert(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.summon_alert()
    page.solve_quiz_and_get_code()
