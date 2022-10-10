from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as sentiment

class VADER():

    def __init__(self):
        super(VADER, self).__init__()
        self.S = sentiment()

    def __call__(self, x):
        return self.S.polarity_scores(x)