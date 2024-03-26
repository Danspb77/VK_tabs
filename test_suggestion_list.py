import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def setup():

    webdriver_path = '/usr/local/bin/chromedriver'

    # Create a new Chrome service object
    chrome_service = ChromeService(webdriver_path)

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=chrome_service)

    print("Open browser")

    yield driver

    # Close the browser window
    driver.quit()

    print("Close browser")


def test_suggestion_list(setup):
    driver = setup

    # Navigate to Yandex's homepage
    driver.get("https://ya.ru/")

    # Find the search box using its id attribute value
    search_box = driver.find_element("id", "text")

    # Type the search query
    search_box.send_keys("Selenium")

    # time.sleep(3)

    try:
        # Get the text of the first suggestion
        first_suggestion = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.mini-suggest__item.mini-suggest__item_type_fulltext.mini-suggest__item_enriched_yes')))

        # Get the text content of the first suggestion
        first_suggestion_text = first_suggestion.text

    except:
        print("Element with CSS selector .mini-suggest__item.mini-suggest__item_type_fulltext.mini-suggest__item_enriched_yes not found or visible within 10 seconds")

    # Define the expected first suggestion
    expected_suggestion = "selenium"

    # Check if the first suggestion matches the expected suggestion
    assert first_suggestion_text.lower(
    ) == expected_suggestion, f"First suggestion: {first_suggestion_text} does not match the expected value {expected_suggestion}"
