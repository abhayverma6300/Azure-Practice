from flask import *
import AZ
app = Flask(__name__)


@app.route('/custom_ner_local',methods = ['POST'])
def recognize_custom_entities_local():
   
    
    values = dict(request.form)
    
        
    ls = {}
    for key,value in values.items():        
         
        result = AZ.recognize_custom_entities_local(value)
        ls[key] = result
    return ls
    
    


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.2') 