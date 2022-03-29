import pandas as pd
import numpy as np
import xgboost
from sklearn.model_selection import (
    train_test_split,
    KFold
    )

from feature_selector.scally_feature_selector import ScallyShapFeatureSelector


def test_scally_feature_selector():
    """Test feature scally selector add """

    SFC = ScallyShapFeatureSelector(
        n_features=4,
        estimator=xgboost.XGBClassifier(),
        estimator_params={'max_depth':[4]},
        hyper_parameter_optimization_method='Optuna',
        shap_version="v0",
        measure_of_accuracy=None,
        list_of_obligatory_features=[],
        test_size = 0.33,
        cv=KFold(n_splits=2),
        with_shap_summary_plot=False,
        with_shap_interaction_plot=False,
        verbose = 1,
        random_state=0,
        n_jobs=-1,
        )
    try:
        data = pd.read_csv('data/data.csv')
    except:
        data = pd.read_csv('/home/circleci/project/data/data.csv')

    X = data.loc[:,data.columns!='default payment next month']
    y = data.loc[:,data.columns=='default payment next month']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    SFC.fit_transform(X_train,y_train)
    XT=SFC.transform(X_test)
    assert XT.columns.to_list()==['PAY_0', 'LIMIT_BAL', 'BILL_AMT1', 'PAY_AMT1']

