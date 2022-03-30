from optuna.samplers._tpe.sampler import TPESampler
from optuna.pruners import HyperbandPruner

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

    SFC_OPTUNA = ScallyShapFeatureSelector(
        n_features=4,
        estimator=xgboost.XGBClassifier(),
        estimator_params={
            "max_depth": [4, 5],
            "min_child_weight": [0.1, 0.9],
            "gamma": [1, 9],
            "booster": ["gbtree", "dart"],
        },
        hyper_parameter_optimization_method="optuna",
        shap_version="v0",
        measure_of_accuracy="f1",
        list_of_obligatory_features=[],
        test_size=0.33,
        cv=KFold(n_splits=3,random_state=42,shuffle=True),
        with_shap_summary_plot=False,
        with_shap_interaction_plot=False,
        with_stratified=True,
        verbose=3,
        random_state=42,
        n_jobs=-1,
        n_iter=100,
        eval_metric="auc",
        number_of_trials=10,
        sampler=TPESampler(),
        pruner=HyperbandPruner(),
    )

    SFC_GRID = ScallyShapFeatureSelector(
        n_features=4,
        estimator=xgboost.XGBClassifier(),
        estimator_params={
            "max_depth": [4, 5],
            "min_child_weight": [0.1, 0.9],
            "gamma": [1, 9],
            "booster": ["gbtree", "dart"],
        },
        hyper_parameter_optimization_method="grid",
        shap_version="v0",
        measure_of_accuracy="f1",
        list_of_obligatory_features=[],
        test_size=0.33,
        cv=KFold(n_splits=3,random_state=42,shuffle=True),
        with_shap_summary_plot=False,
        with_shap_interaction_plot=False,
        with_stratified=True,
        verbose=3,
        random_state=42,
        n_jobs=-1,
        n_iter=100,
        eval_metric="auc",
        number_of_trials=10,
        sampler=TPESampler(),
        pruner=HyperbandPruner(),
    )

    try:
        data = pd.read_csv("data/data.csv")
    except:
        data = pd.read_csv("/home/circleci/project/data/data.csv")
    print(data.columns.to_list())

    X = data.loc[:, data.columns != "default payment next month"]
    y = data.loc[:, data.columns == "default payment next month"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=0
    )

    SFC_OPTUNA.fit_transform(X_train, y_train)
    XT_OPTUNA = SFC_OPTUNA.transform(X_test)

    SFC_GRID.fit_transform(X_train, y_train)
    XT_GRID = SFC_GRID.transform(X_test)

    assert XT_GRID.columns.to_list()==['PAY_0', 'LIMIT_BAL', 'PAY_AMT2', 'BILL_AMT1']
    assert len(XT_OPTUNA.columns.to_list())==4


