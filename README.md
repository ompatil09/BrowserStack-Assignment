# 📰 BrowserStack Automation Assignment

## Overview

This project automates the scraping of **Opinion articles from EL PAÍS**, a Spanish news outlet, and performs **cross-browser & cross-device testing using BrowserStack**.

It collects article links, extracts titles and content in Spanish, translates article titles to English, analyzes repeated words, and logs all results in a structured format.

---

## 🚀 What This Project Does

### 1️⃣ Scrapes Opinion Articles
- Loads the **EL PAÍS Opinion** page  
- Collects the latest **5 article URLs**  
- Fetches full **Spanish titles and article content**

### 2️⃣ Translates Titles
- Uses **Google Translate API via RapidAPI**
- Converts titles from **Spanish → English**
- ⚠️ If the RapidAPI quota is exhausted, titles will remain in Spanish

### 3️⃣ Analyzes Translated Titles
- Identifies words repeated **more than twice** across all translated titles

### 4️⃣ Runs Cross-Browser & Device Tests
Executed via **BrowserStack** on:
- Chrome
- Edge
- Firefox
- iPhone 14
- Samsung Galaxy S22

### 5️⃣ Logs Everything
- Runs locally and on BrowserStack
- Writes structured logs to **output.log**

---

## 📂 Repository Structure

```
.
├── browserstack_runner.py      # Runs parallel BrowserStack sessions
├── config.py                   # Config values & API keys
├── main.py                     # Entry point
├── scraper.py                  # EL PAÍS opinion scraper
├── translator.py               # Title translation logic
├── text_analyzer.py            # Repeated words analyzer
├── utils.py                    # Helpers
├── output.log                  # Log output from last run
├── pyproject.toml              # uv project config
├── uv.lock                     # Lock file for dependencies
├── README.md                   # This file
```

---

### 🛠 Requirements

This is a uv-managed Python project.

Make sure you have:
  1)  Python 3.10+
  2)  uv package manager

---

### ⚙️ Setup & Run (Step-by-Step)
1️⃣ Fork the Repository
   Click the Fork button (top-right corner of the repo page).

---

2️⃣ Clone Your Fork
```
    git clone https://github.com/ompatil09/BrowserStack-Assignment
    cd BrowserStack-Assignment
```

---

3️⃣ Install Python
Check your version:
```
python --version
```
If Python is not installed: https://www.python.org/downloads/

---

4️⃣ Install uv
If not installed:
```
pip install uv
```

---

5️⃣ Install Dependencies
```
uv sync
```

---

6️⃣ Run the Automation
```
uv run py main.py
```

---

### This will:
- Scrape locally
- Translate titles
- Log repeated words
- Then run BrowserStack tests
- Output is written to:
```
output.log
```


---

### 🔑 Credentials Required
You need two sets of credentials.

---

🅰 Google Translate API (via RapidAPI)
1) Visit: https://rapidapi.com

2) Search: Google Translate

3) Subscribe (free plan)

4) Copy your API Key

---

🅱 BrowserStack Credentials
1) Sign up at: https://www.browserstack.com/

2) Go to Account → Settings

3) Copy:

USERNAME

ACCESS_KEY

---

### 🔧 Add Credentials
Open config.py and update:
```
# Google Translate
Google_Translate_API = "YOUR_RAPIDAPI_KEY"
Google_Translate_HOST = "google-translate1.p.rapidapi.com"
Google_Translate_URL = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# BrowserStack
BROWSERSTACK_USERNAME = "YOUR_BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"

# Scraper
OPINION_URL = "https://elpais.com/opinion/"
ARTICLE_LIMIT = 5
```

---

### 📄 Output
All results are logged in:
```
output.log
```

---

### Each run includes:
- Collected links
- Article titles (Spanish)
- Full article text (Spanish)
- Translated titles
-  Repeated words analysis
- BrowserStack run info

                  
