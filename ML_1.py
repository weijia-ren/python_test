
#%% [markdown]
# ## This codes give the basic models in sklearn

# ###   1. The bike usage prediction project 

#%%
from sklearn.linear_model import LinearRegression
import pandas as pd
train = pd.read_csv("bike_train.csv")
test = pd.read_csv("bike_test.csv")
submit = pd.read_csv("bike_sample_submit.csv")
train.head(5)

#%%
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)
train.head(5)
#%%
y_train = train.pop('y')
reg = LinearRegression()
reg.fit(train, y_train)
y_pred = reg.predict(test)

submit['y'] = y_pred
submit.head(5)
#%%
submit.to_csv('my_LR_prediction.csv', index=False)
