

import os
from flask import Flask, jsonify, request
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username='03d8c66b-071e-48d6-86ec-c5a85269d8fc',
    password='eGLqwxU4YtDK')

classifier_id = 'e55175x249-nlc-51054'

#comment_text = str(input("What comment do you want to analyze: "))

#while comment_text != "":
#  analysis_results = natural_language_classifier.classify(classifier_id, comment_text)
#  if "classes" in analysis_results.keys():
#    for predicted_class in analysis_results["classes"]:
#      print (predicted_class['class_name'], " - ", predicted_class['confidence'])
#    comment_text = str(input("What comment do you want to analyze: "))

#comment_text = "I love coffee made in my Keurig machine!"

#analysis_results = natural_language_classifier.classify(classifier_id, comment_text)

#if "classes" in analysis_results.keys():
 # for predicted_class in analysis_results["classes"]:
 #   print (predicted_class['class_name'], " - ", predicted_class['confidence'])
#print(analysis_results)

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def Analyze():
    comment_text = request.form['text']
    analysis_results = {}
    
    if comment_text != "":
        analysis_results = natural_language_classifier.classify(classifier_id, comment_text)
        
    return jsonify(analysis_results)
   
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
