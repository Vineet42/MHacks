import math
import scipy
# MUST FIRST LOAD DATA FROM CAPITAL ONE DEMO ACCOUNTS

# a user is going to be a dictof industry: [[frequency, total amt], [freq, amt]]
# this is a sample code to demo the math formulae and I/O format & file types
#    replace all strings and numbers with queried results & firebase data
user = {"Information Technology": [[5, 100], [6, 100], [1, 200], [10, 20], [30, 600]],
"Materials":[[6, 70], [1, 10], [1, 1], [5, 6]]}

# (dictof industry: vals) -> (listof industry)
def all_industries(auser):
    return list(user.keys())

# (listof (listof Num)) -> Num
def avg_freq(listofnum):
    return sum(list(map(lambda x: x[0], listofnum)))/len(list(map(lambda x: x[0], listofnum)))

#(listof (listof Num)) -> Num
def avg_amt(listofnum):
    return sum(list(map(lambda x: x[1], listofnum)))/len(list(map(lambda x: x[1], listofnum)))

#(listof (listof Num)) -> Num
def sigmamle_freq(listofnum):
    n = len(listofnum)
    count = 0
    sumofdiffsq = 0
    while count < n:
        diff = listofnum[count][0] - avg_freq(listofnum)
        sumofdiffsq += diff * diff
        count += 1
    return math.sqrt(sumofdiffsq / n)

#(listof (listof Num)) -> Num
def sigmamle_amt(listofnum):
    n = len(listofnum)
    count = 0
    sumofdiffsq = 0
    while count < n:
        diff = listofnum[count][1] - avg_freq(listofnum)
        sumofdiffsq += diff * diff
        count += 1
    return math.sqrt(sumofdiffsq / n)

def get_cdf(y, mu, sigma):
    return normal.cdf((y - mu) / sigma)

#(listof Str) -> (listof (listof Str Num))
#def weight_freq(listofindustry):
