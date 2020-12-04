from flask import Flask
from elasticsearch import Elasticsearch

app = Flask(__name__) 
es = Elasticsearch()

user_request = "Data Mining~"

query_body = {
  "from" : 0, "size" : 1,
  "query": {
    "query_string": {
      "query": user_request,
      "fuzziness" : 0
    }
  }
}

result = es.search(index="test-index", body=query_body)

all_hits = result['hits']['hits']
count = 0
for num, doc in enumerate(all_hits):
    count += 1
    print("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
   
    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)
   
    # print a few spaces between each doc for readability
    
    print ("\n\n")
    print(count)
    print ("\n\n")

@app.route('/')
def home():
    return result

if __name__ == '__main__':
   app.run(debug = True)