from docx import Document
from elasticsearch import Elasticsearch
import os
from subprocess import call
import lxml.html

host = "http://localhost:9200"

es = Elasticsearch(host)
index_name = "search_index"

def parse_docx(file_name):
    current_dir = os.getcwd()
    os.chdir("app/files_to_index")
    doc = Document(file_name)
    data = {}
    data["text"] = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    data["title"] = file_name
    es.index(index=index_name, doc_type="txt", body=data)
    os.chdir(current_dir)

def parse_txt(file_name, pdf_parser=False):
    current_dir = os.getcwd()
    if not pdf_parser:
        os.chdir("app/files_to_index")
    with open(file_name,"r") as f:
        data = {}
        data["text"] = f.read()
        data["title"] = file_name
        es.index(index=index_name, doc_type="txt", body=data)
    os.chdir(current_dir)

def parse_pdf(file_name):
    current_dir = os.getcwd()
    os.chdir("app/files_to_index")
    call(["pdftotext","-layout",file_name])
    filename = '.'.join(file_name.split(".")[:-1]) + ".txt"
    parse_txt(filename, pdf_parser=True)
    os.chdir(current_dir)
