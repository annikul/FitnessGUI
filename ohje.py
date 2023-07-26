# HELP DIALOG WINDOW
# ==================

# LIBRARIES AND MODULES
from PyQt6 import QtWidgets as QW # UI elements functionality
from PyQt6.uic.load_ui import loadUi # Reads the UI file 

# CLASS DEFINITION
class OpenHelp(QW.QDialog):

    # The constructor
    def __init__(self):
        super().__init__()

        loadUi('ohje.ui', self) # Muista laittaa self. Muuten on virhe mutta ei anna virheilmoitusta
        self.setWindowTitle('Kuntoilusovelluksen ohje') # Otsikko
        self.closePB = self.closePushButton
        self.closePB.clicked.connect(self.closeHelp) # Määritellään kun painetaan ohjeessa sulje se kutsuu metodia closeHelp.

    # Methods ie. slots 
    def closeHelp(self):  # Määritellään metodi
        self.close()