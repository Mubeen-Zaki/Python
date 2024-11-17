import requests

def get_stock(name):
    try:
        url = f"https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice%2CHighLow&query={name}"
        response = requests.get(url)
        obj = response.json()
        if obj['success'] and 'data' in obj:
            data = obj['data']['data']
            return_obj = []
            for stock in data:
                obj = {}
                obj['name'] = stock['Name']
                obj['symbol'] = stock['Symbol']
                obj['market_cap'] = stock['MarketCap']
                obj['curr'] = stock['CurrentPrice']
                obj['high/low'] = stock['HighLow']
                return_obj.append(obj)
            return return_obj
    except Exception as e:
        return str(e)

def pretty_print(objs):
    print("*" * 100)
    for obj in objs:
        print(f"\n Stock Name : {obj['name']} \n")
        print(f"\n Stock Symbol : {obj['symbol']} \n")
        print(f"\n Market Cap : {obj['market_cap']} \n")
        print(f"\n Current : {obj['curr']} \n")
        print(f"\n High-Low : {obj['high/low']} \n")
        print("*" * 100)

def process(text):
    num = ''
    for i in text:
        if i.isnumeric():
            num += i
    return int(num)

def process_HL(hl):
    list = hl.split('/')
    return process(list[0]), process(list[1])

def analyze_stock(curr,hl):
    curr = process(curr)
    high, low = process_HL(hl)
    if (curr - high >= 0):
        print("\n Best Time to Buy this STOCK! \n")
    elif curr > low:
        print("\n Stable \n")
    else:
        print("\n Stock is performing really bad! \n")

def main():
    while True:
        print("\n ****** View and analyze Stocks ****** \n")
        name = input("Enter name : ").strip().lower()
        try:
            obj = get_stock(name)
            if type(obj) == str:
                print("\n Error in fetching stock details.... \n")
                choice = input("\n Do you want to exit? (Y/N) \n").strip().lower()
                if choice == 'y':
                    break
                continue
            pretty_print(obj)
            choice = input("\n Do you want to Analyze stock? (Y/N) \n").strip().lower()
            if choice == 'y':
                analyze_stock(obj[0]['curr'],obj[0]['high/low'])
            choice = input("\n Do you want to exit? (Y/N) \n").strip().lower()
            if choice == 'y':
                break

        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    main()
