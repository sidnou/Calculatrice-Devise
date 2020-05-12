import os
from src.module.devise_api import get_rates


def devise_today(self):
    pass


def conversion_devise(sefl, devise_value, devise_ref):
    resultDevise = devise_value * devise_ref
    return resultDevise


if __name__ == '__main__':
    conversion_devise()