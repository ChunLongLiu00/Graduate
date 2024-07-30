import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from App.disease_detection.apple_leaf_disease_detection import apple_leaf_disease_detection
from App.disease_detection.apple_leaf_disease_classify import apple_leaf_disease_classify
from App.disease_detection.test_Classify_by_url import apple_leaf_disease_classify
import json
from zhipuai import ZhipuAI
from App.consumers import base64_to_image,img_to_base64
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def hello(request):
    pass
    #返回response
    return HttpResponse("hello Django!")
@csrf_exempt
def detect(request):
    if request.method == 'POST':
        # jsonData = json.loads(request.body)
        # img1_base64 = jsonData["base64Code"]
        img1_base64=request.POST.get('base64Code')
        print(img1_base64)
        # # id = request.POST.get('id')
        img1=base64_to_image(img1_base64)
        img1_array=apple_leaf_disease_detection(img1)
        base64Code=img_to_base64(img1_array)
        result = {"base64Code": ''}
        result["base64Code"]=base64Code
        return HttpResponse(json.dumps(result))
@csrf_exempt
def classify(request):
    if request.method == 'POST':
        # jsonData = json.loads(request.body)
        # img1_base64 = jsonData["base64Code"]
        img1_base64=request.POST.get('base64Code')
        print(img1_base64)
        # # id = request.POST.get('id')
        img1=base64_to_image(img1_base64)
        im=np.array(img1)
        img1_array,classify_result=apple_leaf_disease_classify(im)
        base64Code=img_to_base64(img1_array)
        result = {"base64Code": '',"classify_result": ''}
        result["base64Code"]=base64Code
        result["classify_result"]=classify_result
        return HttpResponse(json.dumps(result))
@csrf_exempt
def glmapi(request):
    client=ZhipuAI(api_key="017d0bb8785afe4469d14404d74d04a1.JN6dZBkpg4aacFCJ")
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        messages = jsonData['messages']
        # print(messages)
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=messages,
        )
        return HttpResponse(response.choices[0].message.content)
@csrf_exempt
def testClassify(request):
    if request.method == 'POST':
        # jsonData = json.loads(request.body)
        # img1_base64 = jsonData["base64Code"]
        imgurl=request.POST.get('imgurl')

        img1_array,classify_result=apple_leaf_disease_classify(imgurl)
        base64Code=img_to_base64(img1_array)
        result = {"base64Code": '',"classify_result": ''}
        result["base64Code"]=base64Code
        result["classify_result"]=classify_result
        return HttpResponse(json.dumps(result))