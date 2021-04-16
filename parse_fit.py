from fitparse import FitFile
import datetime
import numpy as np
''' 
 * cadence: 79 rpm
 * calories: 133 kcal
 * distance: 0.0 m
 * heart_rate: 156 bpm
 * left_right_balance: 0
 * power: 173 watts
 * temperature: 23 C
 * timestamp: 2021-03-08 06:33:57
'''

def getPower(filename):
    time = []
    data = []
    fitfile = FitFile(filename)
    init = True
    # Get all data messages that are of type record
    for record in fitfile.get_messages('record'):
        # Go through all the data entries in this record
        for record_data in record:
            if record_data.name == "timestamp":
                time.append(record_data.value)
            if record_data.name == "power" :
                data.append(record_data.value)
    return [time, data]


def getTime(filename):
    data = []
    fitfile = FitFile(filename)
    # Get all data messages that are of type record
    for record in fitfile.get_messages('record'):
        # Go through all the data entries in this record
        for record_data in record:
            if record_data.name == "timestamp" :
                data.append(record_data.value)
                break
                #print(record_data.value)
    return data


def add_zero(p1, p2):
    end1 = p1[0][-1]
    end2 = p2[0][-1]
    endtime = end2
    if end1 > end2:
        endtime = end1

    begin1 = p1[0][0]
    begin2 = p2[0][0]
    begintime = begin2
    if begin1 < begin2:
        begintime = begin1

    length = (int) ((endtime - begintime) / datetime.timedelta(seconds=1))
    print(length)
    result1 = np.zeros(length)
    result2 = np.zeros(length)
    index = 0
    current_time = begintime
    while current_time <= endtime:
        try:
            i1 = p1[0].index(current_time)
            result1[index] = p1[1][i1]
        except:
            print('index not in range')

        try:
            i2 = p2[0].index(current_time)
            result2[index] = p2[1][i2]
        except:
            print('index not in range')

        index += 1
        current_time += datetime.timedelta(seconds=1)

    return result1, result2


def moving_3sec_avg(power, time=3):
    result = np.zeros(len(power))
    padding = np.zeros(time-1)
    power = np.concatenate((padding, power))
    for i in range(0, len(power)-time):
        avg = np.average(power[i:i+time])
        result[i] = avg
    return result
