"""FastAPI app for Azure CLU endpoint.

This script requires FastAPI to be installed and imported.

This script requires the AZ module to be imported.

Functions:
    * hit_clu: Take a form with key 'document' and value the text you want to analyze using CLU
        Returns a dictionary of results obtained from the CLU endpoint.
"""

# Import libraries
from fastapi import FastAPI, Form
from typing import Dict
import AZ

app = FastAPI()

@app.post('/clu')
async def hit_clu(document: str = Form(...)) -> Dict:
    """takes a form input and gives it to the CLU endpoint.

    Parameters:
    ----------
        document : str
            A form key value pair, where key is 'document' and value is the text the user wants to get analyzed.
    
    Returns:
    -------
        A dictionary of with key 'document' and values is the results obtained from the endpoint for the text.
    
    
    """

    print(document)
    values = {"document": document}
    ls = {}
    for i, j in values.items():
        result = AZ.get_clu_results(j)
        ls[i] = result
    return ls

