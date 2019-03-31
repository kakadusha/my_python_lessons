'''
По мотивам Костиного задания, вроде бы, https://github.com/ckorikov/python-bar-review
'''

import pandas as pd

df = pd.read_csv("https://github.com/rudeboybert/JSE_OkCupid/raw/master/profiles.csv.zip")
df.head(1).T