import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
import shap
from sklearn.metrics import f1_score
from sklearn.metrics import make_scorer
import xgboost

import fasttreeshap


class ScallyShapFeatureSelector(BaseEstimator, TransformerMixin):
    """Feature Selector class using shap values
    Parameters
    ----------
    estimator : estimator instance
        An unfitted estimator.
    cv : int, cross-validation generator or an iterable, default=None
    n_jobs : int, default=None
        Number of jobs to run in parallel. When evaluating a new feature to
        add or remove, the cross-validation procedure is parallel over the
        folds.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.
    Attributes
    ----------
    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.
        .. versionadded:: 0.24
    """

    def __init__(
        self,
        n_features=5,
        estimator=None,
        estimator_params=None,
        hyper_parameter_optimization_method="Optuna",
        shap_version="v0",
        measure_of_accuracy=None,
        list_of_obligatory_features=[],
        test_size=0.33,
        cv=3,
        with_shap_summary_plot=False,
        with_shap_interaction_plot=False,
        verbose=1,
        random_state=0,
        n_jobs=-1,
    ):

        self.n_features = n_features
        self.estimator = estimator
        self.estimator_params = estimator_params
        self.hyper_parameter_optimization_method = hyper_parameter_optimization_method
        self.shap_version = shap_version
        self.measure_of_accuracy = measure_of_accuracy
        self.list_of_obligatory_features = list_of_obligatory_features
        self.test_size = test_size
        self.cv = cv
        self.with_shap_summary_plot = with_shap_summary_plot
        self.with_shap_interaction_plot = with_shap_interaction_plot
        self.verbose = verbose
        self.random_state = random_state
        self.n_jobs = n_jobs
        self.importance_df = None

    @property
    def n_features(self):
        print("Getting value for n_features")
        return self._n_features

    @n_features.setter
    def n_features(self, value):
        print("Setting value for n_features")
        if value < 0:
            raise ValueError("n_features below 0 is not possible")
        self._n_features = value

    @property
    def estimator(self):
        print("Getting value for estimator")
        return self._estimator

    @estimator.setter
    def estimator(self, value):
        print("Setting value for estimator")
        if value.__class__.__name__ not in [
            "XGBRegressor",
            "XGBClassifier",
            "RandomForestClassifier",
            "RandomForestRegressor",
            "CatBoostClassifier",
            "CatBoostRegressor",
            "BalancedRandomForestClassifier",
        ]:

            raise TypeError(f"{value.__class__.__name__} model is not supported yet")
        self._estimator = value

    @property
    def estimator_params(self):
        print("Getting value for estimator_params")
        return self._estimator_params

    @estimator_params.setter
    def estimator_params(self, value):
        print(self.estimator)
        print(self.estimator.get_params().keys())
        if value.keys() <= self.estimator.get_params().keys():
            print("Setting value for estimator_params")
            self._estimator_params = value
        else:
            raise TypeError(
                f"error occures during parameter checking for {value.__class__.__name__}"
            )

    @property
    def hyper_parameter_optimization_method(self):
        print("Getting value for hyper_parameter_optimization_method")
        return self._hyper_parameter_optimization_method

    @hyper_parameter_optimization_method.setter
    def hyper_parameter_optimization_method(self, value):
        print("Setting value for hyper_parameter_optimization_method")
        if (
            value.lower() == "optuna"
            or value.lower() == "grid"
            or value.lower() == "random"
        ):
            self._hyper_parameter_optimization_method = value
        else:
            raise ValueError(
                f"error occures during selecting optimization_method, {value} is not supported."
            )

    @property
    def shap_version(self):
        print("Getting value for shap_version")
        return self._shap_version

    @shap_version.setter
    def shap_version(self, value):
        print("Setting value for shap_version")
        self._shap_version = value

    @property
    def measure_of_accuracy(self):
        print("Getting value for measure_of_accuracy")
        return self._measure_of_accuracy

    @measure_of_accuracy.setter
    def measure_of_accuracy(self, value):
        print("Setting value for measure_of_accuracy")
        self._measure_of_accuracy = value

    @property
    def list_of_obligatory_features(self):
        print("Getting value for list_of_obligatory_features")
        return self._list_of_obligatory_features

    @list_of_obligatory_features.setter
    def list_of_obligatory_features(self, value):
        print("Setting value for list_of_obligatory_features")
        self._list_of_obligatory_features = value

    @property
    def test_size(self):
        print("Getting value for test_size")
        return self._test_size

    @test_size.setter
    def test_size(self, value):
        print("Setting value for test_size")
        self._test_size = value

    @property
    def cv(self):
        print("Getting value for Cross Validation object")
        return self._cv

    @cv.setter
    def cv(self, value):
        print("Setting value for Cross Validation object")
        self._cv = value

    @property
    def with_shap_summary_plot(self):
        print("Getting value for with_shap_summary_plot")
        return self._with_shap_summary_plot

    @with_shap_summary_plot.setter
    def with_shap_summary_plot(self, value):
        print("Setting value for with_shap_summary_plot")
        self._with_shap_summary_plot = value

    @property
    def with_shap_interaction_plot(self):
        print("Getting value for with_shap_interaction_plot")
        return self._with_shap_interaction_plot

    @with_shap_interaction_plot.setter
    def with_shap_interaction_plot(self, value):
        print("Setting value for with_shap_interaction_plot")
        self._with_shap_interaction_plot = value

    @property
    def verbose(self):
        print("Getting value for verbose")
        return self._verbose

    @verbose.setter
    def verbose(self, value):
        print("Setting value for verbose")
        self._verbose = value

    @property
    def random_state(self):
        print("Getting value for random_state")
        return self._random_state

    @random_state.setter
    def random_state(self, value):
        print("Setting value for random_state")
        self._random_state = value

    @property
    def n_jobs(self):
        print("Getting value for n_jobs")
        return self._n_jobs

    @n_jobs.setter
    def n_jobs(self, value):
        print("Setting value for n_jobs")
        self._n_jobs = value

    @property
    def importance_df(self):
        print("Getting value for importance_df")
        return self._importance_df

    @importance_df.setter
    def importance_df(self, value):
        print("Setting value for importance_df")
        self._importance_df = value

    def fit(self, X, y):

        self.cols = X.columns

        # train model with those setting comes from conf to select best feature in each cv
        self.grid_search = GridSearchCV(
            self.estimator,
            param_grid=self.estimator_params,
            cv=StratifiedKFold(n_splits=2, random_state=0, shuffle=True),
            n_jobs=1,
            scoring=make_scorer(f1_score),
            verbose=0,
        )

        self.grid_search.fit(X, y)
        best_estimator = self.grid_search.best_estimator_
        shap_explainer = fasttreeshap.TreeExplainer(
            best_estimator, algorithm=self.shap_version, n_jobs=-1
        )
        shap_values_v0 = shap_explainer(X).values
        shap_values_v0.shape
        shap_values = shap_explainer.shap_values(X)
        print(shap_values)
        shap_sum = np.abs(shap_values).mean(axis=0)
        self.importance_df = pd.DataFrame([X.columns.tolist(), shap_sum.tolist()]).T
        self.importance_df.columns = ["column_name", "shap_importance"]
        self.importance_df = self.importance_df.sort_values(
            "shap_importance", ascending=False
        )
        print(self.importance_df[0 : self.n_features])
        num_feat = min([self.n_features, self.importance_df.shape[0]])
        self.selected_cols = self.importance_df["column_name"][0:num_feat].to_list()
        shap.summary_plot(shap_values, X, max_display=self.n_features)

        return self

    def transform(self, X):

        return X[self.selected_cols]
