"""Django app for using Conversational Language Understanding endpoint

This script allows the user create views for the Django application
    Views are python functions that take HTTP requests and return HTTP responses.

This file requires the AZ module in the same directory as this file and imported.

    AZ module contains all the necessary credentials to use the CLU resource.
    Demonstrates how to analyze user query for intents and entities using
    a conversation project.

This file contains the following functions:

    * hit_clu - Returns a dictionary as a Json Response.

"""


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 

# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt

from . import AZ


@csrf_exempt
def hit_clu(request):
    """Takes a HTTP POST request,give it to get_clu_results() function from AZ module.

    Parameters
    ----------
    request : request
        An HTTP post request that has values as form-data.

    Returns
    -------
    JsonResponse
        A dictionary containing the results obtained from the CLU endpoint.
    
    """
    
    if request.method == "POST": 
        # request.POST has form data given to api from a post method. --> 
        # <<QueryDict:{'key1': [value in one form field],'key2': [value in 2nd form field]}
        items = request.POST 
        
        # a dictionary to store the results as key value pairs. Key being the form-key
        # and value being the output returned by CLU endpoint.
        ls = {}
        for i,j  in items.items():
            result = AZ.get_clu_results(j)
            ls[i] = result
        
    
    return JsonResponse(ls, safe = False)