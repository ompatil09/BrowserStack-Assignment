import logging
import os
import string
import requests


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, timeout=10)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
    except Exception as e:
        logging.error(f"Image download failed: {e}")


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text
