import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_cr
from selenium.webdriver.firefox.options import Options as Options_fr


# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", user_language)
# browser = webdriver.Firefox(firefox_profile=fp)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options_cr()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        options = Options_fr()
        options.profile = fp
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()