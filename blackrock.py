import requests
import json

ticker = "TSLA"

portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/performance", params= {'identifiers':ticker})

jsonData = portfolioAnalysisRequest.json()

want = ["highReturn", "lowReturn"]


for ele in want:
	print(ele + "\t\t" + str(jsonData["resultMap"]["RETURNS"][0][ele]))

latestPerf = jsonData["resultMap"]["RETURNS"][0]["latestPerf"]

wantInLatestPerf = ["fiveYear", "fiveYearAnnualized", "fiveYearRisk", "fiveYearRiskAnnualized", "fiveYearSharpeRatio"]

for ele in wantInLatestPerf:
	print(ele + "\t\t" + str(jsonData["resultMap"]["RETURNS"][0]["latestPerf"][ele]))
