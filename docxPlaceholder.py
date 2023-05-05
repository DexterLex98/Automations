import os
import csv
import uuid
from docxtpl import DocxTemplate

doc_path = "STH.docx"

client_usernames = [] # For storing the usernames

def get_usernames():
    with open("Usernames.csv", 'r') as cf:
        reader = csv.reader(cf)
        for username in reader:
            generate_cert_no(username[0])
        

def generate_cert_no(Cusername):
    print("Generating certs")
    id = uuid.uuid4() # Generate ID for each user
    print(f"UID:{id}, Username:{Cusername}")
    creating_certs(id,Cusername) # Create a new certificate

def creating_certs(cert_id, CUsername):
    # Opening the document and saving it
    doc = DocxTemplate(doc_path)
    context = {"Name": f"{CUsername} Client"}
    doc.render(context)
    doc.save(f"save_certs/{cert_id}_{CUsername}.docx") # Saving the certificates
    cert_manager(cert_id)


def cert_manager(cert_id):
    file_path = f"save_certs\{cert_id}.docx"
    # Checking if the cert_id file exists in directory
    if os.path.isfile(file_path):
        print("Already Generated file", cert_id)
    else:
        print("DEBUG: cert_manager exited")
        exit

get_usernames()
# generate_cert_no()







