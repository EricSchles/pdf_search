## Summary of functionality

This is a generalized search tool built on top of elastic search.  It will ingest documents, analyze their type and then make them searchable.  At this point, only full word search with correct spelling is supported, but other features will be added to allow for fuzzy search, partial words, etc.

##How to install:

`sudo pip install -r requirements.txt`

`python run.py` from the root directory of this repo

`sudo docker build -t ericschles/elasticpython:v0.0.1 .`

`sudo docker run -d -p 5000:5000 ericschles/elasticpython:v0.0.1 --name example_run`
