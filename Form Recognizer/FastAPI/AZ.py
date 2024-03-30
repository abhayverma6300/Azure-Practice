"""Analyze documents using Azure Form Recognizer.

This script utilizes Azure Form Recognizer to analyze documents either from a URL or from a local file.

Ensure that the necessary Azure services are set up and the relevant environment variables are configured:
- AZURE_FORM_RECOGNIZER_ENDPOINT: Azure Form Recognizer endpoint URL.
- AZURE_FORM_RECOGNIZER_SUBSCRIPTION_KEY: Azure Form Recognizer subscription key.

Install the required packages:
    pip install azure-ai-formrecognizer

For more information on Azure Form Recognizer, visit:
https://azure.microsoft.com/en-us/services/form-recognizer/

"""

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

def analyze_document_from_url(address):
    """Analyze a document from a URL using Azure Form Recognizer.

    Parameters:
    ----------
    address : str
        The URL of the document to be analyzed.

    Returns:
    -------
    dict
        A dictionary containing the analysis results.
    """
    # Fetching keys and endpoint from environment variables
    endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
    subscription_key = os.getenv("AZURE_FORM_RECOGNIZER_SUBSCRIPTION_KEY")

    # Check if environment variables are set
    if not all([endpoint, subscription_key]):
        raise ValueError("Please set both AZURE_FORM_RECOGNIZER_ENDPOINT and AZURE_FORM_RECOGNIZER_SUBSCRIPTION_KEY environment variables.")

    # Create the DocumentAnalysisClient with AzureKeyCredential
    credential = AzureKeyCredential(subscription_key)
    document_analysis_client = DocumentAnalysisClient(endpoint, credential)

    model_id = "b223ff5f-87e4-42b4-a98c-509e79f9c18a"

    document_url = address
    poller = document_analysis_client.begin_analyze_document_from_url(model_id=model_id, document_url=document_url)
    result = poller.result()

    result_dict = {}
    for analyzed_document in result.documents:
        result_dict["modelID"] = result.model_id
        result_dict["Document has confidence"] = analyzed_document.confidence
        for name, field in analyzed_document.fields.items():
            result_dict[name] = f"{field.value}, {field.confidence}"

    return result_dict

def analyze_document_local(address):
    """Analyze a local document using Azure Form Recognizer.

    Parameters:
    ----------
    address : str
        The path to the local document to be analyzed.

    Returns:
    -------
    dict
        A dictionary containing the analysis results.
    """
    # Fetching keys and endpoint from environment variables
    endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
    subscription_key = os.getenv("AZURE_FORM_RECOGNIZER_SUBSCRIPTION_KEY")

    # Check if environment variables are set
    if not all([endpoint, subscription_key]):
        raise ValueError("Please set both AZURE_FORM_RECOGNIZER_ENDPOINT and AZURE_FORM_RECOGNIZER_SUBSCRIPTION_KEY environment variables.")

    # Create the DocumentAnalysisClient with AzureKeyCredential
    credential = AzureKeyCredential(subscription_key)
    document_analysis_client = DocumentAnalysisClient(endpoint, credential)

    model_id = "b223ff5f-87e4-42b4-a98c-509e79f9c18a"

    with open(address, "rb") as fd:
        document = fd.read()

    poller = document_analysis_client.begin_analyze_document(model_id=model_id, document=document)
    result = poller.result()

    result_dict = {}
    for analyzed_document in result.documents:
        result_dict["modelID"] = result.model_id
        result_dict["Document has confidence"] = analyzed_document.confidence
        for name, field in analyzed_document.fields.items():
            result_dict[name] = f"{field.value}, {field.confidence}"

    return result_dict

if __name__ == '__main__':
    analyze_document_from_url("https://github.com/Azure/azure-sdk-for-net/issues/28217")
