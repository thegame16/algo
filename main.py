import time
from data_engine.data_feed import connect, get_data
from strategy_engine.strategy import generate_signal
from execution_engine.execution import place_trade

SYMBOL = "EURUSD"

connect()

while True:

    df = get_data(SYMBOL)

    signal = generate_signal(df)

    print("Signal:", signal)

    if signal != "HOLD":
        place_trade(SYMBOL, signal)

    time.sleep(60)
