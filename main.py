import pandas as pd
import xgboost
from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
    )
from sklearn.model_selection import (
    train_test_split,
    KFold
    )
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from feature_selector.scally_feature_selector import ScallyShapFeatureSelector
def print_results():
    print('this is main : ')
    
    SFC = ScallyShapFeatureSelector(
        n_features = 4,
        estimator=xgboost.XGBClassifier(),
        estimator_params={'max_depth':[4]},
        hyper_parameter_optimization_method='random',
        shap_version="v0",
        measure_of_accuracy=None,
        list_of_obligatory_features=[],
        test_size = 0.33,
        cv=KFold(n_splits=3),
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
    print(data.columns.to_list())

    X = data.loc[:,data.columns!='default payment next month']
    y = data.loc[:,data.columns=='default payment next month']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

    
    SFC.fit_transform(X_train,y_train)
    XT=SFC.transform(X_test)
    print(XT.columns.to_list())

    return True


if __name__=='__main__':
    print_results()

