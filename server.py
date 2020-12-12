from flask import Flask
from elasticsearch import Elasticsearch
from flask import render_template, request, jsonify, redirect, url_for
import json
import re

app = Flask(__name__) 
es = Elasticsearch()
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
alert = 0
default_size = 10
@app.route('/')
def home():
    return render_template("index.html", alert = alert, size = default_size)

@app.route('/search', methods=['POST'])
def search():
    # querytext is user_request from frontend
    querytext = request.form['querytext']

    # input checking
    # no special char and querytext should not only contain whitespace
    if((regex.search(querytext) == None) and (querytext.strip())):
      alert = 0 
      querytext += "~"
    else:
      alert = 1
      return redirect(url_for('home', alert = alert))
    
    #use query_string to take querytext as key words, fuzziness is a feature of ElasticSearch to compare the edit distance between data stored in database and key words.
    query_body = {
      "from" : 0, "size" : 5,
      "query": {
        "query_string": {
          "query": querytext,
          "fuzziness" : "auto:0,10"
        }
      }
    }
    result = es.search(index="test-index", body=query_body)
    all_hits = result['hits']['hits']

    #divide results into different lists according to the categories 
    faculty_emails = []
    faculty_names = []
    texts = []
    faculty_urls = []
    for doc in all_hits:
      faculty_emails.append(doc["_source"]["faculty_email"])
      faculty_names.append(doc["_source"]["faculty_name"])
      faculty_urls.append(doc["_source"]["faculty_url"])
      texts.append(doc["_source"]["text"])
    docs = list(zip(faculty_emails, faculty_names, faculty_urls,texts))
    return render_template("display.html", doc = docs)



if __name__ == '__main__':
   app.run(debug = True)
