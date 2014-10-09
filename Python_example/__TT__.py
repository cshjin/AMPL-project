from datetime import datetime
from collections import defaultdict
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


def main():
    filename = os.path.join(os.path.join(CURRENT_FOLDER, "solar_data", "total_20_years_solar_with_weather.csv"))
    dic = get_dict_data(filename)
    print dic.keys()

if __name__ == '__main__':
    main()
