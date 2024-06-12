import requests

def getUnitProtFasta(id):

    response = requests.get("https://rest.uniprot.org/uniprotkb/P12345.fasta")
    print(response.text)


getUnitProtFasta("ax")