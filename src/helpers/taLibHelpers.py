import talib

def rsi(close, timeperiod=14):
    try:
        real = talib.RSI(close, timeperiod)
        return real
    except Exception as e:
        print(e)
        return None

def macd(close, fastperiod=12, slowperiod=26, signalperiod=9):
    try:
        macd, macdsignal, macdhist = talib.MACD(close, fastperiod, slowperiod, signalperiod)
        return {"macd":macd, "macdsignal":macdsignal, "macdhist":macdhist}
    except Exception as e:
        print(e)
        return None

def adx(high, low, close, timeperiod=14):
    try:
        real = talib.ADX(high, low, close, timeperiod)
        return real
    except Exception as e:
        print(e)
        return None

def ema(close, period=30):
    try:
        real = talib.EMA(close, period)
        return real
    except Exception as e:
        print(e)
        return None

def stochastic(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0,slowd_period=3,slowd_matype=0):
    try:
        slowk, slowd = talib.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)
        return {"slowk":slowk, "slowd":slowd}
    except Exception as e:
        print(e)
        return None