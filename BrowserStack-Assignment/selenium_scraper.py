from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_article_links():
    options = Options()

    # Reduce Selenium detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    # Hide webdriver property
    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """)

    # Set a normal Chrome User-Agent
    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {
            "userAgent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        }
    )

    articles = []

    try:
        driver.get("https://elpais.com")

        wait = WebDriverWait(driver, 15)

        # Accept cookies
        accept = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "didomi-notice-agree-button")
            )
        )
        accept.click()

        time.sleep(2)

        # Click Opinion menu
        opinion = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Opinión")
            )
        )
        opinion.click()

        time.sleep(3)

        # Wait until article titles are visible
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h2.c_t")
            )
        )

        titles = driver.find_elements(By.CSS_SELECTOR, "h2.c_t")

        for title in titles[:5]:
            link = title.find_element(By.TAG_NAME, "a")

            articles.append({
                "title": link.text.strip(),
                "url": link.get_attribute("href")
            })

    finally:
        driver.quit()

    return articles