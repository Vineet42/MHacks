#used to get stocks in a particular category

import requests
import json

# "Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Health Care", "Financials", "Information Technology", "Telecommunication Services", "Utilities", 

sector = "Consumer Staples"

portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/search-securities", params= {"useCache":"true","filters":"gicsSector1:(\"" + sector + "\")","responseFields":"bloombergTicker"})

jsonData = portfolioAnalysisRequest.json()

companies = jsonData["resultMap"]["SEARCH_RESULTS"][0]["resultList"]
for company in companies:
	ticker = company["bloombergTicker"]
	if(ticker): print(ticker.split(" ")[0])
