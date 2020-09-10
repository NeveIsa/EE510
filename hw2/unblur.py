import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

img = loadmat('blurryimage.mat')['blurryimage']
print('IMG DATATYPE:',type(img))


# extend image by inserting a black boundary box
hborder = np.array([[0]*64])
vborder = np.array([[0]*66])
img=np.concatenate((img,hborder),axis=0)
img=np.concatenate((hborder,img),axis=0)
img=np.concatenate((img,vborder.T),axis=1)
img=np.concatenate((vborder.T,img),axis=1)


print('IMG SHAPE:',img.shape)


plt.imshow(img,cmap='gray')
plt.show()



