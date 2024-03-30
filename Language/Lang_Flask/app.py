from flask import *
# script that authenticates, connects to the  endpoint, retrieves results.
import AZ
app = Flask(__name__)
  


# recognizes and categorizes Personally Identifiable Information (PII) entities in its input text, such as Social Security Numbers, 
# bank account information, credit card numbers, and more.
@app.route('/extract_pii/text',methods = ['POST'])
def text_extract_pii():    
    # input to text_analyzer should passed as a list of documents(text to be read).
    values = dict(request.form)
    
        
    ls = {}
    for i,j  in values.items():
        
         
        result = AZ.text_extract_pii([j])
        ls[i] = result
    return ls

# determines the main talking points in its input text. For example,  for the input text 
# "The food was delicious and there were wonderful staff", the API returns: "food" and "wonderful staff".
@app.route('/extract_key_phrases/text',methods = ['POST'])
def text_extract_key_phrases():    
    values = dict(request.form)

    ls = {}
    for i,j  in values.items():
        result = AZ.extract_key_phrases_text([j])
        ls[i] = result
    return ls


@app.route('/recognize_linked_entities/text',methods = ['POST'])
def text_recognize_linked_entities():    
    values = dict(request.form)

    ls = {}
    for i,j  in values.items():
        result = AZ.recognize_linked_entities_text([j])
        ls[i] = result
    return ls



#recognizes and categories entities in its input text as people, places, organizations, date/time, 
# quantities, percentages, currencies, and more.
@app.route('/extract_named_entities/text',methods = ['POST'])
def text_extract_named_entities():    
    values = dict(request.form)

    ls = {}
    for i,j  in values.items():
        result = AZ.recognize_named_entities_text([j])
        ls[i] = result
    return ls


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.2') 


