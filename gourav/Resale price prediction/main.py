import numpy as np
import pandas as pd
import joblib
from sklearn import metrics
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import norm, skew 

df_test = pd.read_csv("test_data.csv")
df_train = pd.read_csv("train_data.csv")
df_test_prediction = pd.read_csv("test_data_prediction.csv")
df_test_prediction = df_test_prediction['v39']

def drop_columns(df):
    df = df.drop({"v1","v2","v4","v19"}, axis=1)
    return df

# Fixing categorical data 
def categorical_to_numerical(df):
    cleanup_nums =     {"v5": {"ASC" : 1, "DEALER" : 0},
                        "v11": {"P": 0, "A": 1, "G": 2},
                        "v12": {"P": 0, "A": 1, "G": 2},
                        "v13": {"P": 0, "A": 1, "G": 2},
                        "v14": {"P": 0, "A": 1, "G": 2},
                        "v37": {"N": 0, "Y": 1},
                        "v38": {"NO": 0, "YES": 1}
                        }
    df = df.replace(cleanup_nums)    
    return df

def impute_columns(df_train_imputedValues):
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues["v10"].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v11'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v12'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v13'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v14'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v17'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v18'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v24'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v32'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v33'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v34'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v35'].mode()[0])
    df_train_imputedValues = df_train_imputedValues.fillna(df_train_imputedValues['v36'].mode()[0])
    return df_train_imputedValues

def fix_skew(df):
    from scipy.special import boxcox1p
    skewed_features = ["v32","v34","v27","v24","v38","v33","v29","v10","v15","v7",]
    lam = 0.15
    for feat in skewed_features:
        df[feat] = boxcox1p(df[feat], lam)      
    return df


def predict(X_test,y_test):
    model = joblib.load("model.pkl")
    y_pred=model.predict(X_test)
    print("\t\tError Table")
    print('Mean Absolute Error      : ', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared  Error      : ', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared  Error : ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('R Squared Error          : ', metrics.r2_score(y_test, y_pred))

if __name__ == '__main__':
    df_test = drop_columns(df_test)
    df_test = categorical_to_numerical(df_test)
    df_test = impute_columns(df_test)
    df_test = fix_skew(df_test)
    predict(df_test,df_test_prediction)


