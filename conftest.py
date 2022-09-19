import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = chromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = firefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
