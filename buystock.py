import pandas as pd
import math
from time import sleep
global money
from stockname import Stockname
stock_price = []
stock = Stockname
data = pd.read_csv(stock)
data = data[["counter", "middle_band"]]
data["future"] = data["middle_band"].shift(-1)
data.dropna(inplace=True)

going_up = []
going_down = []

counter = 1
stocks = {"stock": 0}
history = []

stock_inf = {
    "bought_price": 0,
    "sell_price": 0,
    "amount_bought":0,
    "money":0
}


def Buy(cash, price):
    if cash > price:
        max_stocks = math.trunc(cash / price)
        cash -= max_stocks * price
        stocks["stock"] += max_stocks
        
    return cash


def Sell(price):
    return price * stocks["stock"]

#print(data)

#print(data.count()["counter"])

transactions = 0
money = 10000
price_bought = 0
for counter in range(data.count()["counter"]):
    current, future = data["middle_band"][counter], data["future"][counter]

    if current - future < 0 and stocks["stock"] == 0:
        money = Buy(round(money, 2), round(future, 2))
        transactions += 1
        #print(stocks["stock"], future)
        going_up.append(([counter+1], [future]))
    elif current - future >= 0 and stocks["stock"] != 0:
        ret = Sell(float(future))
        stocks["stock"] = 0
        money += ret 
        transactions += 1
        #print("sold", money)
        going_down.append(([counter+ 1], [future]))
    
    stock_inf["bought_price"],stock_inf["sell_price"],stock_inf["amount_bought"],stock_inf["money"] = current,0,stocks["stock"],money
    history.append(stock_inf)

    counter += 1


    
ret = Sell(float(future))
stocks["stock"] = 0
money += ret
#print(stocks)
#print(transactions)
#print(history)
"""print(going_up)
print(going_down)"""