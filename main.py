# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# Käytetään C-tyyppistä muuttujen nimeämistä metodin nimi on calculate ja All isolla ei tule aliviivoja

# LIBRARIES AND MODULES
import sys # For system arguments if needed to run the app
from PyQt6 import QtCore  # Core functionality of Qt # Kirjastosta PyQt6 otetaan komponentti QtCore
from PyQt6 import QtWidgets as QW # UI elements functionality
from PyQt6.uic.load_ui import loadUi # Reads the UI file 
import kuntoilija # Home brew module for athlete
import timetools # DIY module for date and time calculations
import athleteFile # Home made module for processing data files
# TODO: Import some library able to plot trends and make it as widgets in the UI

# Class for the main window
class MainWindow(QW.QMainWindow):   # Luokka alkaa aina isolla(MainWindow) ja koska se perii niin toisiin sulkuihin(QtWidgets.QMainWindow)(tehty ikkuna designilla) jos ei perisi mitään otetaan toiset ()pois
    
    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):  # argumentteja init ja self
        super().__init__()

        # Load the UI file  (UI file = käyttöliittymä)
        self.main = loadUi('main.ui', self)  # Tämän takia python ei tiedä objektien nimiä joten ei tule valmiit tekstejä eikä värit kerro oletko kirjoittanut väärin. 

        # Define UI Controls ie buttons and input fields
        # self.nameLE = self.nameLineEdit   # tulee tekstiä. Tällä toimii. Alla toinen vaihtoehto
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia 
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
        self.hipsSB = self.hipsSpinBox
        self.hipsSB.setEnabled(False)
        self.hipsSB.valueChanged.connect(self.activateCalculatePB)

        # Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar() # statusBar on olio
        self.setStatusBar(self.statusBar) # Tässä kutsutaan statusBar oliota
        self.statusBar.show() # Oletus on että statusBar ei näy ja tällä sen saa näkyviin.

        # self.calculatePB = self.calculatePushButton # Tällä toimii kanssa. Alupuolella vaihtoehto. (Olion ominaisuus calculatePB ja oikeasti nappula on calculatePushButton)
        self.calculatePB = self.findChild(QW.QPushButton, 'calculatePushButton') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia 
        self.calculatePB.clicked.connect(self.calculateAll) # self.calculatePB.clicked.connect käynnistää oliosta jonka nimeä ei vielä tiedetä self.calculateAll (calculateAll = funktio)
        self.calculatePB.setEnabled(False)

        # self.savePB = self.savePushButton # Tällä toimii kanssa. Alupuolella vaihtoehto
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton') # findChild tekee että osaa ehdottaa joitakin metodeja/ominaisuuksia
        self.savePB.clicked.connect(self.saveData) 
        self.savePB.setEnabled(False) # pisti harmaaksi tallennus nappulan

        # Read data from file and save it to a list
        self.dataList = []   # datalist = muuttuja, oma keksimä. = [] eli määritellään että lista on tyhjä. Luetaan tiedosto datalistaan 
        jsonFile = athleteFile.ProcessJsonFile() # Kutsutaan 
        try:
            data = jsonFile.readData('athleteData.json')
            self.dataList = data[3] 
        except Exception as e:
            data = (1, 'Error', str(e), self.dataList)  # Palauttaa virhekoodin, virheselitys, yksityiskohtaisen virhekuvauksen ja datan.
        # Joka kerta kun softa käynnistetään uudestaan. Vanhojen mittojen perään tulee aina uudet mitat
    

        # Define slots ie methods

# Create a alerting method
    def alert(self, message, detailedMessage):
        msgBox = QW.QMessageBox() # Luodaan ensiksi tyhjä olio
        msgBox.setIcon(QW.QMessageBox.critical) # Asetetaan arvoja
        msgBox.setWindowTitle('Tapahtui vakava virhe') # Yleiskäyttöinen viesti
        msgBox.setText(message) # Välitetään message argumentti
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def activateCalculatePB(self): # Laskenappula aktivoituu vasta kun kaikki tiedot on laitettu!
        self.calculatePB.setEnabled(True) # Aktivoi laskenappulan
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
            self.hipsSB.setEnabled(True) # lantio kohta tulee näkyviin vain jos on naine

            if self.hipsSB.value() == 50:
                self.calculatePB.setEnabled(False)
        else:
            self.hipsSB.setEnabled(False) # Miehelle ei tule lantiokohtaa

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
        hips = self.hipsSB.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, neck, waist, hips, dateOfWeighing)

        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi)) # Kun nappulaa painetaan tehdään tämä

        fiFatPercentage = athlete.fi_rasva #fiFatPercentage = muuttuja eli keksitty. athleten alta otetaan fi_rasva
        usaFatPercentage = athlete.usa_rasva # athleten alta otetaan usa_rasva

        # Set fat percentage labels
        self.fatFiLabel.setText(str(fiFatPercentage)) # muutetaan numeroista merkkijonoksi joten lisää () sisään (str())
        self.fatUsaLabel.setText(str(usaFatPercentage))

        self.dataRow = self.constructData(athlete) # athlete = muuttuja.constructData funktio palauttaa athlete datan oliomuodossa. Rivit 155-160 tekevät tämän.
        print(self.dataRow) # Tällä voidaan testata että dictionary näyttä järkevältä

    def constructData(self, athlete):  # athlete on olio jossa on kaikki minkä edessä lukee athlete. 
        # A dictionary for single weighing of an athlete
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino, 
                    'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva,
                    'bmi': athlete.bmi, 'rasvaprosenttiFi': athlete.fi_rasva, 'rasvaprosenttiUs': athlete.usa_rasva} 
        return athlete_data_row     
    
    # Saves data to disk
    def saveData(self): 

        # Add current values to a list
        self.dataList.append(self.dataRow)

        # Save list to a json file
        jsonfile2 = athleteFile.ProcessJsonFile()
        status = jsonfile2.saveData('athleteData.json', self.dataList)
        
        # Show message about status of saving on statusbar
        self.statusBar.showMessage(status[1], 4000)

        # TODO: Call error message box if error code is not 0
        if status[0] != 0:  # Jos status on 0 kutsutaan metodia
            self.alert(status[1], status[2]) # Jos status on 1 tai 2 tulee error koodi
        else: 
            # Set all inputs to their default values
            self.nameLE.clear() # Kun käyttäjä on tallentanut tiedot. Palaa kaikki kohdat alkupisteeseen
            zeroDate = QtCore.QDate(1900, 1, 1)
            self.birthDateE.setDate(zeroDate)
            self.heightSB.setValue(100)
            self.weightSB.setValue(20)
            self.neckSB.setValue(10)
            self.waistSB.setValue(30)
            self.hipsSB.setValue(50)
            self.savePB.setEnabled(False)

if __name__ == "__main__":
    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion') # Use fusion style 
   
    # Create the main window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())