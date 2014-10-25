import json
import urllib
import os
from datetime import datetime, timedelta
import csv
from dateutil import tz
import tempfile
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
from collections import defaultdict, Counter


def get_history_using_API(WEATHER_API):
    '''
    Get Historical Weather Data through HTTP 
    NOTE: be cautious, the API is only allowed to get retrieve data 20 times per day
    '''
    num_days = (END_DATE - START_DATE).days
    work_day = START_DATE

    for i in range(num_days):
        y = work_day.year
        m = "%02d" % work_day.month
        d = "%02d" % work_day.day
        address = "http://api.wunderground.com/api/" + WEATHER_API + "/history_{}{}{}/q/KMDW.json".format(y, m, d)
        filename = os.path.join(META_DATA_FOLDER, "wunderground_{}_{}_{}.json".format(y, m, d))
        urllib.urlretrieve(address, filename)
        work_day = work_day + timedelta(days=1)


def get_history_using_HTTP():
    ''' 
    Get Historical Weather Data through HTTP 
    '''
    num_days = (END_DATE - START_DATE).days
    work_day = START_DATE

    # @TODO: use multi thread to download weather data if possible.
    for i in range(num_days):
        y = work_day.year
        m = "%02d" % work_day.month
        d = "%02d" % work_day.day
        address = "http://www.wunderground.com/history/airport/KORD/{}/{}/{}/DailyHistory.html?format=1".format(y, m, d)
        filename = os.path.join(META_DATA_FOLDER, "wunderground_{}_{}_{}.csv".format(y, m, d))
        urllib.urlretrieve(address, filename)
        outFile = ""
        with open(filename, "r") as inFile:
            inFile.readline()
            for line in inFile:
                line = line.replace("<br />", "")
                outFile += line
        with open(filename, "w") as inputFile:
            inputFile.write(outFile)
        work_day = work_day + timedelta(days=1)


# def convert_to_json():
#     """
#     Convert yearly solar data into json format.
#     NOTE: it will cost much more spaces.
#     """
# with open("wunderground_1991_01_01.csv", "r") as inFile:
#     for year in range(1991, 2011):
#         with open("..\\Weather_Data\\725340\\725340_" + str(year) + "_solar.csv", "r") as inFile:
#             fieldnames = inFile.readline().strip("\n").split(",")
#             fieldnames = [i.strip() for i in fieldnames]
#             reader = csv.DictReader(inFile, fieldnames)

#             out_data = {}
#             out_data["history"] = []
#             with open(os.path.join(CURRENT_FOLDER, "725340_" + str(year) + "_solar.json"), "w") as outFile:
#                 for row in reader:
#                     out_data["history"].append(row)
# json.dump(row, outFile, indent = 4, sort_keys = True)
# outFile.write(",")
#                 json.dump(out_data, outFile, indent=4, sort_keys=True)
#     pass


# def convert_weather_to_json():
#     '''
#     Convert weather underground weather data into json file.
#     NOTE: it will cost much more spaces.
#     '''
#     num_days = (END_DATE - START_DATE).days
#     work_day = START_DATE
#     for i in range(num_days):
#         y = work_day.year
#         m = "%02d" % work_day.month
#         d = "%02d" % work_day.day
# address = "http://www.wunderground.com/history/airport/KMDW/{}/{}/{}/DailyHistory.html?format=1".format(y, m, d)
#         filename = os.path.join(CURRENT_FOLDER, "wunderground_{}_{}_{}.csv".format(y, m, d))
#         out_file = os.path.join(CURRENT_FOLDER, "wunderground_{}_{}_{}.json".format(y, m, d))
# print filename
# urllib.urlretrieve(address, filename)
#         outFile = ""
#         with open(filename, "r") as inFile:
#             fieldnames = inFile.readline().strip("\n").split(",")
#             fieldnames = [i.strip() for i in fieldnames]
#             reader = csv.DictReader(inFile, fieldnames)

#             out_data = {}
#             out_data["history"] = []
#             with open(out_file, "w") as outFile:
#                 for row in reader:
#                     out_data["history"].append(row)
#                 json.dump(out_data, outFile, indent=4, sort_keys=True)
#         work_day = work_day + timedelta(days=1)


