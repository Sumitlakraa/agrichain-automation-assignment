from utils.browser_setup import get_driver
from pages.home_page import HomePage
from pages.result_page import ResultPage
import time

def test_output_for_valid_string():
    driver = get_driver()
    driver.get("https://agrichain.com/qa/input")

    home = HomePage(driver)
    home.enter_text("abcabcbb")               # test case 2 in excel sheet 
    home.click_submit()

    time.sleep(2)

    result = ResultPage(driver)
    output = result.get_output()

    assert output == "3"
    driver.quit()
