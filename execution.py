import MetaTrader5 as mt5

def place_trade(symbol, signal, lot=0.1):

    tick = mt5.symbol_info_tick(symbol)

    if signal == "BUY":
        price = tick.ask
        order_type = mt5.ORDER_TYPE_BUY

    elif signal == "SELL":
        price = tick.bid
        order_type = mt5.ORDER_TYPE_SELL

    else:
        return

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 100,
        "comment": "AlgoBot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)

    print(result)
