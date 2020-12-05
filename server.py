from flask import Flask
from elasticsearch import Elasticsearch
from flask import render_template, request, jsonify
import json

app = Flask(__name__) 
es = Elasticsearch()

# user_request = "Data Mining~"

# query_body = {
#   "from" : 0, "size" : 1,
#   "query": {
#     "query_string": {
#       "query": user_request,
#       "fuzziness" : 0
#     }
#   }
# }

# result = es.search(index="test-index", body=query_body)

# all_hits = result['hits']['hits']
# count = 0
# for num, doc in enumerate(all_hits):
#     count += 1
#     print("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
   
#     # Use 'iteritems()` instead of 'items()' if using Python 2
#     for key, value in doc.items():
#         print (key, "-->", value)
   
#     # print a few spaces between each doc for readability
    
#     print ("\n\n")
#     print(count)
#     print ("\n\n")

@app.route('/')
def home():
    # return result
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    querytext = request.form['querytext']
    query_body = {
      "from" : 0, "size" : 5,
      "query": {
        "query_string": {
          "query": querytext,
          "fuzziness" : 0
        }
      }
    }
    result = es.search(index="test-index", body=query_body)
    all_hits = result['hits']['hits']
    faculty_urls = []
    faculty_emails = []
    faculty_names = []
    texts = []
    for doc in all_hits:
      faculty_emails.append(doc["_source"]["faculty_email"])
      faculty_names.append(doc["_source"]["faculty_name"])
      faculty_urls.append(doc["_source"]["faculty_url"])
      texts.append(doc["_source"]["text"])
    docs = list(zip(faculty_emails, faculty_names, faculty_urls,texts))
    return jsonify({
        "docs": docs
    })



if __name__ == '__main__':
   app.run(debug = True)
