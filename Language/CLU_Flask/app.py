"""Flask API app for Azure CLU endpoint

This script requires flask to be installed

This script requires the AZ module to be imported.


Functions :
    * hit_clu : takes a HTTP request from user and returns a dictionary
        of results obtained from CLU endpoint.

"""


# import modules
from flask import *
import AZ
app = Flask(__name__)


@app.route('/clu',methods = ['POST'])
def hit_clu():
    """Take an HTTP form request from user,get results from the CLU endpoint.

    Returns
    -------
    dictionary
        A dictionary of results obtained for each form value.
        key : the form key given by the user
        value : the analysis result of the form value, returned by get_clu_results 
    
    """
    # Take the HTTP request form values.  FORM -> { key for a particular text : the text to be analyzed}
    values = dict(request.form)   
    
    # a dictionary that will store the keys from the form and the results obtained from analyzing text.
    ls = {}
    for i,j  in values.items():
        
        # get the result from the endpoint for a particular form value.
        result = AZ.get_clu_results(j)
        ls[i] = result

    return ls
      


if __name__ == "__main__":
    app.run(debug=True, port=11000, host='127.0.0.2') 