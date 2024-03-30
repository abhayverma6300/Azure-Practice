"""Perform text analysis using Azure Text Analytics.

This script utilizes Azure Text Analytics for various text analysis tasks, including extracting Personally Identifiable Information (PII), key phrases, named entities, and linked entities.

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
credential = AzureKeyCredential(os.getenv("TEXT_ANALYTICS_KEY"))
endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")

# Initialize TextAnalyticsClient
text_analytics_client = TextAnalyticsClient(endpoint, credential)

def text_extract_pii(documents):
    """Extract personally identifiable information (PII) entities from text documents.

    Parameters:
    ----------
    documents : list of str
        List of text documents to be analyzed.

    Returns:
    -------
    dict_ : dict
        A dictionary containing the extracted PII entities and related information.
    """
    response = text_analytics_client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    
    dict_ = {}
    for idx, doc in enumerate(result):
        dict_['Document text: '] = documents[idx]
        dict_['Redacted document text'] = doc.redacted_text
        ls = []
        for entity in doc.entities:
            dict_entities = {}
            dict_entities["...Entity"] = entity.text
            dict_entities["......Category"] = entity.category
            dict_entities["......Confidence Score"] = entity.confidence_score
            dict_entities['......Offset'] = entity.offset
            ls.append(dict_entities)
        dict_['Entities'] = ls
    return dict_

def extract_key_phrases_text(documents):
    """Extract key phrases from text documents.

    Parameters:
    ----------
    documents : list of str
        List of text documents to be analyzed.

    Returns:
    -------
    lst_of_key_phrases : list
        A list of key phrases extracted from the documents.
    """
    response = text_analytics_client.extract_key_phrases(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    lst_of_key_phrases = []
    for doc in result:
        lst_of_key_phrases.append(doc.key_phrases)
    return lst_of_key_phrases

def recognize_linked_entities_text(documents):
    """Recognize linked entities from text documents.

    Parameters:
    ----------
    documents : list of str
        List of text documents to be analyzed.

    Returns:
    -------
    list
        A list of dictionaries containing recognized linked entities and related information.
    """
    response = text_analytics_client.recognize_linked_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    ls = []
    for doc in result:
        for entity in doc.entities:
            dict_entities = {}
            dict_entities["Entity"]  = entity.name
            dict_entities["...URL"]  = entity.url
            dict_entities["...Data Source"] =entity.data_source
            matches_ = []
            for match in entity.matches:
                matches = {}
                matches["......Entity match text"] = match.text
                matches["......Confidence Score"] = match.confidence_score
                matches["......Offset"] = match.offset
                matches_.append(matches)
            dict_entities['...Entity matches'] = matches_
            ls.append(dict_entities)
    return ls

def recognize_named_entities_text(documents):
    """Recognize named entities from text documents.

    Parameters:
    ----------
    documents : list of str
        List of text documents to be analyzed.

    Returns:
    -------
    list
        A list of dictionaries containing recognized named entities and related information.
    """
    response = text_analytics_client.recognize_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    ls = []
    for doc in result:
        for entity in doc.entities:
            entity_ = {}
            entity_["Entity"]  =entity.text
            entity_["...Category"] = entity.category
            entity_["...Confidence Score"] = entity.confidence_score
            entity_["...Offset"]  = entity.offset
            ls.append(entity_)
    return ls
