# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(20, 30, 281, 21))
        self.nameLineEdit.setToolTip("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 10, 58, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 130, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 130, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 130, 58, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 10, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label.setObjectName("label")
        self.bmiLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmiLabel.setGeometry(QtCore.QRect(20, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bmiLabel.setFont(font)
        self.bmiLabel.setObjectName("bmiLabel")
        self.fatUsaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatUsaLabel.setGeometry(QtCore.QRect(160, 270, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fatUsaLabel.setFont(font)
        self.fatUsaLabel.setObjectName("fatUsaLabel")
        self.fatFiLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(20, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 250, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(160, 250, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(480, 10, 81, 16))
        self.label_14.setObjectName("label_14")
        self.birthDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.birthDateEdit.setGeometry(QtCore.QRect(330, 30, 110, 22))
        self.birthDateEdit.setCalendarPopup(True)
        self.birthDateEdit.setDate(QtCore.QDate(1900, 1, 1))
        self.birthDateEdit.setObjectName("birthDateEdit")
        self.genderComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.genderComboBox.setGeometry(QtCore.QRect(480, 30, 151, 22))
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.weighingDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.weighingDateEdit.setGeometry(QtCore.QRect(20, 90, 110, 22))
        self.weighingDateEdit.setCalendarPopup(True)
        self.weighingDateEdit.setObjectName("weighingDateEdit")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(20, 150, 62, 22))
        self.heightSpinBox.setDecimals(2)
        self.heightSpinBox.setMaximum(230.99)
        self.heightSpinBox.setProperty("value", 100.0)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.weightSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.weightSpinBox.setGeometry(QtCore.QRect(110, 150, 62, 22))
        self.weightSpinBox.setMaximum(200.99)
        self.weightSpinBox.setProperty("value", 20.0)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.neckSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(200, 150, 61, 22))
        self.neckSpinBox.setProperty("value", 10)
        self.neckSpinBox.setDisplayIntegerBase(10)
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(290, 150, 61, 22))
        self.waistSpinBox.setMaximum(300)
        self.waistSpinBox.setProperty("value", 30)
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.hipsSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.hipsSpinBox.setGeometry(QtCore.QRect(380, 150, 61, 22))
        self.hipsSpinBox.setMaximum(300)
        self.hipsSpinBox.setProperty("value", 50)
        self.hipsSpinBox.setObjectName("hipsSpinBox")
        self.calculatePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(480, 140, 80, 31))
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.savePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(580, 140, 80, 31))
        self.savePushButton.setObjectName("savePushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuTiedosto = QtWidgets.QMenu(parent=self.menubar)
        self.menuTiedosto.setObjectName("menuTiedosto")
        self.menuJaa = QtWidgets.QMenu(parent=self.menuTiedosto)
        self.menuJaa.setObjectName("menuJaa")
        self.menuAsetukset = QtWidgets.QMenu(parent=self.menuTiedosto)
        self.menuAsetukset.setObjectName("menuAsetukset")
        self.menuMuokkaa = QtWidgets.QMenu(parent=self.menubar)
        self.menuMuokkaa.setObjectName("menuMuokkaa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTulosta = QtGui.QAction(parent=MainWindow)
        self.actionTulosta.setObjectName("actionTulosta")
        self.actionSulje = QtGui.QAction(parent=MainWindow)
        self.actionSulje.setObjectName("actionSulje")
        self.actionFacebook = QtGui.QAction(parent=MainWindow)
        self.actionFacebook.setObjectName("actionFacebook")
        self.actionInstagram = QtGui.QAction(parent=MainWindow)
        self.actionInstagram.setObjectName("actionInstagram")
        self.actionTwitter = QtGui.QAction(parent=MainWindow)
        self.actionTwitter.setObjectName("actionTwitter")
        self.actionTulosta_2 = QtGui.QAction(parent=MainWindow)
        self.actionTulosta_2.setObjectName("actionTulosta_2")
        self.actionSUlje = QtGui.QAction(parent=MainWindow)
        self.actionSUlje.setObjectName("actionSUlje")
        self.actionFacebook_2 = QtGui.QAction(parent=MainWindow)
        self.actionFacebook_2.setObjectName("actionFacebook_2")
        self.actionTwitter_2 = QtGui.QAction(parent=MainWindow)
        self.actionTwitter_2.setObjectName("actionTwitter_2")
        self.actionInstagram_2 = QtGui.QAction(parent=MainWindow)
        self.actionInstagram_2.setObjectName("actionInstagram_2")
        self.actionKieli = QtGui.QAction(parent=MainWindow)
        self.actionKieli.setObjectName("actionKieli")
        self.actionUlkoasu = QtGui.QAction(parent=MainWindow)
        self.actionUlkoasu.setObjectName("actionUlkoasu")
        self.actionY_tila = QtGui.QAction(parent=MainWindow)
        self.actionY_tila.setCheckable(True)
        self.actionY_tila.setObjectName("actionY_tila")
        self.actionAutomaattinen_tallennus = QtGui.QAction(parent=MainWindow)
        self.actionAutomaattinen_tallennus.setCheckable(True)
        self.actionAutomaattinen_tallennus.setObjectName("actionAutomaattinen_tallennus")
        self.actionPoista = QtGui.QAction(parent=MainWindow)
        self.actionPoista.setObjectName("actionPoista")
        self.menuJaa.addAction(self.actionFacebook_2)
        self.menuJaa.addAction(self.actionTwitter_2)
        self.menuJaa.addAction(self.actionInstagram_2)
        self.menuAsetukset.addAction(self.actionKieli)
        self.menuAsetukset.addAction(self.actionUlkoasu)
        self.menuTiedosto.addAction(self.menuJaa.menuAction())
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.menuAsetukset.menuAction())
        self.menuTiedosto.addAction(self.actionTulosta_2)
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.actionY_tila)
        self.menuTiedosto.addAction(self.actionSUlje)
        self.menuMuokkaa.addAction(self.actionAutomaattinen_tallennus)
        self.menuMuokkaa.addAction(self.actionPoista)
        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menubar.addAction(self.menuMuokkaa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLabel.setText(_translate("MainWindow", "Nimi"))
        self.label_3.setText(_translate("MainWindow", "Kaula"))
        self.label_5.setText(_translate("MainWindow", "Vyötärö"))
        self.label_6.setText(_translate("MainWindow", "Lantio"))
        self.label_4.setText(_translate("MainWindow", "Pituus"))
        self.label_2.setText(_translate("MainWindow", "Paino"))
        self.label_7.setText(_translate("MainWindow", "Syntymäaika"))
        self.label.setText(_translate("MainWindow", "Mittauspäivä"))
        self.bmiLabel.setText(_translate("MainWindow", "0"))
        self.fatUsaLabel.setText(_translate("MainWindow", "0"))
        self.fatFiLabel.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Painoindeksi"))
        self.label_12.setText(_translate("MainWindow", "Rasvaprosentti (FI)"))
        self.label_13.setText(_translate("MainWindow", "Rasvaprosentti (US)"))
        self.label_14.setText(_translate("MainWindow", "Sukupuoli"))
        self.birthDateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.genderComboBox.setPlaceholderText(_translate("MainWindow", "Valitse sukupuoli"))
        self.genderComboBox.setItemText(0, _translate("MainWindow", "Mies"))
        self.genderComboBox.setItemText(1, _translate("MainWindow", "Nainen"))
        self.weighingDateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.calculatePushButton.setText(_translate("MainWindow", "Laske"))
        self.savePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.menuTiedosto.setTitle(_translate("MainWindow", "Tiedosto"))
        self.menuJaa.setTitle(_translate("MainWindow", "Jaa"))
        self.menuAsetukset.setTitle(_translate("MainWindow", "Asetukset"))
        self.menuMuokkaa.setTitle(_translate("MainWindow", "Muokkaa"))
        self.actionTulosta.setText(_translate("MainWindow", "Tulosta..."))
        self.actionSulje.setText(_translate("MainWindow", "Sulje"))
        self.actionFacebook.setText(_translate("MainWindow", "Facebook"))
        self.actionInstagram.setText(_translate("MainWindow", "Instagram"))
        self.actionTwitter.setText(_translate("MainWindow", "Twitter"))
        self.actionTulosta_2.setText(_translate("MainWindow", "Tulosta"))
        self.actionSUlje.setText(_translate("MainWindow", "Sulje"))
        self.actionFacebook_2.setText(_translate("MainWindow", "Facebook"))
        self.actionTwitter_2.setText(_translate("MainWindow", "Twitter"))
        self.actionInstagram_2.setText(_translate("MainWindow", "Instagram"))
        self.actionKieli.setText(_translate("MainWindow", "Kieli"))
        self.actionUlkoasu.setText(_translate("MainWindow", "Ulkoasu"))
        self.actionY_tila.setText(_translate("MainWindow", "Yötila"))
        self.actionY_tila.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionAutomaattinen_tallennus.setText(_translate("MainWindow", "Automaattinen tallennus"))
        self.actionAutomaattinen_tallennus.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPoista.setText(_translate("MainWindow", "Poista käyttäjä"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
