"""Predict image contents using Azure Custom Vision.

This script utilizes Azure Custom Vision to predict image contents either from a URL or from a local file.

Ensure that the necessary Azure services are set up and the relevant environment variables are configured:
- CUSTOM_VISION_ENDPOINT: Azure Custom Vision endpoint URL.
- CUSTOM_VISION_PREDICTION_KEY: Azure Custom Vision prediction key.
- CUSTOM_VISION_PROJECT_ID: Azure Custom Vision project ID.
- CUSTOM_VISION_ITERATION_NAME: Name of the iteration to use for prediction.

Install the required packages:
    pip install azure-cognitiveservices-vision-customvision msrest

For more information on Azure Custom Vision, visit:
https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/

"""

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

def predict_image_from_local(image_path):
    """Predict image contents from a local file using Azure Custom Vision.

    Parameters:
    ----------
    image_path : str
        The path to the local image file.

    Returns:
    -------
    dict
        The prediction results.
    """
    # Fetching keys and endpoints from environment variables
    ENDPOINT = os.getenv("CUSTOM_VISION_ENDPOINT")
    prediction_key = os.getenv("CUSTOM_VISION_PREDICTION_KEY")
    project_id = os.getenv("CUSTOM_VISION_PROJECT_ID")
    publish_iteration_name = os.getenv("CUSTOM_VISION_ITERATION_NAME")

    # Create a predictor object
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

    # Open the image and get prediction results
    with open(image_path, 'rb') as test_data:
        results = predictor.detect_image(project_id, publish_iteration_name, test_data)

    # Format and return the prediction results
    prediction_dict = {}
    for prediction in results.predictions:
        prediction_dict[prediction.tag_name] = "Prediction probability: {0:.2f}% | Bounding box: left={1:.2f}, top={2:.2f}, width={3:.2f}, height={4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height)

    return prediction_dict

def predict_image_from_url(image_url):
    """Predict image contents from a URL using Azure Custom Vision.

    Parameters:
    ----------
    image_url : str
        The URL of the image.

    Returns:
    -------
    dict
        The prediction results.
    """
    # Fetching keys and endpoints from environment variables
    ENDPOINT = os.getenv("CUSTOM_VISION_ENDPOINT")
    prediction_key = os.getenv("CUSTOM_VISION_PREDICTION_KEY")
    project_id = os.getenv("CUSTOM_VISION_PROJECT_ID")
    publish_iteration_name = os.getenv("CUSTOM_VISION_ITERATION_NAME")

    # Create a predictor object
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

    # Get prediction results from the image URL
    results = predictor.detect_image_url(project_id, publish_iteration_name, url=image_url)

    # Format and return the prediction results
    prediction_dict = {}
    for prediction in results.predictions:
        prediction_dict[prediction.tag_name] = "Prediction probability: {0:.2f}% | Bounding box: left={1:.2f}, top={2:.2f}, width={3:.2f}, height={4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height)

    return prediction_dict
