from textblob import TextBlob


def find_sentiment(news_story):
    news = TextBlob(news_story)

    sentiments = []
    for sentence in news.sentence:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiment.append(metric)

    polarity_data = []
    subjectivity_data = []
    for i in range(len(sentiments)):
        if i % 2 == 0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])

    polarity_average = calculate_average(polarity_data)
    subjectivity_average = calculate_average(subjectivity_data)

    print()
    print("Final Analysis")
    print("-----------------------------")
    print("Polarity: " + calculate_sentiment(polarity_average, "polarity"))
    print("Subjectivity: " + calculate_sentiment(subjectivity_average, "subjectivity"))


    def calculate_average(list):
        return sum(list) / len(list)



    def calculate_sentiment(sentiment, type):
        sentiment_category = ""
        if type == "polarity":
            if sentiment > 0.75:
                sentiment_category = "Extremely positive."
            elif sentiment > 0.5:
                sentiment_category = "Significantly positive."
            elif sentiment > 0.3:
                sentiment_category = "Fairly positive"
            elif sentiment > 0.1:
                sentiment_category = "Slightly positive"
            elif sentiment < -0.1:
                sentiment_category = "Slightly negative"
            elif sentiment < -0.3:
                sentiment_category = "Fairly negative"
            elif sentiment < -0.5:
                sentiment_category = "Significantly negative"
            elif sentiment < -0.75:
                sentiment_category = "Extremely negative."
            else:
                sentiment_category = "Neutral."
            return sentiment_category
        elif type == "subjectivity":
            if sentiment > 0.75:
                sentiment_category = "Extremely subjective"
            elif sentiment > 0.75:
                sentiment_category = "Fairly subjective."
            elif sentiment > 0.5:
                sentiment_category = "Fairly subjective"
            elif sentiment > 0.3:
                sentiment_category = "Fairly objective"
            elif sentiment > 0.1: sentiment_category = "Extremely objective"
            return sentiment_category
        else:
            print("Invalid Input.")



