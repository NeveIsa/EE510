import numpy as np
import scipy.io
import sklearn.decomposition
import matplotlib.pyplot as plt
import seaborn as sns


data = scipy.io.loadmat('data.mat')['data']

pca = sklearn.decomposition.PCA(2)

#print(data)
pca.fit(data)
compressed = pca.transform(data)

print(compressed)

sns.scatterplot(compressed.T[0],compressed.T[1])
#plt.scatter(compressed.T[0],compressed.T[1])
plt.show()
