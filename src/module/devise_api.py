from pprint import pprint

import requests


def get_rates(curencies=None):
    if curencies is not None:
        # Récupération du Taux de change par défaut pour 1 Euro
        r = requests.get(f"https://api.exchangeratesapi.io/latest?symbols={curencies}")
        # Teste la reponse de la demande de l'api
        if r.status_code != 200:
            return print("La valeur entrée n'est pas correcte")
        if not (r or r.json()):
            return False, False
        else:
            api_rates = r.json().get("rates")

            return api_rates
    else:
        r = requests.get("https://api.exchangeratesapi.io/latest")
        if not (r or r.json()):
            return False, False
        api_rates = r.json().get("rates")
        return api_rates


def get_rates_base(base="EUR"):
    rBase = requests.Request("GET", )


#
#  fonction qui ne récupère pas rates
#
# def get_rates_crypto():
#     rCrypto = requests.request("GET","https://api.coinbase.com/v2/exchange-rates")
#     print(type(rCrypto))
#     if not rCrypto and not rCrypto.json():
#         return False, False
#     api_rates_crypto = rCrypto.json().get("rates")
#     return api_rates_crypto


if __name__ == '__main__':
    valeur = get_rates()
    pprint(valeur)
    valeur1 = list(valeur.keys())
    print(valeur1)
    # varleurCrypto = get_rates_crypto()
    # pprint(varleurCrypto)
