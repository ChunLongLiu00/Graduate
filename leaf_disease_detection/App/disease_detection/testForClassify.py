import numpy as np

from App.views import *
from App.disease_detection.apple_leaf_disease_classify import apple_leaf_disease_classify
import cv2
img=cv2.imread('../datasets/22.jpg')
img_a=np.array(img)
im = Image.fromarray(img_a[..., ::-1])
im_array,classify=apple_leaf_disease_classify(im)
print(classify)
im = Image.fromarray(im_array[..., ::-1])
im.show()