"""Extract information from text using Azure Text Analytics.

This script utilizes Azure Text Analytics for extracting various types of information from text, including Personally Identifiable Information (PII), key phrases, named entities, and linked entities.

Make sure to have the relevant Azure services set up and the necessary environment variables configured:
- TEXT_ANALYTICS_KEY: Azure Text Analytics subscription key.
- TEXT_ANALYTICS_ENDPOINT: Azure Text Analytics endpoint URL.

Install the required packages:
    pip install azure-ai-textanalytics fastapi pydantic

For more information on Azure Text Analytics, visit:
https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/

"""

from fastapi import FastAPI
from pydantic import BaseModel
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

app = FastAPI()

class DocumentInput(BaseModel):
    text: str

class DocumentOutput(BaseModel):
    document_text: str
    redacted_text: str
    entities: list

# Get secrets from environment variables
credential = AzureKeyCredential(os.getenv("TEXT_ANALYTICS_KEY"))
endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")

text_analytics_client = TextAnalyticsClient(endpoint, credential)

@app.post("/extract-pii")
def extract_pii(document_input: DocumentInput):
    documents = [document_input.text]
    response = text_analytics_client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    output = []
    for idx, doc in enumerate(result):
        output.append(
            DocumentOutput(
                document_text=documents[idx],
                redacted_text=doc.redacted_text,
                entities=[{
                    "entity": entity.text,
                    "category": entity.category,
                    "confidence_score": entity.confidence_score,
                    "offset": entity.offset
                } for entity in doc.entities]
            )
        )

    return output

@app.post("/extract-key-phrases")
def extract_key_phrases(document_input: DocumentInput):
    documents = [document_input.text]
    response = text_analytics_client.extract_key_phrases(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    output = []
    for doc in result:
        output.append(doc.key_phrases)

    return output

@app.post("/recognize-named-entities")
def recognize_named_entities(document_input: DocumentInput):
    documents = [document_input.text]
    response = text_analytics_client.recognize_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    output = []
    for doc in result:
        entities = [{
            "entity": entity.text,
            "category": entity.category,
            "confidence_score": entity.confidence_score,
            "offset": entity.offset
        } for entity in doc.entities]
        output.append(entities)

    return output

@app.post("/recognize-linked-entities")
def recognize_linked_entities(document_input: DocumentInput):
    documents = [document_input.text]
    response = text_analytics_client.recognize_linked_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    output = []
    for doc in result:
        entities = []
        for entity in doc.entities:
            matches = [{
                "entity_match_text": match.text,
                "confidence_score": match.confidence_score,
                "offset": match.offset
            } for match in entity.matches]
            entity_dict = {
                "entity": entity.name,
                "url": entity.url,
                "data_source": entity.data_source,
                "matches": matches
            }
            entities.append(entity_dict)
        output.append(entities)

    return output
