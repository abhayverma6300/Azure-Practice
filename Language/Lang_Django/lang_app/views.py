from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 

# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import AZ


@csrf_exempt
def text_extract_pii(request):
    if request.method == "POST": 
        # request.POST has form data given to api from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        #print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.text_extract_pii([j])
            ls[i] = result
        
    
    return JsonResponse(ls, safe = False)

@csrf_exempt
def text_extract_key_phrases(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.extract_key_phrases_text([j])
            ls[i] = result
    
    return JsonResponse(ls, safe = False)  



@csrf_exempt
def text_recognize_linked_entities(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.recognize_linked_entities_text([j])
            ls[i] = result
    
    return JsonResponse(ls, safe = False)  



@csrf_exempt
def text_extract_named_entities(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        print(items)
        ls = {}
        for i,j  in items.items():
            result = AZ.recognize_named_entities_text([j])
            ls[i] = result
    
    return JsonResponse(ls, safe = False) 


