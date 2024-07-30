import base64

import cv2
import numpy as np

from django.http import HttpResponse







def img_to_base64(img_array):
    # 传入图片为RGB格式numpy矩阵，传出的base64也是通过RGB的编码
    # img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR) #RGB2BGR，用于cv2编码
    encode_image = cv2.imencode(".jpg", img_array)[1]  # 用cv2压缩/编码，转为一维数组
    byte_data = encode_image.tobytes()  # 转换为二进制
    base64_str = base64.b64encode(byte_data).decode("ascii")  # 转换为base64
    return base64_str


def base64_to_image(base64_code):
    """
    将base64编码解析成opencv可用图片
    base64_code: base64编码后数据
    Returns: cv2图像，numpy.ndarray
    """
    # base64解码
    num_padding = 4 - (len(base64_code) % 4)
    if num_padding < 4:
        base64_code += "=" * num_padding
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.fromstring(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    # faceRecognition(img_array)
    return img


def show(img):
    cv2.imshow('000', img)
    cv2.waitKey(0)
    # cv.destroyAllWindows()
    print("22222222222222222222222222")



