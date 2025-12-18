import sys
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
import math
import constant as const
from show_graph import ShowGraph

class CalculPerteMaximaleModelUma(QWidget):
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0

    celeretyV = (3 * (10**8))  # m/s
    shadowFadingV = 6.8 
    affaiblissement = 3

    totalMarge = 0
    pire = 0
    model = ""

    def __init__(self, bilanWidows:QWidget,  pireDValueCalcul: int, totalMargeDValueCalcul: int, pireMValueCalcul: int, totalMargeMValueCalcul: int):
        self.bilanWidows = bilanWidows
        self.bilanWidows.hide()
        self.pireDValueCalcul = pireDValueCalcul
        self.totalMargeDValueCalcul = totalMargeDValueCalcul
        self.pireMValueCalcul = pireMValueCalcul
        self.totalMargeMValueCalcul = totalMargeMValueCalcul

        super().__init__()
        self.setWindowTitle("Study of the impact of path loss on the coverage radius")
        layoutContainer = QVBoxLayout()
        container = QWidget()

        # Create a top-level layout
        layout = QHBoxLayout()
        self.setLayout(layoutContainer)
                
        resultat = QLabel("Results Model Uma")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        resultat.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        resultat.setStyleSheet("QLabel{color:green;}")
                
        title = QLabel("Input Parameters")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        title.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        
        self.superficie = QLabel('Area d, (Km²)')
        self.superficie.setFont(font)
        self.superficie.setWordWrap(True)
        self.superficieValue = QLineEdit(self)
        self.superficieValue.setValidator(QDoubleValidator())
        self.superficieValue.setFont(font)
        self.superficieValue.setText("100")
        
        self.frequence = QLabel('Frequency in Ghz')
        self.frequence.setFont(font)
        self.frequence.setWordWrap(True)
        self.frequenceValue = QLineEdit(self)
        self.frequenceValue.setFont(font)
        self.frequenceValue.setText("3.5")
        
        self.celerety = QLabel('Celerity (c)')
        self.celerety.setFont(font)
        self.celerety.setWordWrap(True)
        self.celeretyValue = QLineEdit(self)
        self.celeretyValue.setValidator(QDoubleValidator())
        self.celeretyValue.setFont(font)
        self.celeretyValue.setText(str(self.celeretyV))
        self.celeretyValue.setDisabled(True)
        
        self.affaiblissementTrajet = QLabel('weakening of the path (n)')
        self.affaiblissementTrajet.setFont(font)
        self.affaiblissementTrajet.setWordWrap(True)
        self.affaiblissementTrajetValue = QLineEdit(self)
        self.affaiblissementTrajetValue.setValidator(QDoubleValidator())
        self.affaiblissementTrajetValue.setFont(font)
        self.affaiblissementTrajetValue.setDisabled(True)
        self.affaiblissementTrajetValue.setText(str(self.affaiblissement))
        
        self.shadowFading = QLabel('Shadow fading (SF)')
        self.shadowFading.setFont(font)
        self.shadowFading.setWordWrap(True)
        self.shadowFadingValue = QLineEdit(self)
        self.shadowFadingValue.setValidator(QDoubleValidator())
        self.shadowFadingValue.setFont(font)
        self.shadowFadingValue.setText(str(self.shadowFadingV))
        self.shadowFadingValue.setDisabled(True)

        self.rayonZU = QLabel('Coverage radius (m) - (urban area)')
        self.rayonZU.setFont(font)

        self.rayonZUValue = QLineEdit(self)
        self.rayonZUValue.setValidator(QDoubleValidator())
        self.rayonZUValue.setDisabled(True)
        self.rayonZUValue.setStyleSheet("QLineEdit{color:green;}")
        self.rayonZUValue.setFont(font)
                
        self.perteMaximaleUrbain = QLabel('Maximum loss (dB) - (urban area)')
        self.perteMaximaleUrbain.setFont(font)

        self.perteMaximaleUrbainValue = QLineEdit(self)
        self.perteMaximaleUrbainValue.setValidator(QDoubleValidator())
        self.perteMaximaleUrbainValue.setDisabled(True)
        self.perteMaximaleUrbainValue.setStyleSheet("QLineEdit{color:green;}")
        self.perteMaximaleUrbainValue.setFont(font)

        # Create the first page
        self.form = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addRow(title)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.superficie, self.superficieValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.frequence, self.frequenceValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.celerety, self.celeretyValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.affaiblissementTrajet, self.affaiblissementTrajetValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.shadowFading, self.shadowFadingValue)
        self.form.setLayout(self.formLayout)
        layout.addWidget(self.form)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

       
        buttonLayout = QVBoxLayout()
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

        showGraphBtn = QPushButton('See graph', self)
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
        layout.addWidget(self.buttons)
        container.setLayout(layout)

        self.form1 = QWidget()
        self.form1Layout = QFormLayout()
        self.form1Layout.addRow(resultat)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.perteMaximaleUrbain, self.perteMaximaleUrbainValue)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.rayonZU, self.rayonZUValue)
        self.form1.setLayout(self.form1Layout)
        layout.addWidget(self.form1)

        layoutContainer.addWidget(container)
        layoutContainer.addItem(QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutContainer.addWidget(self.form1)

    def previousBtn(self):
        self.hide()
        self.bilanWidows.show()

    def showGraphBtn(self):
        if (self.rayonZUValue.text() != ""):
            self.window = ShowGraph(
                title= "Lmax vs Rayon (Model Uma)",
                x_label= "Rayon",
                y_label= "Lmax",
                x_data=[float(self.rayonZUValue.text())], 
                y_data=[float(self.perteMaximaleUrbainValue.text())],
                graphType='scatter'
                )
            self.window.show()

    def calculRayon(self,  perteMaxi: float, a: float, b: float):
        return 10**((perteMaxi - a) / b)

    def calculPerteModel(self, f: float, d:float):
        return 20*math.log10(4*math.pi*f/self.celeretyV) + 10*self.affaiblissement*math.log10(d) + self.shadowFadingV
    
    def calculBtn(self):
        try:
            frequence_Ghz = float(self.frequenceValue.text().replace(',', '.'))  # valeur en Ghz
            frequence_Hz = frequence_Ghz * 10**9  # conversion en Hz

            perteMU = self.calculPerteModel( 
                f=frequence_Hz, 
                d=float(self.superficieValue.text().replace(',', '.'))
            )

            self.perteMaximaleUrbainValue.setText(str(perteMU))
            coefZU = self.getCoefficientZU()

            self.rayonZUValue.setText(
                str(self.calculRayon(
                        a=float(coefZU['A']),
                        b=float(coefZU['B']),
                        perteMaxi=perteMU
                    )
                )
            )
        except Exception as error:
            self.show_dialog(error=str(error))

    def resetBtn(self):
        self.perteMaximaleUrbainValue.setText("")
        self.rayonZUValue.setText("")

    def getFrequence(self):
        return 700

    def getCoefficientZU(self):
        return {
            'A': 78.2 , 'B': 15.5
        }

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
