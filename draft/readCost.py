
def main():
	result = []
	# with open("mg_1_42.out") as in_file:
	# 	for line in in_file:
	# 		if "cost" in line:
	# 			result.append(line.split("cost")[1].strip())
	# with open("COST_MG_1_42_new.out", "w") as out_file:
	# 	for i in result:
	# 		out_file.write(i+'\n')
	# 		
	with open("mg_3_42.out") as in_file:
		for line in in_file:
			if " = " in line:
				result.append(line.split(" = ")[1])
	with open("COST_MG_3_42_new.out", "w") as out_file:
		for i in result:
			out_file.write(i)
	print len(result)

if __name__ == '__main__':
	main()