# def stat_each_field():
#     condition = []
#     with open("test.json", "r") as inFile:
#         json_data = json.load(inFile)
#         for each in json_data["history"]:
#             if each["Conditions"] not in condition:
#                 condition.append(each["Conditions"])
#     return condition

def add_condition_to_solar(lst):
    """
    Add weather condition to the last column of solar data
    """
    with open(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar.csv"), "r") as csvinput:
        with open(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"), 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            row = next(reader)
            row.append('Conditions')
            all.append(row)
            conds = iter(lst)
            for row in reader:
                row.append(conds.next())
                all.append(row)
            writer.writerows(all)


# def combine_weather_and_radi():
#     with open("725340_1991_solar.json", "r") as solar_file:
#         solar_data = json.load(solar_file)
#         solar_history = solar_data["history"]

#         with open("test.json", "r") as weather_file:
#             weather_data = json.load(weather_file)
#             weather_history = weather_data["history"]
#             for i in weather_history:
#                 weather_timestamp = _convert_to_LST(i["DateUTC"])
#                 for j in solar_history:
#                     solar_timestamp = datetime.strptime(
#                         j["YYYY-MM-DD"] + " " + j["HH:MM (LST)"].zfill(5), "'%Y-%m-%d %H:%M")
#                     if solar_timestamp.year == weather_timestamp.year and solar_timestamp.month == weather_timestamp.month and solar_timestamp.day == weather_timestamp.day and solar_timestamp.hour == weather_timestamp.hour:
#                         print solar_timestamp.hour

#     pass


def merge_solar_csv_files():
    """
    Merge yearly solar data into a single csv file. 
    """
    with open(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar.csv"), "w") as target_file:
        for line in open(os.path.join(CURRENT_FOLDER, "solar_data", "725340", "725340_" + str(1991) + "_solar.csv"), "r"):
            target_file.write(line)
        for year in range(1992, 2011):
            with open(os.path.join(CURRENT_FOLDER, "solar_data", "725340", "725340_" + str(year) + "_solar.csv"), "r") as in_file:
                in_file.next()
                for line in in_file:
                    target_file.write(line)


def merge_weather_csv_files():
    """
    Merge weather underground csv file into a single csv file. 
    """
    num_days = (END_DATE - START_DATE).days
    work_day = START_DATE + timedelta(days=1)
    with open(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"), "w") as target_file:
        for line in open(os.path.join(CURRENT_FOLDER, "weather_data", "KORD", "wunderground_1991_01_01.csv")):
            target_file.write(line)

        for i in range(num_days - 1):
            y = work_day.year
            m = "%02d" % work_day.month
            d = "%02d" % work_day.day
            filename = os.path.join(CURRENT_FOLDER, "weather_data", "KORD", "wunderground_{}_{}_{}.csv".format(y, m, d))
            with open(filename) as in_file:
                in_file.next()
                for line in in_file:
                    target_file.write(line)
            work_day = work_day + timedelta(days=1)
    pass


def get_weather_field(fieldname):
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"), "r") as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k
    return columns[fieldname]


def plot_weather():
    fname = cbook.get_sample_data(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'total_20_years_weather.csv'), asfileobj=False)
    plotfile(fname, (2, 5))


def get_csv_data_size(filename):
    """
    Get the row size of a csv file.
    """
    with open(filename) as in_file:
        in_file.readline()
        return len(in_file.readlines())


def get_dict_data(filename):
    """
    Get dictionary data from a cvs file
    """
    data_dic = defaultdict(list)
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for (k, v) in row.items():
                data_dic[k].append(v)
    return data_dic


def get_weather_data_dic():
    filename = os.path.join(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"))
    data_dic = defaultdict(list)
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for (k, v) in row.items():
                data_dic[k].append(v)
    return data_dic


def _convert_to_LST(date_UTC):
    '''
    Convert UTC timestamp to Local Standard Timezone 
    '''
    from_zone = tz.gettz("UTC")
    to_zone = tz.tzlocal()
    utc = datetime.strptime(date_UTC, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


START_DATE = datetime.strptime("1991-01-01", "%Y-%m-%d")
END_DATE = datetime.strptime("2011-01-01", "%Y-%m-%d")
API = "2f060cf5d6061a63"  # weather underground API
CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
# CURRENT_FOLDER = tempfile.mkdtemp()
# CURRENT_FOLDER = os.path.abspath("c:\\users\\hongwe~1\\appdata\\local\\temp\\tmppemjrz")
# DATA_FOLDER = os.path.join(CURRENT_FOLDER, "meta_data")
if not os.path.exists(os.path.join(CURRENT_FOLDER, "weather_data")):
    META_DATA_FOLDER = os.mkdir(os.path.join(CURRENT_FOLDER, "weather_data", "KORD"))
META_DATA_FOLDER = os.path.join(CURRENT_FOLDER, "weather_data", "KORD")


def _main():
    # download weather history data
    # get_history_using_HTTP()

    # merge solar into single csv file
    # merge_solar_csv_files()

    # merge weather into single csv file
    # merge_weather_csv_files()

    # get the data size of csv file
    # filename = os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv")
    # print get_csv_data_size(filename)

    # get weather data dictionary
    # weather_data_dic = get_weather_data_dic()
    # weather_data_size = len(weather_data_dic["TimeCST"])
    # for i in range(weather_data_size - 1, 0, -1):
    #     timestamp1 = weather_data_dic["DateUTC"][i - 1]
    #     timestamp2 = weather_data_dic["DateUTC"][i]
    #     first = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    #     second = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    #     diff = second - first
    #     interval_size = diff.total_seconds() / 60
    # print interval_size
    #     if interval_size > 1:
    #         new_time_lst = [(first + timedelta(minutes=1) * step).strftime("%Y-%m-%d %H:%M:%S") for step in range(1, int(interval_size))]
    #         [weather_data_dic["DateUTC"].insert(i+j, item) for j, item in enumerate(new_time_lst)]
    # print len(weather_data_dic["TimeCST"])

    # add weather condition to solar data
    # add_condition_to_solar()
    #

    # filename = os.path.join(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"))
    
    # **************************************************************************
    cond_list = list()
    ori_cond_list = get_weather_field("Conditions")
    ori_time_list = get_weather_field("DateUTC")
    local_time_list = [_convert_to_LST(i) for i in ori_time_list]
    time_size = len(local_time_list)
    print time_size
    temp = []
    # time_size = 10
    i, j = 0, 1
    while j < time_size:
        # temp.append(ori_cond_list[i])
        gap_size = (local_time_list[j]-local_time_list[i]).total_seconds()/60
        temp.extend([ori_cond_list[i] for x in range(int(gap_size))])
        j+=1
        i+=1
    # print len(temp)
    condi = []
    i = 0
    less30 = 0
    while i < len(temp) - 1:
        t = []
        for j in range(60):
            t.append(temp[i+j])
        i += 60
        condi.append(max(set(t), key=t.count))

        if Counter(t).most_common(1)[0][1] < 30:
            less30 += 1
    print less30
    # print len(condi)
    # print condi[:100]
    add_condition_to_solar(condi)

    # **************************************************************************
    # filename = os.path.join(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"))
    # data_dic = defaultdict(list)
    # with open(filename, "r") as in_file:
    #     reader = csv.DictReader(in_file)
    #     for row in reader:
    #         for (k, v) in row.items():
    #             data_dic[k].append(v)
    # data_size = len(data_dic["HH:MM (LST)"])
    # j = 0
    # for i in range(data_size):
    #     # for j in range(len(local_time_list)):
    #     date = data_dic["YYYY-MM-DD"][i].split("-")
    #     year = date[0]
    #     month = date[1]
    #     day = date[2]
    #     time = data_dic["HH:MM (LST)"][i].split(":")
    #     hour = str(int(time[0])%24).zfill(2)
    #     minute = time[1][:2]
    #     # solar_time = datetime.strptime(data_dic["YYYY-MM-DD"][i]+" "+str(int(data_dic["HH:MM (LST)"][i][:2])%24).zfill(2)+data_dic["HH:MM (LST)"][i][2:], "%Y-%m-%d %H:%M")
    #     solar_time = datetime.strptime(year+"-"+month+"-"+day+" "+hour+":"+minute, "%Y-%m-%d %H:%M")
    #     if hour == "00":
    #         solar_time = solar_time + timedelta(days=1)
        
    #     if solar_time == local_time_list[i].replace(tzinfo=None):
    #         # print solar_time, local_time_list[i].replace(tzinfo=None)
    #         cond_list.append(ori_cond_list[i])
    #     elif solar_time > local_time_list[i].replace(tzinfo=None):
    #         # print solar_time, local_time_list[i].replace(tzinfo=None)

    #         temp = []
    #         index = i
    #         while solar_time >= local_time_list[index].replace(tzinfo=None):
    #             temp.append(ori_cond_list[index])
    #             index += 1
    #         cond_list.append(max(set(temp), key=temp.count))
    #     else:
    #         # print solar_time, local_time_list[i].replace(tzinfo=None)

    #         temp = []
    #         index = i
    #         while solar_time <= local_time_list[index].replace(tzinfo=None):
    #             temp.append(ori_cond_list[index])
    #             index -= 1
    #         cond_list.append(max(set(temp), key=temp.count))

    #     # else:
    #     #     j += 1
    # # print cond_list
    # add_condition_to_solar(cond_list)
    # _demo()

def _demo():
        # Demo goes here!!!
    filename = os.path.join(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"))
    data_dic = defaultdict(list)
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for (k, v) in row.items():
                data_dic[k].append(v)
    data_size = len(data_dic["HH:MM (LST)"])

    current_date, current_time, current_cond = "10-21", "14:00", "Partly Cloudy"
    print "Current_time:", current_date, current_time
    print "Condition:", current_cond

    print "LOOKING INTO HISTORICAL DATA..."
    # get historical data
    date = data_dic["YYYY-MM-DD"]
    time = data_dic["HH:MM (LST)"]
    condition = data_dic["Conditions"]
    solar_radiation = data_dic["METSTAT Glo (Wh/m^2)"]
    matched_index = []
    for i in range(data_size):
        if date[i][-5:] == current_date and time[i].zfill(5) == current_time:
            matched_index.append(i)

    flexible_index = []
    for i in matched_index:
        flexible_index.extend([i - 10*24 + j*24 for j in range(20)])
    print len(flexible_index), "flexible timestemps selected"

    forecasted_cond = []
    cur_cond_indices = []
    for i in flexible_index:
        if condition[i - 1] == current_cond:
            cur_cond_indices.append(i)
            forecasted_cond.append(condition[i])

    counted_cond = Counter(forecasted_cond)

    print "historical_cond: ", counted_cond
    forecasted_prob = {}
    SR = {}
    for key in counted_cond:
        forecasted_prob[key] = float(counted_cond[key]) / len(cur_cond_indices)
        SR[key] = 0
    print "with its probablity:", forecasted_prob

    for i in cur_cond_indices:
        SR[condition[i]] += float(solar_radiation[i])
    print "the associated SR value:", SR

    expected_SR = 0
    for key in counted_cond:
        expected_SR += forecasted_prob[key] * SR[key] / counted_cond[key]
    print "----------------"
    print "The expected solar radiation based on historical data is:", expected_SR, "Wh"

    # get the simulated load of that hour
    diff = datetime.strptime("2014-"+ current_date + " " + current_time, "%Y-%m-%d %H:%M") - datetime.strptime("2014-01-01", "%Y-%m-%d")
    hours = diff.total_seconds()/60/60
    
    filename = os.path.join(os.path.join(CURRENT_FOLDER, "wind_data", "wind_data.csv"))
    data_dic = defaultdict(list)
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for (k, v) in row.items():
                data_dic[k].append(v)
    spd = float(data_dic["Wind speed"][int(hours)+1])
    print "----------------"
    print "The energy can get from wind turbine is: ", 1.0/2*1.27*3.14*25*spd**3*0.5, "Wh"

    filename = os.path.join(os.path.join(CURRENT_FOLDER, "load_data", "E_PLUS_RESI_TMY3_Load.csv"))
    data_dic = defaultdict(list)
    with open(filename, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            for (k, v) in row.items():
                data_dic[k].append(v)
    print "----------------"
    print "The simulated load energy of a single residental house will be ", float(data_dic["load"][int(hours)+1])*1000, "Wh"

if __name__ == '__main__':
    # _main()
    _demo()
