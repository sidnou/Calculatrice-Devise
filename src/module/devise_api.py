from pprint import pprint

import requests


def get_rates(currencies):
    # Récupération du Taux de change par défaut pour 1 Euro
    r = requests.get(f"https://api.exchangeratesapi.io/latest?symbols={currencies}")
    if not r and not r.json():
        return False, False

    api_rates = r.json().get("rates")
    valeur_rates = api_rates[currencies]
    return valeur_rates


if __name__ == '__main__':
    valeur = get_rates(currencies="USD")
    print(type(valeur))