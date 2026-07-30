from translator import translate_titles
from analyzer import analyze_titles
from selenium_scraper import (
    create_driver,
    get_article_links,
    scrape_article
)


def main():

    driver = create_driver()

    try:
        articles = get_article_links(driver)

        scraped_articles = []

        print("\n===== SCRAPING ARTICLES =====\n")

        for i, article in enumerate(articles, start=1):

            try:

                article_data = scrape_article(
                    driver,
                    article["url"],
                    i
                )

                scraped_articles.append(article_data)

                print(f"\nArticle {i}")
                print("Title:", article_data["title"])

                print("\nBody Preview:")
                print(article_data["body"][:300])

                print("\nImage saved at:", article_data["image_path"])
                print("-" * 60)

            except Exception as error:

                print(f"\nCould not process article {i}")
                print(error)
                print("-" * 60)

        print("\n===== TRANSLATING TITLES =====\n")

        translated_articles = translate_titles(scraped_articles)

        for i, article in enumerate(translated_articles, start=1):

            print(f"{i}.")
            print("Spanish :", article["title"])
            print("English :", article["translated_title"])
            print("-" * 60)

        print("\n===== REPEATED WORDS =====\n")

        repeated_words = analyze_titles(translated_articles)

        if repeated_words:
            for word, count in repeated_words.items():
                print(f"{word} : {count}")
        else:
            print("No repeated words found.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()