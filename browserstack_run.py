import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from config import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY
from scraper import scrape_articles


BROWSERS = [
    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Firefox", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Edge", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"deviceName": "iPhone 14", "realMobile": "true", "osVersion": "16"},
    {"deviceName": "Samsung Galaxy S22", "realMobile": "true", "osVersion": "12"}
]


def run_browserstack_test(capabilities):
    options = Options()
    options.set_capability("bstack:options", {
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    })

    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    env_name = capabilities.get("browserName") or capabilities.get("deviceName")
    logging.info(f"\n========== Running on {env_name} ==========\n")
    scrape_articles(driver, env = env_name)

    driver.quit()


def run_parallel_tests():
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_browserstack_test, BROWSERS)
