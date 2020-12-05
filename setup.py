from elasticsearch import Elasticsearch
from datetime import datetime
import re
import spacy

def extract_name(input_string):
    nlp = spacy.load('en')
    doc = nlp(input_string)
    for sentence in doc.ents:
        # print(sentence, sentence.label_)
        if sentence.label_ == "PERSON":
            return str(sentence)
    return "Not Found"

def extract_email(input_string):
    nlp = spacy.load('en')
    doc = nlp(input_string)
    for sentence in doc:
        if (sentence.like_email):
            return str(sentence)

    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', input_string)
    if match:
        return match.group()

    return "Not Found"

bios = []
with open("origin_data/bios6525.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        bios.append(line)

urls = []
with open("origin_data/urls6525.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        urls.append(line)

es = Elasticsearch()

for i in range(len(bios)):
    url = urls[i]
    bio = bios[i]

    # email = "None"
    # match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', bio)
    # if match:
    #     email = match.group()

    doc = {
        'faculty_name': extract_name(bio),
        'faculty_email': extract_email(bio),
        'faculty_url': url,
        'text': bio,
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", id=i, body=doc)
    print(res['result'] + " " + str(i))