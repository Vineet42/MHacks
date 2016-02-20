from bs4 import BeautifulSoup
from urllib2 import urlopen




def getIndustryFromScraper(company):
    soup = BeautifulSoup(urlopen('https://www.google.com/finance?q=' + company), "html5lib")
    return soup.find("a", {"id": "sector"}).string


if __name__ == '__main__':
    print(getIndustryFromScraper('Ebay'))
















