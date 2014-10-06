from datetime import datetime, timedelta
import itertools
import numpy
import csv
import get_weather
import os
from collections import defaultdict
CURRENT_FOLDER = os.path.dirname(__file__)
# data = []
# with open(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar.csv"), "r") as infile:
#     infile.next()
#     data = infile.next().split(",")
# for i in data:
#     i = float(i)
#     print i
# print i.isnumeric()
#     c = []
#     for line in infile:
#         c.append(line.split(",")[-1])

# print len(c)

# diff = datetime.strptime("2011-01-01 00:00:00", "%Y-%m-%d %H:%M:%S") - datetime.strptime("1991-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
# print diff.total_seconds()/60/60


# def _interpolate(lst, size):
#     step = float(lst[1] - lst[0]) / size
#     new_lst = [lst[0] + step * i for i in range(1, size)]
#     print new_lst

# _interpolate([1, 3], 2)

# -----------------------------------------------------------------------------------------------------------
filename = os.path.join(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"))
data_dic = defaultdict(list)
with open(filename, "r") as in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        for (k, v) in row.items():
            data_dic[k].append(v)

data_size = len(data_dic["TimeCST"])

# field_name = "TimeCST"
# for i in range(data_size - 1, 0, -1):
#     print i
#     timestamp1 = data_dic[field_name][i - 1]
#     timestamp2 = data_dic[field_name][i]
#     first = datetime.strptime(timestamp1.zfill(8), "%I:%M %p")
#     second = datetime.strptime(timestamp2.zfill(8), "%I:%M %p")
#     diff = second - first
#     interval_size = diff.total_seconds() / 60
#     # print interval_size
#     if interval_size > 1:
#         new_lst = [(first + timedelta(minutes=1) * step).strftime("%I:%M %p") for step in range(1, int(interval_size))]
#         [data_dic[field_name].insert(i+j, item) for j, item in enumerate(new_lst)]
# print len(data_dic[field_name])
# diff = datetime.strptime("12:00 PM".zfill(8), "%I:%M %p") - datetime.strptime("1:00 PM".zfill(8), "%I:%M %p")
# print diff.total_seconds()

field_name = "DateUTC"
for i in range(data_size - 1, 0, -1):
    timestamp1 = data_dic["DateUTC"][i - 1]
    timestamp2 = data_dic["DateUTC"][i]
    first = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    second = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    diff = second - first
    interval_size = diff.total_seconds() / 60
    # print interval_size
    if interval_size > 1:
        new_time_lst = [(first + timedelta(minutes=1) * step).strftime("%Y-%m-%d %H:%M:%S") for step in range(1, int(interval_size))]
        [data_dic["DateUTC"].insert(i+j, item) for j, item in enumerate(new_time_lst)]
        [data_dic["Conditions"].insert(i, data_dic["Conditions"][i-1]) for j in range(len(new_time_lst))]
# print data_dic["DateUTC"]
# print data_dic["Conditions"]
subkeys = ["DateUTC", "Conditions"]
subdict = {x: data_dic[x] for x in data_dic if x in subkeys}

print "here"
# ----------------------------------------------------------------------------------
solar_filename = os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar.csv")
solar_data_dic = defaultdict(list)
with open(solar_filename, "r") as in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        for (k, v) in row.items():
            solar_data_dic[k].append(v)
data_size = len(solar_data_dic["METSTAT Glo (Wh/m^2)"])
for i in range(data_size - 1, 0, -1):
    radi1 = float(solar_data_dic["METSTAT Glo (Wh/m^2)"][i-1])
    radi2 = float(solar_data_dic["METSTAT Glo (Wh/m^2)"][i])
    step = (radi2 - radi1)/60
    [solar_data_dic["METSTAT Glo (Wh/m^2)"].insert(i+j, radi1+step*j) for j in range(59)]
solar_data_dic["METSTAT Glo (Wh/m^2)"] = [float("{0:.4f}".format(float(x))) for x in solar_data_dic["METSTAT Glo (Wh/m^2)"]]
subdict["METSTAT"] = solar_data_dic["METSTAT Glo (Wh/m^2)"]
# print subdict.keys()

with open('dict_backup.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f, subdict.keys())
    # w.writeheader()
    all = []
    row = subdict.keys()
    all.append(row)
    for i in range(len(subdict["METSTAT"])):
        row = [subdict["DateUTC"][i], subdict["METSTAT"][i], subdict["Conditions"][i]]
        all.append(row)
    w.writerows(all)
