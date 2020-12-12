from elasticsearch import Elasticsearch
from datetime import datetime
import re
import spacy

# extract PERSON entity from input string using spacy
def extract_name(input_string):
    nlp = spacy.load('en')
    doc = nlp(input_string)
    for sentence in doc.ents:
        if sentence.label_ == "PERSON":
            return str(sentence)
    return "Not Found"

# extract email entity from input string using spacy
def extract_email(input_string):
    nlp = spacy.load('en')
    doc = nlp(input_string)
    for sentence in doc:
        if (sentence.like_email):
            return str(sentence)

    # if spacy returns nothing, try regex
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', input_string)
    if match:
        return match.group()

    return "Not Found"

# read all bios
bios = []
with open("origin_data/bios6525.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        bios.append(line)

# read all urls
urls = []
with open("origin_data/urls6525.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        urls.append(line)

# create elastic search client, the default port is 9200
es = Elasticsearch()

for i in range(len(bios)):
    url = urls[i]
    bio = bios[i]

    # specify entities to store in es database
    doc = {
        'faculty_name': extract_name(bio),
        'faculty_email': extract_email(bio),
        'faculty_url': url,
        'text': bio,
        'timestamp': datetime.now(),
    }

    # index the new document to es database
    res = es.index(index="test-index", id=i, body=doc)
    print(res['result'] + " " + str(i))