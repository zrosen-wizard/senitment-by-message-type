import pandas as pd
import numpy as np
from .VADER import VADER

class tagged_corpus():

    def __init__(self, df, body_column='body'):
        super(tagged_corpus, self).__init__()
        self.df = df
        self.sentiment = VADER()
        self.tags = self.tag(body_column)

    def highest_prob(self, x):
        keys = np.array(['neg', 'pos', 'neu'])
        vals = np.array([x[k] for k in keys])
        i = vals.argmax()
        return np.array([keys[i], vals[i]]).reshape(1,2)

    def tag(self, column='body'):
        new_cols = self.df[column].apply(lambda x: self.highest_prob(self.sentiment(str(x)))).values.tolist()
        self.df[['sentiment', 'score']] = np.concatenate(new_cols, axis=0)

