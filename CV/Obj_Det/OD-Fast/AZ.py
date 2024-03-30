from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os

# Fetch environment variables
ENDPOINT = os.environ.get("CUSTOM_VISION_ENDPOINT")
prediction_key = os.environ.get("CUSTOM_VISION_PREDICTION_KEY")
publish_iteration_name = os.environ.get("CUSTOM_VISION_PUBLISH_ITERATION_NAME")
project_id = os.environ.get("CUSTOM_VISION_PROJECT_ID")

# Check if any of the required environment variables are missing
if None in [ENDPOINT, prediction_key, publish_iteration_name, project_id]:
    raise ValueError("Please set all required environment variables.")

# Initialize the prediction client
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

def main_local(address):
    # Open the sample image and get back the prediction results.
    with open(address, 'rb') as test_data:
        results = predictor.detect_image(project_id, publish_iteration_name, test_data)

    # Display the results.
    result_dict = {}
    for prediction in results.predictions:
        result_dict[prediction.tag_name] = f"pred_prob- {prediction.probability * 100:.2f}% bbox.left = {prediction.bounding_box.left:.2f}, bbox.top = {prediction.bounding_box.top:.2f}, bbox.width = {prediction.bounding_box.width:.2f}, bbox.height = {prediction.bounding_box.height:.2f}"

    return result_dict

def main_url(address):
    results = predictor.detect_image_url(project_id, publish_iteration_name, url=address)

    result_dict = {}
    for prediction in results.predictions:
        result_dict[prediction.tag_name] = f"pred_prob- {prediction.probability * 100:.2f}% bbox.left = {prediction.bounding_box.left:.2f}, bbox.top = {prediction.bounding_box.top:.2f}, bbox.width = {prediction.bounding_box.width:.2f}, bbox.height = {prediction.bounding_box.height:.2f}"

    return result_dict
