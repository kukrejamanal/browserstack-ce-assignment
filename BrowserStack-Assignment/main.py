from selenium_scraper import get_article_links


def main():
    articles = get_article_links()

    print()

    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")
        print(article["url"])
        print("-" * 50)


if __name__ == "__main__":
    main()