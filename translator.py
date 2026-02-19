import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
}
import requests
import logging
from config import Google_Translate_API, Google_Translate_HOST, Google_Translate_URL


def translate_titles(titles):
    translated = []

    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-key": Google_Translate_API,
        "x-rapidapi-host": Google_Translate_HOST
    }

    for title in titles:
        try:
            payload = {
                "from": "es",
                "to": "en",
                "text": title
            }

            response = requests.post(
                Google_Translate_URL,
                json=payload,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()
                translated_text = result.get("trans", "")
                logging.info(f"Translated: {translated_text}")
                translated.append(translated_text)
            else:
                logging.error(f"Translation API error: {response.status_code}")
                translated.append("")

        except Exception as e:
            logging.error(f"Translation failed: {e}")
            translated.append("")

    return translated


def translate_titles(titles):
    translated = []

    for title in titles:
        payload = {
            "from": "es",
            "to": "en",
            "q": title
        }

        try:
            response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
            data = response.json()

            # 🔍 Defensive parsing
            if isinstance(data, dict):
                translated_text = (
                    data.get("translatedText")
                    or data.get("translation")
                    or title  # fallback
                )
            else:
                translated_text = title

        except Exception:
            translated_text = title

        translated.append(translated_text)
        print(f"TRANSLATED: {translated_text}")

    return translated
