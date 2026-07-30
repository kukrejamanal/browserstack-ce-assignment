from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os
import time


def create_driver():
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )
    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    driver = webdriver.Chrome(options=options)

    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """)

    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {
            "userAgent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        }
    )

    return driver


def get_article_links(driver):

    articles = []

    driver.get("https://elpais.com")

    wait = WebDriverWait(driver, 15)

    accept_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "didomi-notice-agree-button")
        )
    )
    accept_button.click()

    time.sleep(2)

    opinion = wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Opinión")
        )
    )
    opinion.click()

    time.sleep(3)

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h2.c_t")
        )
    )

    titles = driver.find_elements(By.CSS_SELECTOR, "h2.c_t")

    for title in titles[:5]:

        link = title.find_element(By.TAG_NAME, "a")

        articles.append(
            {
                "title": link.text.strip(),
                "url": link.get_attribute("href")
            }
        )

    return articles


def get_article_title(driver):

    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h1")
        )
    )

    return title.text.strip()


def get_article_body(driver):

    selectors = [
        "div.a_c.clearfix",
        "div.a_c",
        "article div.a_c",
        "article"
    ]

    for selector in selectors:

        try:

            body = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, selector)
                )
            )

            paragraphs = body.find_elements(By.TAG_NAME, "p")

            article_text = []

            for paragraph in paragraphs:

                text = paragraph.text.strip()

                if text:
                    article_text.append(text)

            if article_text:
                return "\n\n".join(article_text)

        except:
            pass

    return ""

def get_image_url(driver):

    image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "figure img")
        )
    )

    return image.get_attribute("src")


def download_image(image_url, article_number):

    os.makedirs("images", exist_ok=True)

    image_path = os.path.join(
        "images",
        f"article_{article_number}.jpg"
    )

    response = requests.get(
        image_url,
        timeout=20
    )

    response.raise_for_status()

    with open(image_path, "wb") as file:
        file.write(response.content)

    return image_path


def scrape_article(driver, url, article_number):

    driver.get(url)

    title = get_article_title(driver)

    body = get_article_body(driver)

    image_url = get_image_url(driver)

    image_path = download_image(
        image_url,
        article_number
    )

    return {
        "title": title,
        "body": body,
        "image_url": image_url,
        "image_path": image_path
    }