import xgboost as xgb
def add_two_number(a,b):
    print('add two numbers:', a+b)
    print(xgb.__name__)
    return a+b


if __name__ == "__main__":
    add_two_number(5,7)


