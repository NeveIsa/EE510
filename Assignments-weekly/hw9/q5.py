import numpy as np
import pandas as pd

ur = pd.read_csv('Annual_unemployment_rates.csv')
gdp_change = pd.read_csv('GDP_change.csv')

#ur['CHANGE'] = ur.iloc[:,1] - ur.iloc[:,1].shift(1)


ur["RATE_CHANGE"] = ur.RATE.diff()

all_data = ur

all_data = all_data.merge(gdp_change,  on='YEAR',how='outer').dropna()

delta_u = all_data.RATE_CHANGE
delta_G = all_data.GDP_CHANGE


D = np.array([[1]*len(delta_u),delta_u]).T
#print(D)

best_params = np.linalg.inv(D.T @ D) @ D.T @ delta_G
print(best_params)
