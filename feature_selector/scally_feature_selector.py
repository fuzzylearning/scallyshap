
from sklearn.base import BaseEstimator, TransformerMixin

class ScallyFeatureSelector(BaseEstimator, TransformerMixin):

    def __init__(self):

        self.config = None   
        self.final_list = None  

    def fit(self, X, y):

        cols = X.columns
        self.final_list = cols

        return self

    def transform(self, X):

        return  X[self.final_list]



