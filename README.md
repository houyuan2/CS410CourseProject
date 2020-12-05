# Setup
1. install Docker (https://www.docker.com/get-started, install Docker Desktop)
2. install python3 (at least 3.7)
3. in project folder, run the following in terminal:
    pip3 install flask\
    pip3 install regex\
    pip3 install elasticsearch\
    pip3 install spacy\
    python3 -m spacy download en\
    docker-compose up -d\
4. wait 3 minutes for docker containers to be set up
5. in terminal: python3 setup.py
6. wait for all index to be created, this could take about an hour
