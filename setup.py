from elasticsearch import Elasticsearch
from datetime import datetime
import re

bios = []
with open("origin_data/compiled_dataset/bios.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        bios.append(line)

urls = []
with open("origin_data/compiled_dataset/urls.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        urls.append(line)

es = Elasticsearch()

for i in range(len(bios)):
    url = urls[i]
    bio = bios[i]

    email = "None"
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', line)
    if match:
        email = match.group()

    doc = {
        'author': 'Houyuan Sha',
        'faculty_name': "Dr. Ruby Wang (place_holder)",
        'faculty_email': email,
        'faculty_url': url,
        'text': bio,
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", id=i, body=doc)
    print(res['result'] + " " + str(i))