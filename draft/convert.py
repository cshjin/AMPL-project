# convert
import random, math
# temp = open('HeatDegreeHours.txt','r')
# cool = open('CoolingDegreeHours.txt','r')
# wind = open('WindSpeed.txt','r')
# cloud = open('CloudOvercastPercentage.txt','r')
# solar = open('SolarRadi.txt','r')
dis = open('SellingPrice.txt','w')

# for i in temp.readlines():
# 	if i=="\"N\"\n": 	# N
# 		dis.write(str(1)+'\n')
# 	elif i=='\"A\"\n':	# A
# 		dis.write(str(2)+'\n')
# 	else:				# M
# 		dis.write(str(3)+'\n')
# s = temp.readline()
# l = s.split(',')
# for i in l:
# 	if i=='N':
# 		dis.write(str(1)+'\n')
# 	elif i=='A':
# 		dis.write(str(2)+'\n')
# 	else:
# 		dis.write(str(3)+'\n')

## prices
for i in range(8759):
	if i % 24 <7:
		dis.write(str(0.051*0.8)+'\n')
	elif i % 24 <11:
		dis.write(str(0.099*0.8)+'\n')
	elif i % 24 < 17:
		dis.write(str(0.081*0.8)+'\n')
	elif i % 24 < 21:
		dis.write(str(0.099*0.8)+'\n')
	else:
		dis.write(str(0.051*0.8)+'\n')

## resources
# for i in range(8759):
# 	amount = 0.5*0.5*5*5*1.27*math.pi*pow(float(wind.readline()),3)+ 1.2 *100 * float(solar.readline()) * (1-float(cloud.readline())/100)
# 	dis.write(str(amount)+'\n')


dis.close()
# temp.close()
