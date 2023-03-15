import json
import requests

def get_data(key):
    data = requests.get(key)  
    return data.json()

def main():

    ETHUSDT = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    BTCUSDT = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'    
    ETHBTC = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC'
    result = []
    data = get_data(ETHUSDT)
    result.append(data['price'])
    data = get_data(BTCUSDT)
    result.append(data['price'])    
    data = get_data(ETHBTC)
    result.append(data['price'])

    return result

def get_procents(price, price_now):
    difference = price - price_now
    procent = difference * 100 / price
    return procent


def get_real_price(price, start_price):
    ETHBTC_procent = get_procents(float(start_price[2]), float(price[2]))
    difference = float(start_price[0]) - float(price[0])   
    result = difference / 100 * (100+ETHBTC_procent)
    return float(price[0]) - difference + result
    


if __name__ == '__main__':
    start_price = main()
    ETHUSDT_price = float(start_price[0])
    next_price = main()
    start_real_price = get_real_price(next_price, start_price)
    
    old_price = next_price
    #for i in range(600):
    while True:
        price_now =  main()
        
        now_real_price = get_real_price(price_now, old_price)
        procents = get_procents(start_real_price, now_real_price)
        
        print(i, now_real_price, procents)
        if procents >= 1:
            print('Price Up')
            print(now_real_price, procents)
            start_real_price = now_real_price

        if procents <= -1:
            print('Price Down')
            print(now_real_price, procents)
            start_real_price = now_real_price


       