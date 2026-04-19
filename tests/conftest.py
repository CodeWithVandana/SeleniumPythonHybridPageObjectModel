import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfigurations


import pytest

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name = "failed test case", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return  rep


@pytest.fixture
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser").lower()
    global  driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Invalid browser. Use: chrome, firefox, edge")

    driver.maximize_window()

    # ✅ IMPORTANT: stabilize tests
    driver.implicitly_wait(10)

    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)

    request.cls.driver = driver

    yield

    driver.quit()

