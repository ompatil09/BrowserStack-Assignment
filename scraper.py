import time
import requests
import logging
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import OPINION_URL, ARTICLE_LIMIT, IMAGES_DIR
from utils import download_image, ensure_directory

noise_keywords = [
    "suscripción",
    "modalidad Premium",
    "términos y condiciones",
    "compartiendo tu cuenta",
    "añadir otro usuario"
]

def fetch_article_content(link):
    try:
        response = requests.get(link, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Title
        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else ""

        # Paragraphs inside article
        paragraphs = soup.select("article p")

        content_list = []
        for p in paragraphs:
            text = p.get_text(" ",strip=True)
            if len(text) < 40:
                continue

            if any(keyword in text.lower() for keyword in noise_keywords):
                continue

            content_list.append(text)

        content = "\n\n".join(content_list)

        return title, content

    except Exception as e:
        logging.error(f"Content fetch failed for {link}: {e}")
        return "", ""


def scrape_articles(driver, env="LOCAL"):
    ensure_directory(IMAGES_DIR)

    driver.get(OPINION_URL)

    # Wait for actual article titles to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.c_t.c_t-i"))
    )

    title_elements = driver.find_elements(By.CSS_SELECTOR, "h2.c_t.c_t-i")

    links = []

    for elem in title_elements:
        try:
            anchor = elem.find_element(By.TAG_NAME, "a")
            link = anchor.get_attribute("href")

            if link and "/opinion/" in link:
                links.append(link)

        except:
            continue

    # Remove duplicates and limit
    links = list(dict.fromkeys(links))[:ARTICLE_LIMIT]

    logging.info(f"Collected Links: {links}")

    results = []

    # Visit each article page
    for idx, link in enumerate(links):
        title, content = fetch_article_content(link)

        logging.info(f"\n[{env}] --- Article {idx + 1} ---")
        logging.info(f"[{env}] Title (Spanish): {title}")
        logging.info(f"[{env}] Content (Spanish):\n{content}")
        logging.info(f"[{env}]" + "="*80)

        results.append({
            "title": title,
            "content": content,
            "image_path": None
        })
    return results
