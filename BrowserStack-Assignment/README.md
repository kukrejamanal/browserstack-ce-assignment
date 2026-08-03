# 📰 El País Opinion Scraper

> **BrowserStack Coding Assignment**
>
> 🚀 Selenium • 🌐 BrowserStack • 🌍 Translation API • 📊 Text Analysis

A Python-based Selenium automation project developed for the **BrowserStack Coding Assignment**. The project scrapes opinion articles from **El País**, translates article titles into English, performs text analysis, and validates execution across multiple browsers using BrowserStack.

---

## 📖 Overview

This project automates the complete workflow of collecting articles from the **Opinion** section of **El País**, one of Spain's leading newspapers.

The solution demonstrates:

- Selenium Web Automation
- Dynamic Web Scraping
- Image Downloading
- Translation API Integration
- Text Processing & Analysis
- Cross-Browser Testing using BrowserStack

The project was designed with a modular architecture, separating local execution from BrowserStack execution to keep the code clean, maintainable, and reusable.

---

## ✨ Features

- 🌍 Open **El País** in Spanish
- 📰 Navigate to the **Opinion** section
- 📄 Scrape the first **5 opinion articles**
- ✍ Extract article titles and content
- 🖼 Download cover images (when available)
- 🌐 Translate article titles from **Spanish → English**
- 📊 Identify repeated words across translated titles
- 💻 Execute locally using Selenium
- ☁️ Execute in parallel on BrowserStack across desktop and mobile browsers

---

# 🏗️ Project Architecture

```text
BrowserStack-Assignment/
│
├── analyzer.py                  # Repeated word analysis
├── translator.py                # Spanish → English translation
│
├── selenium_scraper.py          # Local Selenium scraper
├── main.py                      # Local execution
│
├── browserstack_driver.py       # BrowserStack Remote Driver
├── browserstack_scraper.py      # BrowserStack scraper
├── browserstack_runner.py       # Parallel BrowserStack execution
├── browserstack.yml             # BrowserStack configuration
│
├── images/                      # Downloaded article images
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

- Python 3
- Selenium WebDriver
- Requests
- BeautifulSoup4
- Deep Translator
- BrowserStack Automate

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/kukrejamanal/browserstack-ce-assignment.git

cd browserstack-ce-assignment
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

Execute

```bash
python main.py
```

The application will:

- Navigate to El País
- Open the Opinion section
- Scrape the first five opinion articles
- Download article images
- Translate article titles into English
- Analyze repeated words appearing across translated titles

---

# ☁️ Run on BrowserStack

Configure your BrowserStack credentials and execute:

```bash
python browserstack_runner.py
```

The project runs in parallel across multiple browser and device combinations including:

- Windows 11 • Chrome
- Windows 11 • Edge
- macOS Sonoma • Safari
- Samsung Galaxy S24
- iPhone 15

---

# ✅ Assignment Requirements

| Requirement | Status |
|-------------|:------:|
| Visit El País in Spanish | ✅ |
| Navigate to Opinion Section | ✅ |
| Scrape First Five Articles | ✅ |
| Print Titles & Content | ✅ |
| Download Cover Images | ✅ |
| Translate Titles to English | ✅ |
| Analyze Repeated Words | ✅ |
| Local Selenium Execution | ✅ |
| BrowserStack Parallel Execution | ✅ |

---

# 💡 Design Decisions

To keep the project clean and maintainable, the implementation is divided into independent modules.

- **Scraper Layer** – Handles article extraction.
- **Translation Layer** – Performs Spanish to English translation.
- **Analysis Layer** – Identifies repeated words.
- **BrowserStack Layer** – Handles cloud execution without affecting the local scraper.

This separation ensures that local execution remains stable while BrowserStack-specific logic is isolated for cloud testing.

---

# 🚀 Future Improvements

Some enhancements that could be added in the future include:

- Improved support for responsive mobile layouts
- Enhanced retry mechanisms for dynamic web elements
- Structured logging for BrowserStack sessions
- Exporting scraped data to JSON or CSV
- Automated reporting of BrowserStack execution results

---

# 👨‍💻 Author

**Manal Kukreja**

GitHub: https://github.com/kukrejamanal

---

> ⭐ *Thank you for reviewing my submission! I enjoyed building this project and exploring BrowserStack's parallel cross-browser testing capabilities.*