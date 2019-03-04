import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import Lasso,Ridge
from sklearn.preprocessing import PolynomialFeatures
warnings.filterwarnings("ignore")
np.random.seed(42)


df = pd.read_csv("acty_set_2_114_calc_20171229_1525.csv", sep = ';')
print(len(df))
                              
y = df.pop("label")



drop1=df.pop("rec_id")
drop2=df.pop("username")

# Rige  v vide tsify 
# nuzno kolvo nesovpadenii           

                              
train, test, y_train, y_test = train_test_split(df, y, test_size = 0.2)

def fit_predict(train, test, y_train, y_test, scaler = None):
    if scaler is None:
        lr = Ridge()
        lr.fit(train, y_train)
        y_pred = lr.predict(test)
        print('MAE score:', mean_absolute_error(y_test, y_pred))
    else:
        train_scaled = scaler.fit_transform(train)
        test_scaled = scaler.transform(test)
        lr = Ridge()
        lr.fit(train_scaled, y_train)
        y_pred = lr.predict(test_scaled)
        print('MAE score:', mean_absolute_error(y_test, y_pred))

fit_predict(train,test,y_train,y_test)
