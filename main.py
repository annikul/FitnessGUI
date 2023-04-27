# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# Käytetään C-tyyppistä muuttujen nimeämistä metodin nimi on calculate ja All isolla ei tule aliviivoja

# LIBRARIES AND MODULES
import sys
from PyQt6 import QtCore  # Core functionality of Qt # Kirjastosta PyQt6 otetaan komponentti QtCore
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi
import kuntoilija

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):   # Luokka alkaa aina isolla(MainWindow) ja koska se perii niin toisiin sulkuihin(QtWidgets.QMainWindow)(tehty ikkuna designilla) jos ei perisi mitään otetaan toiset ()pois
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):  # argumentteja init ja self
        super().__init__()

        # Load the UI file  (UI file = käyttöliittymä)
        self.main = loadUi('main.ui', self)  # Tämän takia python ei tiedä objektien nimiä joten ei tule valmiit tekstejä eikä värit kerro oletko kirjoittanut väärin. 

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.nameLineEdit   # tulee tekstiä
        self.birthDay = self.birthDateEdit
        self.genderCB = self.genderComboBox
        self.weighingDate = self.weighingDateEdit
        self.heightSB = self.heightSpinBox
        self.weightSB = self.weightSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.hipSB = self.hipSpinBox

        self.calculatePB = self.calculatePushButton  # Olion ominaisuus calculatePB ja oikeasti nappula on calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll) # self.calculatePB.clicked.connect käynnistää oliosta jonka nimeä ei vielä tiedetä self.calculateAll (calculateAll = funktio)

        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie methods

    # Calculates BMI, finnish and US fat percentages and updates corresponding labels
    def calculateAll(self):   # EI anneta argumentteja
        height = self.heightSB.value() # Spinbox value as an integer
        weight = self.weightSB.value()
        age = 100
        gender = self.genderCB.currentText()
        dateOFWeighing = str(self.weighingDate.date().getDate())

        # create an athlete from Kuntoilija class
        #athlete = kuntoilija.Kuntoilija()
        #bmi = athlete.bmi
       
        self.bmiLabel.setText(dateOFWeighing) # Kun nappulaa painetaan tehdään tämä

    # Saves data to disk
    def saveData(self):     # metodi joka ei vielä tee mitään
        pass

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())