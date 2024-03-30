"""Recognize custom entities from text documents using Azure Text Analytics.

This script utilizes Azure Text Analytics to recognize custom entities from text documents.

Make sure to have the relevant Azure services set up and the necessary environment variables configured:
- TEXT_ANALYTICS_KEY: Azure Text Analytics subscription key.
- TEXT_ANALYTICS_ENDPOINT: Azure Text Analytics endpoint URL.

Install the required packages:
    pip install azure-ai-textanalytics

For more information on Azure Text Analytics, visit:
https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/

"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Get secrets from environment variables
endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
key = os.getenv("TEXT_ANALYTICS_KEY")
project_name = os.getenv("CUSTOM_ENTITY_RECOGNIZER_PROJECT_NAME")
deployment_name = os.getenv("CUSTOM_ENTITY_RECOGNIZER_DEPLOYMENT_NAME")

# Initialize TextAnalyticsClient
text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

def recognize_custom_entities_local(document):
    """Recognize custom entities from a local text document.

    Parameters:
    ----------
    document : str
        Path to the local text document to be analyzed.

    Returns:
    -------
    dict
        A dictionary containing recognized custom entities and related information.
    """
    path_to_sample_document = document    

    with open(path_to_sample_document) as fd:
        document = [fd.read()]

    poller = text_analytics_client.begin_recognize_custom_entities(
        document,
        project_name=project_name,
        deployment_name=deployment_name
    )

    document_results = poller.result()
    dict_ = {}

    for custom_entities_result in document_results:
        ls = []
        if custom_entities_result.kind == "CustomEntityRecognition":
            
            for entity in custom_entities_result.entities:
                entity_ = {}
                entity_['Entity'] = entity.text
                entity_['Category'] = entity.category
                entity_['Confidence_score'] = entity.confidence_score

                ls.append(entity_)
            dict_['Entities'] = ls
        elif custom_entities_result.is_error is True:
            error = {}
            error['error_code'] = custom_entities_result.error.code
            error['message'] = custom_entities_result.error.message
            
            dict_['Errors'] = error
    
    return dict_
