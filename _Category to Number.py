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

# List with labels (category)
y_lab = df.pop('label')
# Vocabulary (only one category in list)
E = []
# List with indexes 
y = []

for x in y_lab:
    if not (x in E):
        E = E +[x]
        print(E.index(x),x)
        
    y = y + [E.index(x)]
	
print('----')
#print(y)

