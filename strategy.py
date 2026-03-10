import pandas as pd

def generate_signal(df):

    df['ma_fast'] = df['close'].rolling(10).mean()
    df['ma_slow'] = df['close'].rolling(30).mean()

    if df['ma_fast'].iloc[-1] > df['ma_slow'].iloc[-1]:
        return "BUY"

    elif df['ma_fast'].iloc[-1] < df['ma_slow'].iloc[-1]:
        return "SELL"

    return "HOLD"
