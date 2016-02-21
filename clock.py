from datetime import datetime

from apscheduler.schedulers.background import BlockingScheduler

from bs4 import BeautifulSoup
# from urllib.request import urlopen
from urllib2 import urlopen
from firebase import firebase

import logging
logging.basicConfig()


fireBase = firebase.FirebaseApplication('https://flickering-torch-8936.firebaseio.com/', None)


def getIndustryFromScraper(company): #Get Industry
    soup = BeautifulSoup(urlopen('https://www.google.com/finance?q=' + company), "html5lib")
    return soup.find("a", {"id": "sector"}).string


def getDataFromFirebase():
    things = fireBase.get('/users', None)
    # print(things)
    return things

def pushDataToFirebase(collection, data):
    # fireBase.post('/' + collection, data)
    fireBase.post('/' + collection, {"data":data, "processed":True})
    print(data)

def putDataToFirebase(collection, thing, data):
	fireBase.put('/' + collection, thing, {"data":str(data) + " PROC", "processed":True})


scheduler = BlockingScheduler()

count = 0

def job_function():
	print("hello from job_function!")
	things = getDataFromFirebase()
	for thing in things:
		if(things[thing]["processed"] == False):
			print(things[thing]["data"])
			putDataToFirebase("users", thing, things[thing]["data"])



scheduler.add_job(job_function, 'interval', seconds=10)

scheduler.start()

# job_function()