sectors = ["Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", 
	"Health Care", "Financials", "Information Technology", "Telecommunication Services", "Utilities"]

# sector = sectors[0]
for sector in sectors:
	myfile = open(sector + ".txt", "r").read().split("\n")
	myfile = myfile[0:len(myfile)-1]

	outfile = open(sector + "Rankings.txt", "w")

	nameArr = []
	sharpeArr = []
	peArr = []
	pbArr = []
	roaArr = []

	for line in myfile:
		data = line.split(",")
		nameArr.append(data[0])
		sharpeArr.append(data[1])
		peArr.append(data[2])
		pbArr.append(data[3])
		roaArr.append(data[4])

	s = sharpeArr
	argmaxes = sorted(range(len(s)), key=lambda k: s[k])
	indexes = zip(xrange(len(s)), argmaxes)
	sorted_indexes = sorted(indexes, key=lambda k: k[1])
	sharpeArr = [v[0] for v in sorted_indexes]

	s = peArr
	argmaxes = sorted(range(len(s)), key=lambda k: s[k])
	indexes = zip(xrange(len(s)), argmaxes)
	sorted_indexes = sorted(indexes, key=lambda k: k[1])
	peArr = [v[0] for v in sorted_indexes]

	s = pbArr
	argmaxes = sorted(range(len(s)), key=lambda k: s[k])
	indexes = zip(xrange(len(s)), argmaxes)
	sorted_indexes = sorted(indexes, key=lambda k: k[1])
	pbArr = [v[0] for v in sorted_indexes]

	s = roaArr
	argmaxes = sorted(range(len(s)), key=lambda k: s[k])
	indexes = zip(xrange(len(s)), argmaxes)
	sorted_indexes = sorted(indexes, key=lambda k: k[1])
	roaArr = [v[0] for v in sorted_indexes]

	totArr = [sum(x) for x in zip(sharpeArr, peArr, pbArr, roaArr)]



	print(nameArr)
	print
	print(totArr)

	s = totArr
	argmaxes = sorted(range(len(s)), key=lambda k: s[k])
	indexes = zip(xrange(len(s)), argmaxes)
	sorted_indexes = sorted(indexes, key=lambda k: k[1])
	totArr = [v[0] for v in sorted_indexes]

	print(totArr)

	finalArr = [""] * len(totArr)

	for i in range(len(totArr)):
		finalArr[totArr[i]] = nameArr[i]

	finalArr.reverse()

	for company in finalArr:
		print company
		outfile.write(company + "\n")

	outfile.close()