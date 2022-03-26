import pandas as pd
import numpy as np
import xgboost
from sklearn.model_selection import train_test_split

from feature_selector.scally_feature_selector import ScallyFeatureSelector


def test_scally_feature_selector():
    """Test feature scally selector add """

    SFC = ScallyFeatureSelector(n_features=4,model=xgboost.XGBClassifier(),list_of_features=[])
    try:
        data = pd.read_csv('data/data.csv')
    except:
        data = pd.read_csv('/home/circleci/project/data/data.csv')

    X = data.loc[:,data.columns!='default payment next month']
    y = data.loc[:,data.columns=='default payment next month']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    SFC.fit_transform(X_train,y_train)
    XT=SFC.transform(X_test)
    assert XT.columns.to_list()==['PAY_0', 'LIMIT_BAL', 'BILL_AMT1', 'PAY_AMT2']

