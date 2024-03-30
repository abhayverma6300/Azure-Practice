"""Analyze images using Azure Computer Vision.

This script utilizes Azure Computer Vision to analyze images either from a URL or from a local file.

Ensure that the necessary Azure services are set up and the relevant environment variables are configured:
- AZURE_COGNITIVE_SUBSCRIPTION_KEY: Azure Cognitive Services subscription key.
- AZURE_COGNITIVE_ENDPOINT: Azure Cognitive Services endpoint URL.

Install the required packages:
    pip install azure-cognitiveservices-vision-computervision msrest

For more information on Azure Computer Vision, visit:
https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/

"""

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import os
import time

def analyze_image_from_url(image_url):
    """Analyze an image from a URL using Azure Computer Vision.

    Parameters:
    ----------
    image_url : str
        The URL of the image to be analyzed.

    Returns:
    -------
    dict
        The extracted text and its bounding box.
    """
    # Fetching keys and endpoints from environment variables
    subscription_key = os.getenv("AZURE_COGNITIVE_SUBSCRIPTION_KEY")
    endpoint = os.getenv("AZURE_COGNITIVE_ENDPOINT")

    # Check if environment variables are set
    if not all([subscription_key, endpoint]):
        raise ValueError("Please set both AZURE_COGNITIVE_SUBSCRIPTION_KEY and AZURE_COGNITIVE_ENDPOINT environment variables.")

    # Authenticate with the Computer Vision service
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Call API with URL and wait for retrieval of the results
    read_response = computervision_client.read(image_url, raw=True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Extract the detected text and its bounding box
    results = {}
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:            
            for line in text_result.lines:
                results[line.text] = line.bounding_box
    return results

def analyze_image_local(image_path):
    """Analyze a local image using Azure Computer Vision.

    Parameters:
    ----------
    image_path : str
        The path to the local image to be analyzed.

    Returns:
    -------
    dict
        The extracted text and its bounding box.
    """
    # Fetching keys and endpoints from environment variables
    subscription_key = os.getenv("AZURE_COGNITIVE_SUBSCRIPTION_KEY")
    endpoint = os.getenv("AZURE_COGNITIVE_ENDPOINT")

    # Check if environment variables are set
    if not all([subscription_key, endpoint]):
        raise ValueError("Please set both AZURE_COGNITIVE_SUBSCRIPTION_KEY and AZURE_COGNITIVE_ENDPOINT environment variables.")

    # Authenticate with the Computer Vision service
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Open the image
    with open(image_path, "rb") as image_file:
        # Call API with image and wait for retrieval of the results
        read_response = computervision_client.read_in_stream(image_file, raw=True)
        read_operation_location = read_response.headers["Operation-Location"]
        operation_id = read_operation_location.split("/")[-1]

        while True:
            read_result = computervision_client.get_read_result(operation_id)
            if read_result.status.lower() not in ['notStarted', 'running']:
                break
            time.sleep(10)

    # Extract the detected text and its bounding box
    results = {}
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                results[line.text] = line.bounding_box
    return results
