"""Analyze user query for intents and entities using Azure CLU.

This script requires the client library 'azure-ai-language-conversations' to be installed.
    TRY : pip install azure-ai-language-conversations --pre
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

# Get secrets from environment variables
clu_endpoint = os.environ.get("CLU_ENDPOINT")
clu_key = os.environ.get("CLU_KEY")
project_name = os.environ.get("CLU_PROJECT_NAME")
deployment_name = os.environ.get("CLU_DEPLOYMENT_NAME")

def get_clu_results(query: str):
    """Analyze user query for intents and entities using Azure CLU.

    Parameters:
        query (str): The user query to be analyzed.

    Returns:
        dict: A dictionary containing the analysis results.
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

    # Process and return the result
    analysis_result = {
        "query": result["result"]["query"],
        "project_kind": result["result"]["prediction"]["projectKind"],
        "top_intent": result["result"]["prediction"]["topIntent"],
        "category": result["result"]["prediction"]["intents"][0]["category"],
        "confidence_score": result["result"]["prediction"]["intents"][0]["confidenceScore"],
        "entities": []
    }

    for entity in result["result"]["prediction"]["entities"]:
        entity_info = {
            "category": entity["category"],
            "text": entity["text"],
            "confidence_score": entity["confidenceScore"]
        }

        if "resolutions" in entity:
            entity_info["resolutions"] = [{"kind": resolution["resolutionKind"], "value": resolution["value"]} for resolution in entity["resolutions"]]

        if "extraInformation" in entity:
            entity_info["extra_information"] = [{"kind": data["extraInformationKind"], "value": data["key"] if data["extraInformationKind"] == "ListKey" else data["value"]} for data in entity["extraInformation"]]

        analysis_result["entities"].append(entity_info)

    return analysis_result

if __name__ == "__main__":
    get_clu_results("Distance between Paris and Moscow")
