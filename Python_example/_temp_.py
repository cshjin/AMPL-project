cond = []
clu_cond = []
with open("conditions.txt") as infile:
	for i in infile:
		cond.append(int(i))
for i in cond:
	if i in [1,2,3,4,5]:
		clu_cond.append(1)
	elif i in [6,7,8,9,10]:
		clu_cond.append(2)
	elif i in [11,12,13,14,15]:
		clu_cond.append(7)
	elif i in [16,17,18,19,20,21]:
		clu_cond.append(8)
	elif i in [22,23,24,25,26]:
		clu_cond.append(5)
	elif i in [27,28,29,30,31]:
		clu_cond.append(4)
	elif i in [32,33,34,35,36,37]:
		clu_cond.append(6)
	elif i in [38,39,40,41,42]:
		clu_cond.append(3)
	# elif i in [16,17,18,19,20,21]:
	# 	clu_cond.append(8)
	# elif i in [16,17,18,19,20,21]:
	# 	clu_cond.append(8)
with open("cluster_condition.txt", "w") as outfile:
	for i in clu_cond:
		outfile.write(str(clu_cond[i])+"\n")
print len(cond)