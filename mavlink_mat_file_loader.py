from scipy.io import loadmat
import numpy as np
import datetime
import pandas as pd
import numpy as np


def data(datafile,params):
    data = loadmat(datafile)

    label = []
    for i in range(len(params)):
        label.append(params[i].split("_")[0] + '_label')

    dt = {}
    for i in range(len(params)):
        dt[str(params[i])] = {}
        for j in range(len(data[str(label[i])])):
            dt[str(params[i])][str(data[str(label[i])][j]).split("'")[1]] = data[str(params[i])][0:len(data[str(params[i])]),j]

    return dt

def datetime_info(datafile):
    
    data = loadmat(datafile)

    flightdatetime = datetime.datetime.strptime(datafile[0:19], '%Y-%m-%d %H-%M-%S')
    missionstarttime = flightdatetime + datetime.timedelta(microseconds=data['AHR2'][0,1])
    missionendtime = flightdatetime + datetime.timedelta(microseconds=data['AHR2'][len(data['AHR2'])-1,1])
    missionduration = missionendtime - missionstarttime

    return (flightdatetime,missionduration,missionstarttime,missionendtime)

def timedata(datafile,params):
    data = loadmat(datafile)

    flightdatetime = datetime.datetime.strptime(datafile[0:19], '%Y-%m-%d %H-%M-%S')
    missionstarttime = flightdatetime + datetime.timedelta(microseconds=data['AHR2'][0,1])

    time = {}

    for i in range(len(params)):
        time[str(params[i])] = []
        for j in range(len(data[str(params[i])])):
            # time[str(params[i])].append(str((missionstarttime + datetime.timedelta(microseconds=data[str(params[i])][j,1])).time()))
            time[str(params[i])].append((missionstarttime + datetime.timedelta(microseconds=data[str(params[i])][j,1])))
        time[str(params[i])] = np.array(time[str(params[i])])

    return time

def label(datafile,params):
    data = loadmat(datafile)

    label = []
    for i in range(len(params)):
        label.append(params[i].split("_")[0] + '_label')

    dt = {}
    for i in range(len(params)):
        dt[str(params[i])] = {}
        for j in range(len(data[str(label[i])])):
            dt[str(params[i])][str(data[str(label[i])][j]).split("'")[1]] = data[str(params[i])][0:len(data[str(params[i])]),j]

    lab = {}
    for i in range(len(params)):
        lab[str(params[i])] = list(dt[str(params[i])].keys())

    lab = pd.DataFrame({key: pd.Series(value) for key, value in lab.items()})
    lab = pd.DataFrame.map(lab,lambda x: '' if pd.isna(x) else x)

    return lab

def label(datafile,params):
    data = loadmat(datafile)

    label = []
    for i in range(len(params)):
        label.append(params[i].split("_")[0] + '_label')

    dt = {}
    for i in range(len(params)):
        dt[str(params[i])] = {}
        for j in range(len(data[str(label[i])])):
            dt[str(params[i])][str(data[str(label[i])][j]).split("'")[1]] = data[str(params[i])][0:len(data[str(params[i])]),j]

    lab = {}
    for i in range(len(params)):
        lab[str(params[i])] = list(dt[str(params[i])].keys())

    lab = pd.DataFrame({key: pd.Series(value) for key, value in lab.items()})
    lab = pd.DataFrame.map(lab,lambda x: '' if pd.isna(x) else x)

    return lab
