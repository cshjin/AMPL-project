from datetime import datetime
from collections import defaultdict, Counter, OrderedDict
import matplotlib.pyplot as plt
import itertools
import numpy
import os
import csv

CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))


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


def stat(lst):
    conds_unique = _get_unique_list(conds)
    # initial the possible outcomes from condition to condition
    conds_pairs = list(itertools.product(conds_unique, repeat=2))
    dic = dict((pair, 0.) for pair in conds_pairs)
    # count consecutive weather conditions
    for i in range(len(conds) - 1):
        if (conds[i], conds[i + 1]) in dic:
            dic[(conds[i], conds[i + 1])] += 1

    dic = OrderedDict(sorted(dic.items()))

    # pass


def _get_unique_list(lst):
    """ Return a sorted unique list. """
    return sorted(list(set(lst)))

filename = os.path.join(os.path.join(CURRENT_FOLDER, "..", "solar_data", "total_20_years_solar_with_weather.csv"))
# filename = os.path.join(os.path.join(CURRENT_FOLDER, "weather_data", "total_20_years_weather.csv"))
dic = get_dict_data(filename)
conds = dic["Conditions"]
# print Counter(conds)
stat(conds)
# majority_matrix = cond_stat(conds)
# with open("./result_data/new_majority_matrix.txt", "w") as output:
#     output.write(str(majority_matrix))
# numpy.savetxt("./result_data/new_majority_matrix2.csv", majority_matrix, fmt="%.4f", delimiter=",")
