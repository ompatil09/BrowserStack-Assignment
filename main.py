import logging
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scraper import scrape_articles
from translator import translate_titles
from text_analyzer import analyze_titles
from browserstack_run import run_parallel_tests


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("output.log", encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def run_local():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    articles = scrape_articles(driver, env="LOCAL")
    driver.quit()

    titles = [article["title"] for article in articles]

    translated = translate_titles(titles)
    analyze_titles(translated)


if __name__ == "__main__":

    setup_logging()

    logging.info("Running locally...\n")
    run_local()

    logging.info("\nRunning on BrowserStack...\n")
    run_parallel_tests()
