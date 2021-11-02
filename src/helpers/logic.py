import sys
import os
import json
import numpy as np

from redisClient import redisInterface
from taLibHelpers import *


rd = redisInterface("history-redis-python-replica",6379)

def convertToArray(opens,highs,lows,closes):
    return [
        np.array(opens, dtype="float64"),
        np.array(highs, dtype="float64"),
        np.array(lows, dtype="float64"),
        np.array(closes, dtype="float64"),
    ]

def routine(hashkey):
    candles = rd.getCandles(hashkey)
    if candles != None:
        close = []
        open = []
        high = []
        low = []
        date = []
        sortedDict = dict(sorted(candles.items()))
        for i in sortedDict:
            close.append(eval(sortedDict[i])[4])
            open.append(eval(sortedDict[i])[1])
            high.append(eval(sortedDict[i])[2])
            low.append(eval(sortedDict[i])[3])
            date.append(eval(sortedDict[i])[0])
        ### talib expects numpy standard array
        npar = convertToArray(open,high,low,close)
        publishables = []
        publishables.append(doStochOvers(npar[1], npar[2], npar[3], hashkey, date))
        return [x for x in publishables if x is not None]

def doStochOvers(h,l,c, hashkey,date):
    _stochastic = stochastic(h,l,c)
    slowd_last_index = _stochastic['slowd'][-1]
    if(slowd_last_index>80 or slowd_last_index<20):
        return {
            "key": hashkey,
            "base_indicator": "stochastic",
            "type": "overbought" if slowd_last_index>80 else "oversold",
            "interval": hashkey.split("-")[1],
            "ticker": hashkey.split("-")[0],
            "location": date[-1]
        }
    return None

def scanThat(stoch):
    print("gonna scan that")