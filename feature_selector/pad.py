
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
from sklearn.metrics import make_scorer

import fasttreeshap

class Shap_parametric(BaseEstimator, TransformerMixin):

    def __init__(self,n_features,model,list_of_features):

        self.n_features=n_features
        self.model=model
        self.grid_search= None
        self.importance_df = None
        self.list_of_features= list_of_features

    def fit(self, X, y):

        self.cols = X.columns

        # train model with those setting comes from conf to select best feature in each cv
        self.grid_search = GridSearchCV(self.model, param_grid=self.params,
                        cv=StratifiedKFold(n_splits=2, random_state=0,shuffle=True),
                            n_jobs=1, scoring=make_scorer(f1_score),verbose=0)
        
        self.grid_search.fit(X, y)
        best_estimator = self.grid_search.best_estimator_
        shap_explainer = fasttreeshap.TreeExplainer(best_estimator, algorithm = "v0", n_jobs = n_jobs)
        shap_values_v0 = shap_explainer(X).values
        shap_values_v0.shape
        shap_values = shap_explainer.shap_values(X)
        print(shap_values)
        shap_sum = np.abs(shap_values).mean(axis=0)
        self.importance_df = pd.DataFrame([X.columns.tolist(), shap_sum.tolist()]).T
        self.importance_df.columns = ['column_name', 'shap_importance']
        self.importance_df = self.importance_df.sort_values('shap_importance', ascending=False)
        num_feat = min([self.n_features,self.importance_df.shape[0]])
        self.selected_cols = self.importance_df['column_name'][0:num_feat].to_list()

        return self

    def transform(self, X):

        return  X[self.selected_cols]
