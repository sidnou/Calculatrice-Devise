
from src.module import devise_api


class CalculManager(object):
    def __init__(self, currencies=None):
        self.currencies = currencies
        self.deviseRef = None
        self.deviseChange = 1
        self.deviseEntree = None
        self.device_ref()
        # self.conversion()

    def device_ref(self):
        self.deviseRef = devise_api.get_rates(self.currencies)

        return self.deviseRef

    def conversion(self, valeur_entre=0, devise_entree=None):
        self.deviseEntree = devise_entree
        valeurDeChange = self.deviseRef[self.deviseEntree]
        resultat = valeur_entre * valeurDeChange
        return resultat


if __name__ == '__main__':
    app = CalculManager()
    print(app.device_ref())

    print(app.conversion(valeur_entre=1, devise_entree='CAD'))
