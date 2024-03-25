import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    # Set the path to your webdriver executable
    webdriver_path = '/usr/local/bin/chromedriver'  # Use the correct path

    # Specify the path to the ChromeDriver executable using the Service class
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

    # Wait for suggestions to appear
    # suggestion_list = driver.find_element(By.CLASS_NAME,'mini-suggest__item mini-suggest__item_type_fulltext mini-suggest__item_enriched_yes')

    suggestion_list = driver.find_element(By.XPATH,'/html/body/main/div[2]/form/div[2]/div/div/div[2]/div[1]')

    # Get the text of the first suggestion
    first_suggestion = suggestion_list.text

    # Define the expected first suggestion
    expected_suggestion = "Selenium WebDriver"

    # Check if the first suggestion matches the expected suggestion
    assert first_suggestion == expected_suggestion, "First suggestion does not match the expected value"
