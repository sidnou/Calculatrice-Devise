from src.module import devise_api


class CalculManagement(object):
    def __init__(self, currencies=None):
        self.listDeviseRef = ()
        self.currencies = currencies
        self.deviseRef = None
        self.deviseChange = 1
        self.deviseEntree = None
        self.device_ref()


        # self.conversion()

    def device_ref(self):
        self.deviseRef = devise_api.get_rates(self.currencies)

        return self.deviseRef, self.listDeviseRef

    def conversion(self, valeur_entre=0.0, devise_entree=None):
        self.deviseEntree = devise_entree
        valeurDeChange = self.deviseRef[self.deviseEntree]
        return float(valeur_entre) * valeurDeChange

    def liste_devise_ref(self):
        self.deviseRef = devise_api.get_rates(self.currencies)
        self.listDeviseRef = list(self.deviseRef.keys())
        return self.listDeviseRef


if __name__ == '__main__':
    app = CalculManagement()
    print(app.device_ref())
    print(app.liste_devise_ref())

    print(app.conversion(valeur_entre = input('taper nombre: '), devise_entree='USD'))
