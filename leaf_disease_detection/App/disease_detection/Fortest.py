from App.views import *
from App.disease_detection.apple_leaf_disease_detection import apple_leaf_disease_detection
import cv2
img=cv2.imread('../datasets/22.jpg')
results=apple_leaf_disease_detection(img)
