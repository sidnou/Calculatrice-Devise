from PySide2 import QtWidgets, QtCore
from gui.CalculatriceDeviseGUI import Ui_Form


class FenetrePrincipale(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(FenetrePrincipale, self).__init__()

        self.setupUi(self)
        self.show()







app = QtWidgets.QApplication()
fenetre = FenetrePrincipale()
app.exec_()
