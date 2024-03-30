"""Analyze user query for intents and entities using Azure CLU.

This script requires the client library 'azure-ai-language-conversations' to be installed.
    TRY : pip install azure-ai-language-conversations --pre
"""

# import libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

# get secrets from environment variables
clu_endpoint = os.getenv("CLU_ENDPOINT")
clu_key = os.getenv("CLU_KEY")
project_name = os.getenv("CLU_PROJECT_NAME")
deployment_name = os.getenv("CLU_DEPLOYMENT_NAME")

# analyze query
def get_clu_results(query):
    """Takes a user query and gives it to CLU analysis client

    Parameters:
    ----------
        query : str
            The string the user want to be analyzed by CLU
    
    Returns:
    -------
        dict_ : dict
            A dictionary containing the results obtained for the particular 
            input.
    """
    client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))

    with client:        
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            }
        )
    
    # get result
    dict_ = {}
    dict_['query'] = result["result"]["query"]
    dict_['project kind'] = result["result"]["prediction"]["projectKind"]
    dict_['top_intent'] = result["result"]["prediction"]["topIntent"]
    dict_['category'] = result["result"]["prediction"]["intents"][0]["category"]
    dict_['confidence score'] = result["result"]["prediction"]["intents"][0]["confidenceScore"]
    ls = []

    for entity in result["result"]["prediction"]["entities"]:
        entity_ = {}
        entity_['category'] = entity["category"]
        entity_['text'] = entity['text']
        entity_['confidence score'] = entity['confidenceScore']

        if "resolutions" in entity:
            resolutions = []
            print("resolutions")
            for resolution in entity["resolutions"]:
                res = {}
                res['kind'] = resolution['resolutionKind']
                res['value'] = resolution['value']
                resolutions.append(res)
            entity_['resolutions'] = resolutions
        
        if "extraInformation" in entity:
            extra = []
            
            for data in entity["extraInformation"]:
                extra_inf = {}
                extra_inf['extra Information kind'] = data['extraInformationKind']
                
                if data["extraInformationKind"] == "ListKey":
                    extra_inf['List key'] = data['key']
                    print("key: {}".format(data["key"]))
                if data["extraInformationKind"] == "EntitySubtype":
                    extra_inf['value'] = data['value']
                    print("value: {}".format(data["value"]))
                extra.append(extra_inf)
            entity_['extraInformation'] = extra
        ls.append(entity_)
    dict_['entities'] = ls

    return dict_
