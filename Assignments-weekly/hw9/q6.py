import numpy as np


MaxLum = eval('[14.8 14.8 14.8 15.1 14.7 14.4 14.7 14.6 14.3 14.3 14.4 14.3 13.8 14.1 14.0 13.9 13.6 13.4 13.8 13.4 13.4 13.0 12.2 11.4 11.2]'.replace(' ',','))
MinLum = eval('[16.1 16.4 16.4 16.3 15.6 15.7 15.9 16.1 15.3 15.5 15.4 15.2 14.8 14.8 14.8 15.2 14.7 14.6 14.8 14.4 14.3 14.6 14.1 12.8 12.1]'.replace(' ',','))
T = eval('[1.25336 1.6637 1.762 1.87502 2.17352 2.913 3.501 4.2897 4.547 4.9866 5.311 5.323 6.2926 6.65 7.483 8.397 10.336 11.645 12.417 13.08 13.47 16.75 31.94 65.8 127]'.replace(' ',','))

logT = np.log(T)

A = np.array([[1]*len(logT),logT]).T


MAX_params = np.linalg.inv(A.T @ A) @ A.T @ MaxLum
MIN_params = np.linalg.inv(A.T @ A) @ A.T @ MinLum

print('MAX Params->',MAX_params)
print('Error in MaxLum Prediction->', np.linalg.norm(A@MAX_params - MaxLum))
print('MIN Params->',MIN_params)
print('Error in MinLum Prediction->', np.linalg.norm(A@MIN_params - MinLum))




import matplotlib.pyplot as plt
import seaborn as sns

xx = [0,7]
testx=np.array([[1,1],xx]).T
ymaxlum = testx @ MAX_params
yminlum = testx @ MIN_params


sns.scatterplot(logT,MinLum)
plt.plot(xx,yminlum,color='orange')
plt.title('log(Timeperiod) vs Minimum Lumination')
plt.savefig('MinLum.png')


sns.scatterplot(logT,MaxLum)
plt.plot(xx,ymaxlum,color='orange')
plt.title('log(Timeperiod) vs Maximum Lumination')
plt.savefig('MaxLum.png')
