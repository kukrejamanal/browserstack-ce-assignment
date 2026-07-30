from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os
import time


def get_article_links(driver):

    articles = []

    driver.get("https://elpais.com")

    wait = WebDriverWait(driver, 30)

    time.sleep(3)

    # Accept cookies if visible
    try:
        accept_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "didomi-notice-agree-button")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            accept_button
        )

        time.sleep(2)

    except Exception:
        pass

    opinion = wait.until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Opinión")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        opinion
    )

    time.sleep(1)

    driver.execute_script(
        "arguments[0].click();",
        opinion
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h2.c_t")
        )
    )

    titles = driver.find_elements(
        By.CSS_SELECTOR,
        "h2.c_t"
    )

    for title in titles[:5]:

        link = title.find_element(
            By.TAG_NAME,
            "a"
        )

        articles.append(
            {
                "title": link.text.strip(),
                "url": link.get_attribute("href")
            }
        )

    return articles


def get_article_title(driver):

    title = WebDriverWait(driver, 20).until(
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

            body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, selector)
                )
            )

            paragraphs = body.find_elements(
                By.TAG_NAME,
                "p"
            )

            article_text = []

            for paragraph in paragraphs:

                text = paragraph.text.strip()

                if text:
                    article_text.append(text)

            if article_text:
                return "\n\n".join(article_text)

        except Exception:
            pass

    return ""


def get_image_url(driver):

    selectors = [
        "figure img",
        "picture img",
        "article img"
    ]

    for selector in selectors:

        try:

            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, selector)
                )
            )

            src = image.get_attribute("src")

            if src:
                return src

        except Exception:
            pass

    return ""


def download_image(image_url, article_number):

    if not image_url:
        return ""

    os.makedirs("images", exist_ok=True)

    image_path = os.path.join(
        "images",
        f"article_{article_number}.jpg"
    )

    try:

        response = requests.get(
            image_url,
            timeout=20
        )

        response.raise_for_status()

        with open(image_path, "wb") as file:
            file.write(response.content)

        return image_path

    except Exception:
        return ""


def scrape_article(driver, url, article_number):

    driver.get(url)

    time.sleep(2)

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