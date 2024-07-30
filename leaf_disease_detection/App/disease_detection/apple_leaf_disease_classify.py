from PIL import Image
from ultralytics import YOLO
import numpy as np
def apple_leaf_disease_classify(img):
    model = YOLO('D:\\Python\\PythonProject\\leaf_disease_detection\\App\\disease_detection\\runs\\classify\\best.pt')
    results = model(img)  # results list
    im_array = results[0].plot()
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    classify_result=names_dict[np.argmax(probs)]
    im = Image.fromarray(im_array[..., ::-1])
    return im_array, classify_result