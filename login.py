import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QWidget,
    QStackedLayout,
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
)
from bilan_liaison_montante import BilanLiaisonMontante
import constant as const
from qtwidgets import PasswordEdit

class Login(QWidget):
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EMIS.LEEAT")
        # Create a top-level layout

        btnLayout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        self.resize(500, 415)
        
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap(self.resource_path('./images/icon.png'))
 
        # adding image to label
        self.label.setPixmap(self.pixmap)

        self.label.setAlignment(Qt.AlignCenter)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        layout.addWidget(self.label)

        font = QFont(const.font, const.fontSizeText, QFont.Bold)

        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Admin"])
        # self.pageCombo.activated.connect(self.switchPage)

        login = QLabel('Login:')
        login.setFont(font)

        password = QLabel('Password:')
        password.setFont(font)

        self.title = QLabel(" Test bench Propagation attenuation simulation tool on mobility (coverage and capacity) for the 5G network")
        fontTitle = QFont(const.font, const.fontSizeTitle, QFont.Bold)
        self.title.setFont(fontTitle)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)

        # setting geometry to the label 
        # self.title.setMaximumWidth(560)
        layout.addWidget(self.title)
        layout.addItem(QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create the first page
        # self.passwordValue = QLineEdit(self)
        # self.passwordValue.setEchoMode(QLineEdit.Password)

        self.passwordValue = PasswordEdit()
        self.form = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addRow(login, self.pageCombo)
        self.formLayout.addRow(password, self.passwordValue)
        self.form.setLayout(self.formLayout)
        layout.addWidget(self.form)

        buttonWindow1 = QPushButton('login', self)
        buttonWindow1.setMaximumWidth(250)
        buttonWindow1.setMinimumWidth(200)
        buttonWindow1.setFont(QFont(const.font, const.fontSizeText))
        buttonWindow1.clicked.connect(self.validateBtn)

        buttonWindow2 = QPushButton('close', self)
        buttonWindow2.setMaximumWidth(250)
        buttonWindow2.setMinimumWidth(200)
        buttonWindow2.setFont(QFont(const.font, const.fontSizeText))
        buttonWindow2.clicked.connect(self.cancelBtn)

        btnLayout.setAlignment(Qt.AlignCenter)
        btnLayout.addStretch()
        btnLayout.addWidget(buttonWindow2)
        btnLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        btnLayout.addWidget(buttonWindow1)
        btnLayout.addStretch()

        nextBtn = QWidget()
        nextBtn.setLayout(btnLayout)

        # Set the layout on the dialog
        layout.addWidget(nextBtn)
        layout.addStretch()

    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

    def show_dialog(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("Warning")

        # Create a label with a message
        label = QLabel("Please enter the correct login credentials.")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec_()

    def validateBtn(self):
        print('value: ' + self.passwordValue.text())
        print('value combo: ' + self.pageCombo.currentText())
        if self.pageCombo.currentText() == 'Admin' and self.passwordValue.text() == "Azerty@12":
            self.window = BilanLiaisonMontante(linkScreen=self, sens="Montantee")
            self.window.show()
        else:
            self.show_dialog()
      
    def cancelBtn(self):
        self.close()

    def validatePassword(self):
        reg_ex = QRegExp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#\$&*~]).{8,}$")
        input_validator = QRegExpValidator(reg_ex, self.passwordValue)
        self.passwordValue.setValidator(input_validator)

