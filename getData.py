# P/E ratio - (security data) resultMap / SECURITY[0] / peRatio
# P/B ratio - (security data) resultMap / SECURITY[0] / pbRatio
# ROA - (security data) resultMap / SECURITY[0] / returnOnAssets
# One Year Sharpe ratio - (performance data) resultMap / RETURNS[0] / latestPerf / oneYearSharpeRatio   0.20
import requests
import json

sectors = ["Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", 
	"Health Care", "Financials", "Information Technology", "Telecommunication Services", "Utilities"]

# sectors = [] #to prevent overwriting files

for sector in sectors:
	print("PROCESSING SECTOR: " + sector)
	myfile = open(sector + ".txt", "w+")

	portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/search-securities", params= {"useCache":"true","filters":"gicsSector1:(\"" + sector + "\")","responseFields":"bloombergTicker"})

	jsonData = portfolioAnalysisRequest.json()

	companies = jsonData["resultMap"]["SEARCH_RESULTS"][0]["resultList"]
	for company in companies:
		ticker = company["bloombergTicker"]
		if(ticker):
			ticker = ticker.split(" ")[0]

			print(ticker)
			# print(ticker, file = myfile)
			performanceData = requests.get("https://test3.blackrock.com/tools/hackathon/performance", params= {'identifiers':ticker})

			jsonData = performanceData.json()
			try:
				sharpe = jsonData["resultMap"]["RETURNS"][0]["latestPerf"]["oneYearSharpeRatio"]
			except:
				sharpe = -1000

			# print(sharpe)



			securityData = requests.get("https://test3.blackrock.com/tools/hackathon/security-data", params= {'identifiers':ticker})

			jsonData = securityData.json()


			try:
				peRatio = jsonData["resultMap"]["SECURITY"][0]["peRatio"]
			except:
				peRatio = -1000

			try:
				pbRatio = jsonData["resultMap"]["SECURITY"][0]["pbRatio"]
			except:
				pbRatio = -1000

			try:
				roa = jsonData["resultMap"]["SECURITY"][0]["returnOnAssets"]
			except:
				roa = -1000

			toPrint = ticker + "," + str(sharpe) + "," + str(peRatio) + "," + str(pbRatio) + "," + str(roa)

			# print(ticker)
			print(sharpe)
			print(peRatio)
			print(pbRatio)
			print(roa)
			print()

			# print(sharpe, file = myfile)
			# print(peRatio, file = myfile)
			# print(pbRatio, file = myfile)
			# print(roa, file = myfile)
			# print("", file = myfile)

			print(toPrint, file = myfile)