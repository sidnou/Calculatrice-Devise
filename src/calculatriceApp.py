from PySide2 import QtWidgets, QtCore, QtGui
from gui.CalculatriceDeviseGUI import Ui_Form
from src.module.calculManager import CalculManagement


class FenetrePrincipale(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(FenetrePrincipale, self).__init__()

        self.setupUi(self)
        self.show()
        self.setupConnections()








# Fonction d'action

    def setupConnections(self):
        print('clique bouton')
        self.btn_0.clicked.connect(self.teste)

    def conversionDevise(self, valeur_entree, devise_entree):
        CalculManagement.conversion(valeur_entree, devise_entree)
    def teste(self):
        print('tteste')

app = QtWidgets.QApplication()
fenetre = FenetrePrincipale()
app.exec_()
