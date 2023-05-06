import os, multiprocessing as mp
import csv
import uuid
from docxtpl import DocxTemplate
from docxtopdf import convert

doc_path = "STH.docx"
DOCX_dir = f"{os.getcwd()}\save_certs"
PDF_dir = "Exported_PDFS"
client_usernames = [] # For storing the usernames





def get_usernames():
    with open("Usernames.csv", 'r') as cf:
        reader = csv.reader(cf)
        for username in reader:
            # print(username)
            generate_cert_no(username[0]) # Generating certificates for each user
        

def generate_cert_no(Cusername):
    print("Generating certs")
    id = uuid.uuid4() # Generate ID for each user
    print(f"UID:{id}, Username:{Cusername}")
    creating_certs(id,Cusername) # Create a new certificate

def creating_certs(cert_id, CUsername):
    # Opening the document and saving it
    doc = DocxTemplate(doc_path)
    context = {"Name": f"{CUsername}"}
    doc.render(context)
    doc.save(f"save_certs/{CUsername}_{cert_id}.docx") # Saving the certificates
    cert_manager(cert_id)


def cert_manager(cert_id):
    file_path = f"save_certs\{cert_id}.docx"
    # Checking if the cert_id file exists in directory
    if os.path.isfile(file_path):
        print("Already Generated file", cert_id)
    else:
        print("DEBUG: cert_manager exited")
        exit

# Exporting the documents to PDFs
def exportToPdf():
    files = os.listdir(DOCX_dir)    # All the docx files in the save_certs
    isexists = os.path.exists(PDF_dir)
    if not isexists:
        os.makedirs(PDF_dir)        # If directory doesnt exists makeone
        print(f"DEBUG: {PDF_dir} Created")
    else:
        print(f"DEBUG: {PDF_dir} exists \n")
    
    for f in files:
        Convertthefile(f,f.split(".")[0])
        


def Convertthefile(Cdocxfilename, CnameofExportfile):
    # Converting and saving the pdfs in the directory  
    convert(f"{os.getcwd()}\save_certs\{Cdocxfilename}",f"{os.getcwd()}\{PDF_dir}\{CnameofExportfile}.pdf")
    print("DEBUG: Exported All the pdfs")


get_usernames()
exportToPdf()
# generate_cert_no()







