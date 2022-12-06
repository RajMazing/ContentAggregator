from newspaper import Article


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    article.download('punkt')
    article.nlp()


    author_string = "Author(s): "
    for author in article.authors:
        author_string += author
    print(author_string)

    date = article.publish_date


    print("Publish Date: "+str(date.strftime("%m/%d/%Y")))

    print("Top Image Url: " + str(article.top_image))



    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image
    print(image_string)
    print()


    print("A Quick Article Summary")
    print("-----------------------------------------")
    print(article.summary)


    return article.summary