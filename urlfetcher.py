import requests as r
import pandas as pd
import json
from colorama import Fore, Style

csv_data = pd.read_csv('sample.csv').filter(['Host','Name','See Also'])

df = pd.DataFrame(csv_data).drop_duplicates()
df.reset_index()


# GetSizeofURLs
def GetSizeofURLS(TotalURLs):
    return TotalURLs

# Processing the Nessus Links Method Definition
def ProcessNewNessus(VulnList):
    
    for vuln in VulnList:
        n_url = vuln[3].split("\n")
        nameofVuln = vuln[2]
        for fetchedURLs in n_url:
            HTTPRedirectHandler(nameofVuln, fetchedURLs)

Dataresolved = dict()

# HTTP Redirect Handling 
def HTTPRedirectHandler(NameofVuln,url):
   response = r.get(url=url)
   if response.history:
    sizeofHistory = len(response.history)
    print(Fore.RED, "Name of Vulnerability:",NameofVuln , Fore.WHITE,"RESOLVED URLS: ",Fore.YELLOW, response.url, "\nSTATUS_CODE:", response.status_code)
    Dataresolved[NameofVuln]= response.url

    # If No redirect add it to Dictonary
   else:
    print(Fore.RED, "Name of Vulnerability:", NameofVuln, Fore.WHITE, "NORMAL URL:", Fore.YELLOW, response.url,"\nSTATUS CODE:", response.status_code)
    Dataresolved[NameofVuln]= response.url
    print(Style.RESET_ALL)

       
    
        
# Printing all the vulnerabilities  
NessusVulnLists = []
for i in df.itertuples():
    # print(i.Host, i.Name, i._3)
    Host = str(i.Host)
    VulnName = str(i.Name)
    urls = str(i._3)
    if "http://www.nessus.org" in urls:
        # print(VulnName,":",urls)
        NessusVulnLists.append(i)

print("Before Nessus Link filter:", df.count())
print("After Nessus Link filter:", len(NessusVulnLists))

ProcessNewNessus(NessusVulnLists)
GetSizeofURLS(len(NessusVulnLists))





    




