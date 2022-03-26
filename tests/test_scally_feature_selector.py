import pandas as pd
import numpy as np
from feature_selector.scally_feature_selector import ScallyFeatureSelector


def test_scally_feature_selector():
    """Test feature scally selector add """

    SFC = ScallyFeatureSelector()
    data = pd.read_csv('data/data.csv')
    X = data.loc[:,data.columns!='default payment next month']
    y = data.loc[:,data.columns=='default payment next month']
    SFC.fit_transform(X,y)
    XT=SFC.transform(X)
    
    assert XT.columns.to_list()==['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

