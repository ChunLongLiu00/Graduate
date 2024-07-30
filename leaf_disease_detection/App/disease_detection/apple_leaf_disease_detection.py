from PIL import Image
from ultralytics import YOLO
import cv2

def apple_leaf_disease_detection(img):
    model = YOLO('D:\\Python\\PythonProject\\leaf_disease_detection\\App\\disease_detection\\runs\detect\\best001.pt')
    results = model(img)  # results list
    im_array = results[0].plot()
    im = Image.fromarray(im_array[..., ::-1])
    return im_array

