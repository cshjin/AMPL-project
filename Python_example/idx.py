dic = {}
with open("idx.txt") as infile:
	for num, line in enumerate(infile, 1):
		# print  dic.get(int(line.strip("\n")), []).append(2)
		dic[num] = int(line.strip("\n"))

		# if dic.get(int(line.strip("\n"))) is None:
		# 	dic[int(line.strip("\n"))] = [num]
		# else:
		# 	dic[int(line.strip("\n"))].append(num)
with open("conditions.txt") as infile:
	with open("c_conditions.txt", "w") as outfile:
		for line in infile:
			outfile.write(str(dic[int(line.strip("\n"))]) + "\n")


