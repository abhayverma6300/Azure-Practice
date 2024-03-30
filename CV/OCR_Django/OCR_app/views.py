from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 

# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import AZ



@csrf_exempt
def url(request):
    if request.method == "POST": 
        # request.POST has form data given to api from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        #print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.analyze_image_from_url(j)
            ls[i] = result
        
    
    return JsonResponse(ls, safe = False)

@csrf_exempt
def local(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.analyze_image_local(j)
            ls[i] = result
    
    return JsonResponse(ls, safe = False)   

