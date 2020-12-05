# Setup
1. install Docker (https://www.docker.com/get-started, install Docker Desktop)
2. install python3 (at least 3.7)
3. in project folder, run the following in terminal:
    pip3 install flask\
    pip3 install regex\
    pip3 install elasticsearch\
    pip3 install spacy\
    python3 -m spacy download en\
    docker-compose up -d
4. wait 3 minutes for docker containers to be set up
5. in terminal: python3 setup.py
6. wait for all index to be created, this could take about an hour

# Server
1. in terminal: python3 server.py
2. navigate to http://127.0.0.1:5000/

# Goal
Our project aims to develop a search tool for experts in different fields. An user can enter a search phrase(e.g Data Mining) in the search bar and our application will return the likely results according to similarity between the bios of the expert and the search phrase. The user can inspect the validity of the result by accessing the homepage of the expert using returned URL. Furthermore, the user can contact the expert via the returned email.

# Overview
Our project is based on elastic search, a document-orientated database that provides unstructured search functionality. 
The code base is divided to 3 parts. 
In "setup.py", the application would read the input text files to obtain faculty bios and the corresponding homepage URL. The application would then attempt to extract the faculty name and email from the bios using spacy, a NLP package. These information would be stored into the elastic search database. 
In "server.py", the application would query the database with the input typed in search bar, and return the corresponding results.

# Contributions
Houyuan Sha: Set up the docker container for elastic search; Extract name and email from faculty bios; Store faculty information to elastic search database
Yuechen Liu: Set up Flask; Write api connecting database and frontend
