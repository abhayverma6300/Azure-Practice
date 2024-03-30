from flask import *
# script that authenticates, connects to the  endpoint, retrieves results.
import AZ
app = Flask(__name__)
  

@app.route('/url',methods = ['POST'])
def url():    
    values = dict(request.form)
    #print(values)  
        
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_image_from_url(j)
        ls[i] = result
    return ls

@app.route('/local',methods = ['POST'])
def local():    
    values = dict(request.form)
    #print(values)
        
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_image_local(j)
        ls[i] = result
    return ls
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.2') 