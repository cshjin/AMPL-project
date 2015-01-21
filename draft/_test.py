init = []
with open("BuyingPrice.txt") as in_file:
	in_lines = [x.strip("\n") for x in in_file.readlines()]
	for i in range(len(in_lines)-1):
		if in_lines[i] < in_lines[i+1]:
			init.append(500)
		else:
			init.append(0)
with open("InitBattery.txt", "w") as out_file:
	for i in init:
		out_file.write(str(i)+"\n")
