import get_weather
from datetime import datetime
from collections import defaultdict, Counter, OrderedDict
import matplotlib.pyplot as plt
import itertools
import numpy
import os
CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))

def time_gap_stat():
    """ 
    Get a time gap list between every consecutive timestampts.
    @return {list} timestampts diffs in MINUTES
    """
    timestampts = get_weather.get_weather_field("DateUTC")
    # print timestampts[1]
    diffs = []
    for i in range(len(timestampts) - 1):
        diff = datetime.strptime(timestampts[i + 1].strip(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(
            timestampts[i].strip(), "%Y-%m-%d %H:%M:%S")
        diffs.append(diff.total_seconds() / 60)
        # if diff.total_seconds() < 0:
        #   print timestampts[i], diff.total_seconds()
    return diffs


def cond_stat(conds, timedelta=1):
    """ 
    Get the Statistics of Conditions 
    @return {numpy.matrix} a probability matrix
    """
    # get the unique list of weather condition
    conds_unique = _get_unique_list(conds)
    # print conds_unique
    # initial the possible outcomes from condition to condition
    conds_pairs = list(itertools.product(conds_unique, repeat=2))
    dic = dict((pair, 0.) for pair in conds_pairs)
    # count consecutive weather conditions
    for i in range(len(conds) - 1):
        if (conds[i], conds[i + 1]) in dic:
            dic[(conds[i], conds[i + 1])] += 1

    # def inter_cond(timedelta=1):
    #     timestampts = get_weather.get_weather_field("DateUTC")
    #     # conds = get_weather.get_weather_field("Conditions")
    #     # iterate backwards
    #     for i in range(len(timestampts) - 1, 0, -1):
    #         diff = datetime.strptime(timestampts[i].strip(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(
    #             timestampts[i - 1].strip(), "%Y-%m-%d %H:%M:%S")
    #         minutes = diff.total_seconds() / 60 / timedelta
    #         if minutes > 0:
    #             for j in range(int(minutes) - 1):
    #                 dic[(conds[i], conds[i])] += 1
    # inter_cond(timedelta)

    def majority_cond():
        timestampts = get_weather.get_weather_field("DateUTC")
        # conds = get_weather.get_weather_field("Conditions")
        # iterate backwards
        for i in range(len(timestampts) - 1, 0, -1):
            diff = datetime.strptime(timestampts[i].strip(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(
                timestampts[i - 1].strip(), "%Y-%m-%d %H:%M:%S")
            minutes = diff.total_seconds() / 60 / 60 
            if minutes >= 0:
                dic[(conds[i], conds[i])] += 1
            if minutes < 0:
                for j in range(int(minutes*60) - 1):
                    dic[(conds[i], conds[i])] += 1
    # print len(pairs)
    # print len(Counter(pairs))
    # print sorted(Counter(pairs).items())
    # print dic.keys()
    dic = OrderedDict(sorted(dic.items()))     
    # get the count values
    count_list = dic.values()
    # get the matrix form of counts
    count_matrix = numpy.array(count_list).reshape((len(conds_unique), len(conds_unique)))
    # get sum of each row
    count_row = numpy.sum(count_matrix, axis=0)
    # calculate the prob. of possible changes
    prob_matrix = (count_matrix.T / count_matrix.sum(axis=1)).T
    # set print options of numpy
    numpy.set_printoptions(precision=2, edgeitems=0, threshold=numpy.nan, linewidth=numpy.nan, suppress=True)
    print numpy.diag(prob_matrix)
    return prob_matrix
    # prob_list = [float(i)/len(conds_unique) for i in dic.values()]
    # print prob_list


def interpolate_cond(timedelta=1):
    """ 
    Interpolate weather conditions based on the timedelta it assigned. 
        default timedelta = 1
    @return new condition list
    """
    timestampts = get_weather.get_weather_field("DateUTC")
    conds = get_weather.get_weather_field("Conditions")
    # iterate backwards
    for i in range(len(timestampts) - 1, 0, -1):
        diff = datetime.strptime(timestampts[i].strip(), "%Y-%m-%d %H:%M:%S") - datetime.strptime(
            timestampts[i - 1].strip(), "%Y-%m-%d %H:%M:%S")
        minutes = diff.total_seconds() / 60 / timedelta
        if minutes > 0:
            for j in range(int(minutes)):
                conds.insert(i - 1, conds[i - 1])
    return conds


def get_prob(dt, weather_cond):
    """ 
    Get probability based on datetime and weather condition.
    @Return{float} probability
    """
    dt = datetime.strptime(dt, "%Y-%m-%d %H:%M")
    month = dt.month
    day = dt.day
    hour = dt.hour
    get_weather_data(month, day, hour, range=10)

    print month, day, weather_cond
    pass

def get_weather_data(month, day, hour, range=10):
    """ 
    @TODO
    """
    for t in timestampts:
        t = datetime.strptime(t.strip(), "%Y-%m-%d %H:%M:%S") - timedelta(hours=6)
        if t.month == month and t.day == day and t.hour == hour:
            pass
    pass

def get_solar_field(fieldname):
    """
    Get the list of one column data.
    """
    columns = defaultdict(list)
    with open('total_20_years_solar_with_weather.csv') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
    return columns[fieldname]

def _get_list_counter(lst):
    """ Return a Counter of a list. """
    return Counter(lst)


def _get_unique_list(lst):
    """ Return a sorted unique list. """
    return sorted(list(set(lst)))


def _main():
    # print dict(_get_list_counter(time_gap_stat()))
    #
    # get the weather conditions from weather data file.
    # conds = get_weather.get_weather_field("Conditions")
    # conds_unique = _get_unique_list(conds)
    # with open("./result_data/conds_unique.txt", "w") as output:
    #     output.write(str(conds_unique))

    # ori_matrix = cond_stat(conds)
    # with open("./result_data/ori_matrix.txt", "w") as output:
    #     output.write(str(ori_matrix))
    # numpy.savetxt("./result_data/ori_matrix2.csv", ori_matrix, fmt="%.4f", delimiter=",")
    # print ori_matrix

    # conds = interpolate_cond(timedelta=30)
    # new_matrix = cond_stat(conds)
    # numpy.savetxt("./result_data/new_matrix2.csv", new_matrix, fmt="%.4f", delimiter=",")
    # print new_matrix
    # for i in [1,2,5,10,20,30,40,50,60]:
    # for i in [1]:
        # new_matrix = cond_stat(conds, i)
        # numpy.savetxt("./result_data/new_matrix_" + str(i) + ".csv", new_matrix, fmt="%.4f", delimiter=",")
    # diff_matrix = numpy.subtract(ori_matrix, new_matrix)
    # print diff_matrix
    # print numpy.linalg.eig(diff_matrix)
    # prob = get_prob("2014-09-17 15:00", "Clear")
    # filename = os.path.join(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"))
    filename = os.path.join(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"))
    dic = get_weather.get_dict_data(filename)
    conds = dic["Conditions"]
    print Counter(conds)
    majority_matrix = cond_stat(conds)
    # with open("./result_data/new_majority_matrix.txt", "w") as output:
    #     output.write(str(majority_matrix))
    # numpy.savetxt("./result_data/new_majority_matrix2.csv", majority_matrix, fmt="%.4f", delimiter=",")

    with open("./result_data/normal_matrix.txt", "w") as output:
        output.write(str(majority_matrix))
    numpy.savetxt("./result_data/normal_matrix.csv", majority_matrix, fmt="%.4f", delimiter=",")

if __name__ == '__main__':
    _main()
