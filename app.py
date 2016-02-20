from bs4 import BeautifulSoup
from urllib2 import urlopen
from firebase import firebase

fireBase = firebase.FirebaseApplication('https://mhacks2016.firebaseio.com/', None)


def getIndustryFromScraper(company): #Get Industry
    soup = BeautifulSoup(urlopen('https://www.google.com/finance?q=' + company), "html5lib")
    return soup.find("a", {"id": "sector"}).string


def getDataFromFirebase():
    things = fireBase.get('/users', None)
    print(things)

def pushDataToFirebase(collection, data):
    fireBase.post('/' + collection, data)















