import pytest
from utils.browser_setup import init_browser

@pytest.fixture
def browser():
    driver = init_browser()
    yield driver
    driver.quit()
