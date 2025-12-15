import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
import numpy as np
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
import math
import constant as const
from show_graph import ShowGraph
import matplotlib.pyplot as plt
import numpy as np
import math

class CalculDebitPhysique(QWidget):
    bitValueCalcul = 0
    totalMargeMValueCalcul = 0

    bitCreteValueCalcul = 0
    totalMargeCreteValueCalcul = 0

    bitPhysiqueValueCalcul = 0
    totalMargePhysiqueValueCalcul = 0

    w_array = [float(10), float(20), float(30)]

    totalMarge = 0
    bit = 0
    model = ""

    def __init__(self, bilanWidows:QWidget):
        self.bilanWidows = bilanWidows
        self.bilanWidows.hide()

        super().__init__()
        self.setWindowTitle("Calculation of the Physical Data Rate")
        layoutContainer = QVBoxLayout()
        container = QWidget()

        # Create a top-level layout
        layout = QHBoxLayout()
        self.setLayout(layoutContainer)
                
        resultat = QLabel("Results")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        resultat.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        resultat.setStyleSheet("QLabel{color:green;}")

        title = QLabel("Input Parameters")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        title.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        
        self.MIMO = QLabel('MIMO')
        self.MIMO.setFont(font)
        self.MIMO.setWordWrap(True)
        self.MIMO_Value = QComboBox()
        self.MIMO_Value.setFont(font)
        self.MIMO_Value.activated.connect(self.switchMimo)
        self.MIMO_Value.addItems(["2×2"])
        
        self.Nt = QLabel('Nt')
        self.Nt.setFont(font)
        self.Nt.setWordWrap(True)
        self.Nt_Value = QLineEdit(self)
        self.Nt_Value.setValidator(QDoubleValidator())
        self.Nt_Value.setFont(font)
        self.Nt_Value.setDisabled(True)
        self.Nt_Value.setText("2")
        
        self.γ = QLabel('γ')
        self.γ.setFont(font)
        self.γ.setWordWrap(True)
        self.γ_Value = QLineEdit(self)
        self.γ_Value.setValidator(QDoubleValidator())
        self.γ_Value.setFont(font)
        self.γ_Value.setDisabled(True)
        self.γ_Value.setText("25")
     
        self.frequence = QLabel('Frequency')
        self.frequence.setFont(font)
        self.frequence.setWordWrap(True)
        self.frequence_Value = QComboBox()
        self.frequence_Value.setFont(font)
        self.frequence_Value.activated.connect(self.switchPage)
        self.frequence_Value.addItems(["700MHz","3.5GHz" ])

        # Create the first page
        self.form = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addRow(title)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.MIMO, self.MIMO_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.Nt, self.Nt_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.γ, self.γ_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.frequence, self.frequence_Value)
        self.form.setLayout(self.formLayout)
        layout.addWidget(self.form)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.title1 = QLabel("Physical Data Rate W = 10Mhz")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        self.title1.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        self.title1.setStyleSheet("QLabel{color:green;}")

        self.title2 = QLabel("Physical Data Rate W = 20Mhz")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        self.title2.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        self.title2.setStyleSheet("QLabel{color:green;}")

        self.title3 = QLabel("Physical Data Rate W = 30Mhz")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        self.title3.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        self.title3.setStyleSheet("QLabel{color:green;}")

        self.bit1 = QLabel('Rate (Bits/s)')
        self.bit1.setFont(font)
        self.bit1Value = QLineEdit(self)
        self.bit1Value.setValidator(QDoubleValidator())
        self.bit1Value.setDisabled(True)
        self.bit1Value.setStyleSheet("QLineEdit{color:green;}")
        self.bit1Value.setFont(font)
        self.bit1Value.setAlignment(Qt.AlignLeft)

        self.megaBit1 = QLabel('Rate (Mbits/s)')
        self.megaBit1.setFont(font)
        self.megaBit1Value = QLineEdit(self)
        self.megaBit1Value.setAlignment(Qt.AlignLeft)
        self.megaBit1Value.setDisabled(True)
        self.megaBit1Value.setValidator(QDoubleValidator())
        self.megaBit1Value.setFont(font)
        self.megaBit1Value.setStyleSheet("QLineEdit{color:green;}")

        self.bit2 = QLabel('Rate (Bits/s)')
        self.bit2.setFont(font)
        self.bit2Value = QLineEdit(self)
        self.bit2Value.setValidator(QDoubleValidator())
        self.bit2Value.setDisabled(True)
        self.bit2Value.setStyleSheet("QLineEdit{color:green;}")
        self.bit2Value.setFont(font)
        self.bit2Value.setAlignment(Qt.AlignLeft)

        self.megaBit2 = QLabel('Rate (Mbits/s)')
        self.megaBit2.setFont(font)
        self.megaBit2Value = QLineEdit(self)
        self.megaBit2Value.setDisabled(True)
        self.megaBit2Value.setAlignment(Qt.AlignLeft)
        self.megaBit2Value.setValidator(QDoubleValidator())
        self.megaBit2Value.setFont(font)
        self.megaBit2Value.setStyleSheet("QLineEdit{color:green;}")

        self.bit3 = QLabel('Rate (Bits/s)')
        self.bit3.setFont(font)
        self.bit3Value = QLineEdit(self)
        self.bit3Value.setValidator(QDoubleValidator())
        self.bit3Value.setDisabled(True)
        self.bit3Value.setStyleSheet("QLineEdit{color:green;}")
        self.bit3Value.setFont(font)
        self.bit3Value.setAlignment(Qt.AlignLeft)

        self.megaBit3 = QLabel('Rate (Mbits/s)')
        self.megaBit3.setFont(font)
        self.megaBit3Value = QLineEdit(self)
        self.megaBit3Value.setDisabled(True)
        self.megaBit3Value.setValidator(QDoubleValidator())
        self.megaBit3Value.setFont(font)
        self.megaBit3Value.setAlignment(Qt.AlignLeft)
        self.megaBit3Value.setStyleSheet("QLineEdit{color:green;}")

        formCalcul1 = QWidget()
        formCalcul1Layout = QFormLayout()
        formCalcul1Layout.addRow(self.title1, QLabel(''))
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1Layout.addRow(self.bit1, self.bit1Value)
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1Layout.addRow(self.megaBit1, self.megaBit1Value)
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1.setLayout(formCalcul1Layout)

        formCalcul2 = QWidget()
        formCalcul2Layout = QFormLayout()
        formCalcul2Layout.addRow(self.title2, QLabel(''))
        formCalcul2Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul2Layout.addRow(self.bit2, self.bit2Value)
        formCalcul2Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul2Layout.addRow(self.megaBit2, self.megaBit2Value)
        formCalcul2Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul2.setLayout(formCalcul2Layout)
   
        self.formCalcul3 = QWidget()
        self.formCalcul3Layout = QFormLayout()
        self.formCalcul3Layout.addRow(self.title3, QLabel(''))
        self.formCalcul3Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formCalcul3Layout.addRow(self.bit3, self.bit3Value)
        self.formCalcul3Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formCalcul3Layout.addRow(self.megaBit3, self.megaBit3Value)
        self.formCalcul3Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formCalcul3.setLayout(self.formCalcul3Layout)
   
        calculContainer = QWidget()
        calculContainerLayout = QHBoxLayout()
        calculContainer.setStyleSheet("QWidget{background:whitesmoke;}")

        buttonLayout = QHBoxLayout()
        previousBtn = QPushButton('Previous', self)
        previousBtn.setMaximumWidth(250)
        previousBtn.setMinimumWidth(200)
        previousBtn.setFont(QFont(const.font, const.fontSizeText,))
        previousBtn.clicked.connect(self.previousBtn)

        calculBtn = QPushButton('Calculate', self)
        calculBtn.setFont(QFont(const.font, const.fontSizeText,))
        calculBtn.setMaximumWidth(250)
        calculBtn.setMinimumWidth(200)
        calculBtn.clicked.connect(self.calculBtn)

        resetBtn = QPushButton('Reset', self)
        resetBtn.setFont(QFont(const.font, const.fontSizeText,))
        resetBtn.setMaximumWidth(250)
        resetBtn.setMinimumWidth(200)
        resetBtn.clicked.connect(self.resetBtn)

        showGraphBtn = QPushButton('Show graph', self)
        showGraphBtn.setFont(QFont(const.font, const.fontSizeText,))
        showGraphBtn.setMaximumWidth(250)
        showGraphBtn.setMinimumWidth(200)
        showGraphBtn.clicked.connect(self.showGraphBtn)
        
        buttonLayout.addStretch()
        buttonLayout.addWidget(previousBtn)
        buttonLayout.addWidget(calculBtn)
        buttonLayout.addWidget(showGraphBtn)
        buttonLayout.addWidget(resetBtn)
        buttonLayout.addStretch()
        
        self.buttons = QWidget()
        self.buttons.setLayout(buttonLayout)

        calculContainerLayout.addWidget(formCalcul1)
        calculContainerLayout.addStretch()
        calculContainerLayout.addWidget(formCalcul2)
        if self.frequence_Value.currentIndex() == 0:
            calculContainerLayout.addStretch()
            calculContainerLayout.addWidget(self.formCalcul3)

        calculContainerLayout.addStretch()
        calculContainer.setLayout(calculContainerLayout)
        calculContainer.setMaximumHeight(500)
        container.setLayout(layout)

        layoutContainer.addWidget(container)
        layoutContainer.addItem(QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutContainer.addWidget(calculContainer)
        layoutContainer.addItem(QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutContainer.addWidget(self.buttons)

    def showGraphBtn(self):
        if self.frequence_Value.currentIndex() == 0:
            if (self.bit2Value.text() != "" and self.bit1Value.text() != "" and self.bit3Value.text() != ""):
                self.window = ShowGraph(
                    title= "(Rate vs W) Frequency (" + self.frequence_Value.currentText() + ")",
                    x_label= "W",
                    y_label= "Rate in Megabits",
                    x_data=self.w_array, 
                    y_data=[float(self.megaBit1Value.text()), float(self.megaBit2Value.text()), float(self.megaBit3Value.text())],
                    graphType='plot'
                    )
                self.window.show()
        else:
            if (self.bit2Value.text() != "" and self.bit1Value.text() != ""):
                self.window = ShowGraph(
                    title= "(Rate vs W) Frequency (" + self.frequence_Value.currentText() + ")",
                    x_label= "W",
                    y_label= "Rate in Megabits",
                    x_data=self.w_array, 
                    y_data=[float(self.megaBit1Value.text()), float(self.megaBit2Value.text())],
                    graphType='plot'
                    )
                self.window.show()

    def previousBtn(self):
        self.hide()
        self.bilanWidows.show()

    def calculBtn(self):
        try:
            # montant
            N_t = float(self.Nt_Value.text()) 
            gamma = float(self.γ_Value.text())
                
            if self.frequence_Value.currentIndex() == 0:
                bits1 = (10 * self.calculate_log(N_t, gamma)) * N_t
                bits2 = (20 * self.calculate_log(N_t, gamma)) * N_t
                bits3 = (30 * self.calculate_log(N_t, gamma)) * N_t
            
                self.bit1Value.setText(str(round(bits1 / (0.00001), 6)))
                self.megaBit1Value.setText(str(round(bits1, 6)))
            
                self.bit2Value.setText(str(round(bits2 / (0.00001), 6)))
                self.megaBit2Value.setText(str(round(bits2, 6)))
            
                self.bit3Value.setText(str(round(bits3 / (0.00001), 6)))
                self.megaBit3Value.setText(str(round(bits3, 6)))
            elif self.frequence_Value.currentIndex() == 1:
                bits1 = (50 * self.calculate_log(N_t, gamma)) * N_t
                bits2 = (100 * self.calculate_log(N_t, gamma)) * N_t
                
                self.bit1Value.setText(str(round(bits1 / (0.00001),6)))
                self.megaBit1Value.setText(str(round(bits1 , 6)))
            
                self.bit2Value.setText(str(round(bits2 / (0.00001), 6)))
                self.megaBit2Value.setText(str(round(bits2, 6)))
            
        except Exception as error:
            self.show_dialog(error=str(error))

    def calculate_log(self,N_t, gamma):
        result = math.log2(1 + ((1/N_t) * gamma))
        return result
    
    def show_dialog(self, error: str):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("Warning")

        # Create a label with a message
        label = QLabel(error)
        fontTitle = QFont(const.font, const.fontSizeTitle, QFont.Bold)
        label.setFont(fontTitle)

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec_()

    def resetBtn(self):
        self.bit1Value.setText("")
        self.megaBit1Value.setText("")
        self.bit2Value.setText("")
        self.megaBit2Value.setText("")
        self.bit3Value.setText("")
        self.megaBit3Value.setText("")

    def switchMimo(self):
        if self.frequence_Value.currentIndex() == 0:
            if self.MIMO_Value.currentIndex() == 0:
                self.Nt_Value.setText("2")
        else:
            if self.MIMO_Value.currentIndex() == 0:
                self.Nt_Value.setText("4")
            elif self.MIMO_Value.currentIndex() == 1:
                self.Nt_Value.setText("8")

    def switchPage(self):
        self.bit1Value.setText("")
        self.megaBit1Value.setText("")
        self.bit2Value.setText("")
        self.megaBit2Value.setText("")
        self.bit3Value.setText("")
        self.megaBit3Value.setText("")
        self.MIMO_Value.clear()
        self.switchMimo()
        if self.frequence_Value.currentIndex() == 0:
            #700
            self.w_array = [float(10), float(20), float(30)]
            self.MIMO_Value.addItems(["2×2"])
            self.γ_Value.setText("25")
            self.Nt_Value.setText("2")
            self.title1.setText("Physical Data Rate W = 10Mhz")
            self.title2.setText("Physical Data Rate W = 20Mhz")
            self.title3.setText("Physical Data Rate W = 30Mhz")
            self.formCalcul3.show()
        elif self.frequence_Value.currentIndex() == 1:
            #3.5
            self.w_array = [float(50), float(100)]
            self.MIMO_Value.addItems(["4×4","8×8"])
            self.Nt_Value.setText("4")
            self.γ_Value.setText("25")
            self.title1.setText("Physical Data Rate W = 50MHz")
            self.title2.setText("Physical Data Rate W = 100MHz")
            self.title3.setText("")
            self.formCalcul3.hide()
