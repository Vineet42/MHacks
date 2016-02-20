#used to get stock performance info

import requests
import json

ticker = "TSLA"
search = ticker+"~25|VWO~25|IVV~25|MALOX~25|"

portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/portfolio-analysis", params= {"useCache":"true","positions":search,"calculateExposures":"true","calculatePerformance":"true"})

jsonData = portfolioAnalysisRequest.json()

myDict = {}
myDict[ticker] = []

# print("highReturn\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["highReturn"]))
# print("lowReturn\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["lowReturn"]))
# print("grossReturnY1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY1"]))
# print("grossReturnY3\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY3"]))
# print("grossReturnY5\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY5"]))

# print("incomeReturnM1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM1"]))
# print("incomeReturnM3\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM3"]))
# print("incomeReturnM6\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM6"]))
# print("incomeReturnY1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnY1"]))
# print("incomeReturnYtd\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnYtd"]))

# print("investorReturnY1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY1"]))
# print("investorReturnY3\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY3"]))
# print("investorReturnY5\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY5"]))

# print("loadAdjustedReturnM1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM1"]))
# print("loadAdjustedReturnM3\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM3"]))
# print("loadAdjustedReturnM6\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM6"]))

# print("loadAdjustedReturnY1\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY1"]))
# print("loadAdjustedReturnY2\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY2"]))
# print("loadAdjustedReturnY3\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY3"]))
# print("loadAdjustedReturnY4\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY4"]))
# print("loadAdjustedReturnY5\t" + str(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY5"]))


myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["highReturn"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["lowReturn"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY3"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["grossReturnY5"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM3"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnM6"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnY1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["incomeReturnYtd"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY3"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["investorReturnY5"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM3"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnM6"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY1"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY2"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY3"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY4"])
myDict[ticker].append(jsonData["resultMap"]["PORTFOLIOS"][0]["portfolios"][0]["returns"]["weightedAveragePerformance"]["loadAdjustedReturnY5"])


print(myDict)