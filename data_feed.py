import MetaTrader5 as mt5
import pandas as pd

def connect():

    if not mt5.initialize():
        print("MT5 initialization failed")
        quit()

    print("Connected to MetaTrader 5")

def get_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M1, bars=200):

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)

    df = pd.DataFrame(rates)

    df['time'] = pd.to_datetime(df['time'], unit='s')

    return df
