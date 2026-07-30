from concurrent.futures import ThreadPoolExecutor
import traceback

from browserstack_driver import create_browserstack_driver
from browserstack_scraper import (
    get_article_links,
    scrape_article
)
from translator import translate_titles
from analyzer import analyze_titles


platforms = [

    {
        "name": "Windows Chrome",
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Chrome",
        "browserVersion": "latest"
    },

    {
        "name": "Windows Edge",
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Edge",
        "browserVersion": "latest"
    },

    {
        "name": "macOS Safari",
        "os": "OS X",
        "osVersion": "Sonoma",
        "browserName": "Safari",
        "browserVersion": "latest"
    },

    {
        "name": "Samsung Galaxy S24",
        "deviceName": "Samsung Galaxy S24",
        "osVersion": "14.0",
        "browserName": "Chrome"
    },

    {
        "name": "iPhone 15",
        "deviceName": "iPhone 15",
        "osVersion": "17",
        "browserName": "Safari"
    }

]


def run_test(platform):

    driver = None

    print(f"\n========== {platform['name']} ==========\n")

    try:

        driver = create_browserstack_driver(platform)

        print("BrowserStack session started.")

        articles = get_article_links(driver)

        print(f"Found {len(articles)} articles")

        scraped_articles = []

        for index, article in enumerate(articles, start=1):

            print(f"Scraping article {index}")

            article_data = scrape_article(
                driver,
                article["url"],
                index
            )

            scraped_articles.append(article_data)

        translated_articles = translate_titles(scraped_articles)

        repeated_words = analyze_titles(translated_articles)

        print("\nRepeated Words")

        if repeated_words:

            for word, count in repeated_words.items():
                print(f"{word} : {count}")

        else:
            print("No repeated words found.")

        print(f"\n{platform['name']} completed successfully.\n")

    except Exception:

        print(f"\n{platform['name']} failed.\n")

        traceback.print_exc()

    finally:

        if driver:

            driver.quit()

            print("Session closed.")


def main():

    with ThreadPoolExecutor(max_workers=5) as executor:

        futures = []

        for platform in platforms:

            futures.append(
                executor.submit(
                    run_test,
                    platform
                )
            )

        for future in futures:
            future.result()


if __name__ == "__main__":
    main()