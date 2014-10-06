import sscapi
from pylab import *
import json
from datetime import datetime

""" Running SAM models """
ssc = sscapi.PySSC()
dat = ssc.data_create()

ssc.data_set_string(dat, 'file_name', '94846.tm2')
ssc.data_set_number(dat, 'system_size', 10)
ssc.data_set_number(dat, 'derate', 0.77)
ssc.data_set_number(dat, 'track_mode', 0)
ssc.data_set_number(dat, 'azimuth', 180)
ssc.data_set_number(dat, 'tilt_eq_lat', 1)

mod = ssc.module_create("pvwattsv1")

ssc.module_exec(mod, dat)

outData = {}
outData["gh"] = ssc.data_get_array(dat, "gh")
outData["dn"] = ssc.data_get_array(dat, "dn")
outData["df"] = ssc.data_get_array(dat, "df")
outData["tamb"] = ssc.data_get_array(dat, "tamb")
outData["tdew"] = ssc.data_get_array(dat, "tdew")
outData["wspd"] = ssc.data_get_array(dat, "wspd")
outData["poa"] = ssc.data_get_array(dat, "poa")
outData["tcell"] = ssc.data_get_array(dat, "tcell")
outData["dc"] = ssc.data_get_array(dat, "dc")
outData["ac"] = ssc.data_get_array(dat, "ac")
outData["shad_beam_factor"] = ssc.data_get_array(dat, "shad_beam_factor")
outData["sunup"] = ssc.data_get_array(dat, "sunup")
outData["poa_monthly"] = ssc.data_get_array(dat, "poa_monthly")
outData["solrad_monthly"] = ssc.data_get_array(dat, "solrad_monthly")
outData["dc_monthly"] = ssc.data_get_array(dat, "dc_monthly")
outData["ac_monthly"] = ssc.data_get_array(dat, "ac_monthly")
outData["solrad_annual"] = ssc.data_get_number(dat, "solrad_annual")
outData["ac_annual"] = ssc.data_get_number(dat, "ac_annual")
outData["location"] = ssc.data_get_string(dat, "location")
outData["city"] = ssc.data_get_string(dat, "city")
outData["state"] = ssc.data_get_string(dat, "state")
outData["lat"] = ssc.data_get_number(dat, "lat")
outData["lon"] = ssc.data_get_number(dat, "lon")
outData["tz"] = ssc.data_get_number(dat, "tz")
outData["elev"] = ssc.data_get_number(dat, "elev")
# with open("result.json", "w") as outFile:
#     json.dump(outData, outFile, indent=4)

""" plot time series graph """
# plot(outData["ac_monthly"], "*")
# show()


def get_hours_of_year():
    diff = datetime.now() - datetime(year=2014, month=1, day=1)
    return int(diff.total_seconds() / 60 / 60)

def get_weather_data():
	pass
start_index = get_hours_of_year()
# start_index = 4356
print outData["gh"][start_index:]
# plot(outData["gh"][start_index:])
# show()