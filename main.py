import pandas as pd
import xgboost
from feature_selector.scally_feature_selector import ScallyFeatureSelector

def print_main():
    print('this is main : ')

    SFC = ScallyFeatureSelector()
    try:
        data = pd.read_csv('data/data.csv')
    except:
        data = pd.read_csv('/home/circleci/project/data/data.csv')
    print(data.columns.to_list())
    X = data.loc[:,data.columns!='default payment next month']
    y = data.loc[:,data.columns=='default payment next month']

    SFC.fit_transform(X,y)
    XT=SFC.transform(X)
    print(XT.columns.to_list())

    return True


if __name__=='__main__':
    print_main()

