import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1800,1200')
    driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
