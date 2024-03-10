from typing import Dict
from settings.money_info_code import (
    get_money_usd,
    get_money_eur,
    get_money_kzt,
    get_money_uah,
    get_money_cny,
    get_money_amd,
)

def get_all_money():
    usd = get_money_usd()
    eur = get_money_eur()
    uah = get_money_uah()
    kzt = get_money_kzt()
    cny = get_money_cny()
    amd = get_money_amd()
    return usd,eur,uah,kzt,cny,amd

usd,eur,uah,kzt,cny,amd = get_all_money()

CONVERSION_RATES: Dict[str, Dict[str, float]] = {
    "rub": {
        "eur": 1/float(eur),
        "usd": 1/float(usd),
        "uah": 1/float(uah),
        "kzt": 1/float(kzt),
        "cny": 1/float(cny),
        "amd": 1/float(amd)
    },
    "eur": {
        "rub": float(eur),
        "usd": float(eur)/float(usd),
        "uah": float(eur)/float(uah),
        "kzt": float(eur)/float(kzt),
        "cny": float(eur)/float(cny),
        "amd": float(eur)/float(amd)
    },
    "usd": {
        "rub": float(usd),
        "eur": float(usd)/float(eur),
        "uah": float(usd)/float(uah),
        "kzt": float(usd)/float(kzt),
        "cny": float(usd)/float(cny),
        "amd": float(usd)/float(amd)
    },
    "uah": {
        "rub": float(uah),
        "eur": float(uah)/float(eur),
        "usd": float(uah)/float(usd),
        "kzt": float(uah)/float(kzt),
        "cny": float(uah)/float(cny),
        "amd": float(uah)/float(amd)
    },
    "kzt": {
        "rub": float(kzt),
        "eur": float(kzt)/float(eur),
        "usd": float(kzt)/float(usd),
        "uah": float(kzt)/float(uah),
        "cny": float(kzt)/float(cny),
        "amd": float(kzt)/float(amd)
    },
    "cny": {
        "rub": float(cny),
        "eur": float(cny)/float(eur),
        "usd": float(cny)/float(usd),
        "uah": float(cny)/float(uah),
        "kzt": float(cny)/float(kzt),
        "amd": float(cny)/float(amd)
    },
    "amd": {
        "rub": float(amd),
        "eur": float(amd)/float(eur),
        "usd": float(amd)/float(usd),
        "uah": float(amd)/float(uah),
        "kzt": float(amd)/float(kzt),
        "cny": float(amd)/float(cny)
    }
}

def convert_currency(v1, v2, value):
    try:
        return round(value * CONVERSION_RATES[v1.lower()][v2.lower()], 2)
    except KeyError:
        return None
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        return None
