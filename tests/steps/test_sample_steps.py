from pytest_bdd import scenarios, given, when, then  # type: ignore
from pages import SamplePage
import time

scenarios('../features/sample.feature')


@given('a thing is true', target_fixture='page')
def page(driver):
    driver.get('https://www.duckduckgo.com/')
    time.sleep(5)


@when('I do "<x>" thing')
def sampleAction(driver, x):
    page = SamplePage(driver)
    page.elements.sample_element().send_keys(x)
    time.sleep(5)


@then('a thing should happen')
def sampleResult():
    assert True
