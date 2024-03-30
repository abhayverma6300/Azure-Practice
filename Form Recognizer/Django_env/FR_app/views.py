from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 

# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import FR_



@csrf_exempt
def url(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        #print(items)
        dict_ = {}
        # iterate through key value pairs in request.POST
        for key, value in items.items():
            #print(value)
            result = FR_.analyze_document_from_url(value)
            dict = {}
            for analyzed_document in result.documents:
                dict.update({"modelID": result.model_id})
                dict.update({"Document has confidence":analyzed_document.confidence})
                for name, field in analyzed_document.fields.items():
                    dict.update({name : f'{field.value}, {field.confidence}'})
            dict_[key] = dict
    
    return JsonResponse(dict_, safe = False)

@csrf_exempt
def local(request):
    if request.method == "POST": 
        # request.POST has form data given to upi from a post method. --> <<QueryDict:{'k': [value in one form field],'key': [2nd form field]}
        items = request.POST 
        #print(items)
        dict_ = {}
        # iterate through key value pairs in request.POST
        for key, value in items.items():
            #print(value)
            result = FR_.analyze_document_local(value)
            dict = {}
            for analyzed_document in result.documents:
                dict.update({"modelID": result.model_id})
                dict.update({"Document has confidence":analyzed_document.confidence})
                for name, field in analyzed_document.fields.items():
                    dict.update({name : f'{field.value}, {field.confidence}'})
            dict_[key] = dict
    
    return JsonResponse(dict_, safe = False)


# python manage.py runserver
#python manage.py startapp appname

