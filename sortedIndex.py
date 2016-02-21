s = [30, 20, 40, 20, 10]

sortedList = sorted(s)

indices = []

for i in s:
	indices.append(sortedList.index(i))

print(indices)