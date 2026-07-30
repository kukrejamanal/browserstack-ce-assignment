from deep_translator import GoogleTranslator


def translate_title(title):

    try:
        translated = GoogleTranslator(
            source="es",
            target="en"
        ).translate(title)

        return translated

    except Exception as error:

        print(f"Translation failed: {error}")

        return title


def translate_titles(articles):

    translated_articles = []

    for article in articles:

        translated_title = translate_title(
            article["title"]
        )

        article["translated_title"] = translated_title

        translated_articles.append(article)

    return translated_articles