import requests

def  get_money_usd():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_usd = data_money['Valute']['USD']['Value']
        return f"{round(data_money_usd,2)}"    

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def  get_money_eur():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_eur = data_money['Valute']['EUR']['Value']
        return f"{round(data_money_eur,2)}"      

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def  get_money_uah():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_uah = data_money['Valute']['UAH']['Value']
        short_v_uah = data_money_uah/10
        return f"{round(short_v_uah,2)}"      

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def  get_money_kzt():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_kzt = data_money['Valute']['KZT']['Value']
        short_v_kzy = data_money_kzt/100
        return f"{round(short_v_kzy,2)}"      

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
        
def  get_money_cny():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_cny = data_money['Valute']['CNY']['Value']
        return f"{round(data_money_cny,2)}"      

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def  get_money_amd():
    try:
        data_money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        data_money_amd = data_money['Valute']['AMD']['Value']
        short_v_amd = data_money_amd/100
        return f"{round(short_v_amd,2)}"      

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def  get_btc_info():
    try:
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        response_json = response.json()
        return f"{response_json['bpi']['USD']['rate']}$"

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
