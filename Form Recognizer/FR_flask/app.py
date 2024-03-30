from flask import *
import AZ

app = Flask(__name__)
  

@app.route('/url',methods = ['GET','POST'])
def url():
    values = dict(request.form)
    
    
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_document_from_url(j)
        
        ls[i] = result
    return ls

@app.route('/local',methods = ['POST'])
def local():    
    values = dict(request.form)    
    
    ls = {}
    for i,j  in values.items():
        result = AZ.analyze_document_local(j)
        
        ls[i] = result
    return ls

if __name__ == '__main__':
    app.run(debug=True) 