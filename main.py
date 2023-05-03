# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# Käytetään C-tyyppistä muuttujen nimeämistä metodin nimi on calculate ja All isolla ei tule aliviivoja

# LIBRARIES AND MODULES
import sys # For system arguments if needed to run the app
from PyQt6 import QtCore  # Core functionality of Qt # Kirjastosta PyQt6 otetaan komponentti QtCore
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi # Reads the UI file 
import kuntoilija # Home brew module for athlete
import timetools # DIY module for date and time calculations
# TODO: Import some library able to plot trends and make it as widgets in the UI

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):   # Luokka alkaa aina isolla(MainWindow) ja koska se perii niin toisiin sulkuihin(QtWidgets.QMainWindow)(tehty ikkuna designilla) jos ei perisi mitään otetaan toiset ()pois
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):  # argumentteja init ja self
        super().__init__()

        # Load the UI file  (UI file = käyttöliittymä)
        self.main = loadUi('main.ui', self)  # Tämän takia python ei tiedä objektien nimiä joten ei tule valmiit tekstejä eikä värit kerro oletko kirjoittanut väärin. 

        # Define UI Controls ie buttons and input fields
        # self.nameLE = self.nameLineEdit   # tulee tekstiä. Tällä toimii. Alla toinen vaihtoehto
        self.nameLE = self.findChild(QtWidgets.QLineEdit, 'nameLineEdit') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia 
        self.nameLE.textEdited.connect(self.activateCalculatePB) # Nyt kun nimikenttää muokataan se kutsuu funktiota activateCalculatePB. Alhaalla tallennanappula menee päälle.
       
        self.birthDateE = self.birthDateEdit  # ensimmäinen self.keksitty
        self.birthDateE.dateChanged.connect(self.activateCalculatePB) # Nyt kun syntymäaikaa muokataan se kutsuu funktiota activateCalculatePB. Alhaalla tallennanappula menee päälle.
        self.genderCB = self.genderComboBox     # Toinen self.Qtdesigneriin laittamasi
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB) # Nyt kun sukupuolta muokataan se kutsuu funktiota activateCalculatePB. Alhaalla tallennanappula menee päälle.
        self.weighingDateE = self.weighingDateEdit

        # Set the weighing date to the current date
        self.weighingDateE.setDate(QtCore.QDate.currentDate()) # Tämä on kuluva päivä
        self.heightSB = self.heightSpinBox  # ensimmäinen self.keksitty
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.weightSpinBox  # Toinen self.Qtdesigneriin laittamasi
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB = self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self.waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipSB = self.hipSpinBox
        self.hipSB.setEnabled(False)
        self.hipSB.valueChanged.connect(self.activateCalculatePB)

        # self.calculatePB = self.calculatePushButton # Tällä toimii kanssa. Alupuolella vaihtoehto. (Olion ominaisuus calculatePB ja oikeasti nappula on calculatePushButton)
        self.calculatePB = self.findChild(QtWidgets.QPushButton, 'calculatePushButton') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia 
        self.calculatePB.clicked.connect(self.calculateAll) # self.calculatePB.clicked.connect käynnistää oliosta jonka nimeä ei vielä tiedetä self.calculateAll (calculateAll = funktio)
        self.calculatePB.setEnabled(False)

        # self.savePB = self.savePushButton # Tällä toimii kanssa. Alupuolella vaihtoehto
        self.savePB = self.findChild(QtWidgets.QPushButton, 'savePushButton') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia
        self.savePB.clicked.connect(self.saveData) 
        self.savePB.setEnabled(False) # pisti harmaaksi tallennus nappulan

    # Define slots ie methods
    def activateCalculatePB(self): # Laskenappula aktivoituu vasta kun kaikki tiedot on laitettu!
        self.calculatePB.setEnabled(True) # Aktivoi laskenappulan kun.....?????
        if self.nameLE.text() == '':  # Jos nimikenttä on tyhjä laskenappula ei mene päälle
            self.calculatePB.setEnabled(False) # laskenappula ei mene päälle

        if self.birthDateE.date() == QtCore.QDate(1900, 1,1):  # QtCoresta otetaan tietotyyppi QDate # Jos syntymäaika ei ole muutettu laskenappula ei mene päälle
            self.calculatePB.setEnabled(False) 

        if self.genderCB.currentText() == '':  # Jos sukupuolikenttä on tyhjä laskenappula ei mene päälle
            self.calculatePB.setEnabled(False)  
        
        if self.heightSB.value() == 100:
            self.calculatePB.setEnabled(False) 

        if self.weightSB.value() == 20:
            self.calculatePB.setEnabled(False) 
        
        if self.neckSB.value() == 10:
            self.calculatePB.setEnabled(False) 

        if self.waistSB.value() == 30:
            self.calculatePB.setEnabled(False) 
        
        if  self.genderCB.currentText() == 'Nainen': # Naisen kohdalla pitää olla lantiokohta täytetty
            self.hipSB.setEnabled(True) # lantio kohta tulee näkyviin vain jos on naine

            if self.hipSB.value() == 50:
                self.calculatePB.setEnabled(False)
        else:
            self.hipSB.setEnabled(False) # Miehelle ei tule lantiokohtaa

    # Calculates BMI, finnish and US fat percentages andik updates corresponding labels
    def calculateAll(self):   # EI anneta argumentteja
        name = self.nameLE.text()
        height = self.heightSB.value() # Spinbox value as an integer
        weight = self.weightSB.value()
        self.calculatePB.setEnabled(False) # Laskenappula menee harmaaksi kun lasku on laskettu
        self.savePB.setEnabled(True) # Tallennanappulaa voi painaa kun tulos on laskettu

        # Convert birthday to ISO string using QtCore's methods
        birthday = self.birthDateE.date().toString(format=QtCore.Qt.DateFormat.ISODate)
        
        # Set Gender Value according to ComboBox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1

        else:
            gender = 0

        # Convert Weighing day to ISO string
        dateOfWeighing = self.weighingDateE.date().toString(format=QtCore.Qt.DateFormat.ISODate)
        
        # Calculate time difference using our home made tools
        age = timetools.datediff2(birthday, dateOfWeighing, 'year') # Laskee iän. Syntymä aika - punnituspäivä
        

        neck = self.neckSB.value() # Koska nämä ovat SpinBoxeja ei arvoa tarvitse muuttaa luvuksi koska ne ovat suoraan lukuja
        waist = self.waistSB.value()
        hip = self.hipSB.value()

        if age >= 18: # Jos ikä on 18v tai enempi lasketaan tulos Kuntoilija laskukaavalla
            # Create an athlete from Kuntoilija class for age 18 or above
            athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, dateOfWeighing) # athlete on sisäinen muuttuja???
           
        else:
            # Create the athlete from JuniorKuntoilija class for age under 18
            athlete = kuntoilija.JunioriKuntoilija(name, height, weight, age, gender) # Jos ikä on alle 18v. lasketaan tulos JuniorKuntoilijan laskukaavalla

        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi)) # Kun nappulaa painetaan tehdään tämä

        fiFatPercentage = athlete.rasvaprosentti #fiFatPercentage = muuttuja eli keksitty. 

        if gender == 1:
            usaFatPercentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)

        else:
            usaFatPercentage = athlete.usa_rasvaprosentti_nainen(height, waist, hip, neck)

        # Set fat percentage labels
        self.fatFiLabel.setText(str(fiFatPercentage)) # muutetaan numeroista merkkijonoksi joten lissää () sisään (str())
        self.fatUsaLabel.setText(str(usaFatPercentage))

    def constructData(self, athlete, fiFat, usaFat):
        # A dictionary for single weighing of an athlete
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino, 
                    'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva,
                    'bmi': athlete.bmi, 'rasvaprosenttiFi': fiFat, 'rasvaprosenttiUs': usaFat } 
        # athlete on olio jossa on kaikki minkä edessä lukee athlete. 
        # Fi ja Usa rasvaprosentissa ei ole edessä athlete koska ne eivät ole oliossa vaan olion metodissa
        return athlete_data_row
    

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