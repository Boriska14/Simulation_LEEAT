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

class CalculPerteMaximaleModelOkumura(QWidget):
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0

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
        self.setWindowTitle("Study of the Impact of Path Loss on Coverage Radius (Radio Coverage)")
        layoutContainer = QVBoxLayout()
        container = QWidget()

        # Create a top-level layout
        layout = QHBoxLayout()
        self.setLayout(layoutContainer)
                
        resultatLM = QLabel("Results Model Okumura Hata")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        resultatLM.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        resultatLM.setStyleSheet("QLabel{color:green;}")
                
        
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
        
        self.frequence = QLabel('Frequency')
        self.frequence.setFont(font)
        self.frequence.setWordWrap(True)
        self.frequenceValue = QLineEdit(self)
        self.frequenceValue.setValidator(QDoubleValidator())
        self.frequenceValue.setText(str(self.getFrequence()))
        self.frequenceValue.setFont(font)
        
        self.hauteur = QLabel('Height Hb, gNodeB (m)')
        self.hauteur.setFont(font)
        self.hauteurValue = QLineEdit(self)
        self.hauteurValue.setValidator(QDoubleValidator())
        self.hauteurValue.setFont(font)
        self.hauteurValue.setText("30")
        
        self.hauteurRecepteur = QLabel('Receiver (or mobile) height (m)')
        self.hauteurRecepteur.setFont(font)
        self.hauteurRecepteur.setWordWrap(True)
        self.hauteurRecepteurValue = QLineEdit(self)
        self.hauteurRecepteurValue.setValidator(QDoubleValidator())
        self.hauteurRecepteurValue.setFont(font)
        self.hauteurRecepteurValue.setText("1.7")

        self.rayonZU_LD = QLabel('Coverage Radius (m) - (urban area)')
        self.rayonZU_LD.setFont(font)
        self.rayonZU_LM = QLabel('Coverage Radius (m) - (urban area)')
        self.rayonZU_LM.setFont(font)

        self.rayonZUValue_LM = QLineEdit(self)
        self.rayonZUValue_LM.setValidator(QDoubleValidator())
        self.rayonZUValue_LM.setDisabled(True)
        self.rayonZUValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.rayonZUValue_LM.setFont(font)

        self.perteMaximaleUrbain_LM = QLabel('Maximum Loss (dB) - (Urban area)')
        self.perteMaximaleUrbain_LM.setFont(font)

        self.perteMaximaleUrbainValue_LM = QLineEdit(self)
        self.perteMaximaleUrbainValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.perteMaximaleUrbainValue_LM.setValidator(QDoubleValidator())
        self.perteMaximaleUrbainValue_LM.setDisabled(True)
        self.perteMaximaleUrbainValue_LM.setFont(font)

        self.rayonZR = QLabel('Coverage Radius (m) - (Rural Area)')
        self.rayonZR.setFont(font)
        self.rayonZRValue_LM = QLineEdit(self)
        self.rayonZRValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.rayonZRValue_LM.setValidator(QDoubleValidator())
        self.rayonZRValue_LM.setDisabled(True)
        self.rayonZRValue_LM.setFont(font)

                
        self.perteMaximaleRurale_LM = QLabel('Maximum Loss (dB) - (Rural Area)')
        self.perteMaximaleRurale_LM.setFont(font)

        self.perteMaximaleRuraleValue_LM = QLineEdit(self)
        self.perteMaximaleRuraleValue_LM.setValidator(QDoubleValidator())
        self.perteMaximaleRuraleValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.perteMaximaleRuraleValue_LM.setDisabled(True)
        self.perteMaximaleRuraleValue_LM.setFont(font)

        self.rayonZSU_LM = QLabel('Coverage Radius (m) - (Suburban Area)')
        self.rayonZSU_LM.setFont(font)

        self.rayonZSUValue_LM = QLineEdit(self)
        self.rayonZSUValue_LM.setValidator(QDoubleValidator())
        self.rayonZSUValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.rayonZSUValue_LM.setDisabled(True)
        self.rayonZSUValue_LM.setFont(font)

        self.perteMaximaleSubUrbain_LM = QLabel('Maximum Loss (dB) - (Auburban Area)')
        self.perteMaximaleSubUrbain_LM.setFont(font)

        self.perteMaximaleSubUrbainValue_LM = QLineEdit(self)
        self.perteMaximaleSubUrbainValue_LM.setValidator(QDoubleValidator())
        self.perteMaximaleSubUrbainValue_LM.setStyleSheet("QLineEdit{color:green;}")
        self.perteMaximaleSubUrbainValue_LM.setDisabled(True)
        self.perteMaximaleSubUrbainValue_LM.setFont(font)


        # Create the first page
        self.form = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addRow(title)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.superficie, self.superficieValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.frequence, self.frequenceValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.hauteur, self.hauteurValue)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.hauteurRecepteur, self.hauteurRecepteurValue)
        self.form.setLayout(self.formLayout)
        layout.addWidget(self.form)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.form1 = QWidget()
        self.form1Layout = QFormLayout()
        self.form1Layout.addRow(resultatLM)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.perteMaximaleUrbain_LM, self.perteMaximaleUrbainValue_LM)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.rayonZU_LM, self.rayonZUValue_LM)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.perteMaximaleSubUrbain_LM, self.perteMaximaleSubUrbainValue_LM)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.rayonZSU_LM, self.rayonZSUValue_LM)    
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.perteMaximaleRurale_LM, self.perteMaximaleRuraleValue_LM)
        self.form1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.form1Layout.addRow(self.rayonZR, self.rayonZRValue_LM)
        self.form1.setLayout(self.form1Layout)
        layout.addWidget(self.form1)
        layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
       
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

        showGraphBtn = QPushButton('See graph', self)
        showGraphBtn.setFont(QFont(const.font, const.fontSizeText,))
        showGraphBtn.setMaximumWidth(250)
        showGraphBtn.setMinimumWidth(200)
        showGraphBtn.clicked.connect(self.showGraphBtn)

        resetBtn = QPushButton('Reset', self)
        resetBtn.setFont(QFont(const.font, const.fontSizeText,))
        resetBtn.setMaximumWidth(250)
        resetBtn.setMinimumWidth(200)
        resetBtn.clicked.connect(self.resetBtn)

        buttonLayout.addStretch()
        buttonLayout.addWidget(previousBtn)
        buttonLayout.addWidget(calculBtn)
        buttonLayout.addWidget(showGraphBtn)
        buttonLayout.addWidget(resetBtn)
        buttonLayout.addStretch()
        
        self.buttons = QWidget()
        self.buttons.setLayout(buttonLayout)

        container.setLayout(layout)
        layoutContainer.addWidget(container)
        layoutContainer.addItem(QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutContainer.addWidget(self.buttons)


    def previousBtn(self):
        self.hide()
        self.bilanWidows.show()

    def calculRayon(self,  perteMaxi: float, a: float, b: float):
        return 10**((perteMaxi - a) / b)

    def calculPerteMR_LD(self, f, Hm, Hb, d):
        return 69.55 + 26.16*math.log10(f) - 13.82*math.log10(Hb) - (1.1*math.log10(f) - 0.7)*Hm - (1.56*math.log10(f) - 0.8) + (44.9 - 6.55*math.log10(Hb))*math.log10(d) - 4.78*(math.log10(f))**2 + 18.33*math.log10(f) - 40.94

    def calculPerteMR_LM(self, f, Hm, Hb, d):
        return 69.55 + 26.16*math.log10(f) - 13.82*math.log10(Hm) - (1.1*math.log10(f) - 0.7)*Hb - (1.56*math.log10(f) - 0.8) + (44.9 - 6.55*math.log10(Hm))*math.log10(d) - 4.78*(math.log10(f))**2 + 18.33*math.log10(f) - 40.94

    def calculPerteMSU_LD(self, f, Hm, Hb, d):
        return 69.55 + 26.16*math.log10(f) - 13.82*math.log10(Hb) - (1.1*math.log10(f) - 0.7)*Hm - (1.56*math.log10(f) - 0.8) + (44.9 - 6.55*math.log10(Hb))*math.log10(d) - 2*(math.log10(f/28))**2 - 5.4

    def calculPerteMSU_LM(self, f, Hm, Hb, d):
        return 69.55 + 26.16*math.log10(f) - 13.82*math.log10(Hm) - (1.1*math.log10(f) - 0.7)*Hb - (1.56*math.log10(f) - 0.8) + (44.9 - 6.55*math.log10(Hm))*math.log10(d) - 2*(math.log10(f/28))**2 - 5.4

    def calculPerteMU_LM(self, f, Hm, Hb, d):
        return 69.55 + (26.16*math.log10(f)) - (13.82*math.log10(Hm)) - (3.2*math.log10(11.75*Hb)) - 4.97 + (44.9 - 6.55*math.log10(Hm))*math.log10(d)

    def calculPerteMU_LD(self, f, Hm, Hb, d):
        return 69.55 + 26.16*math.log10(f) - 13.82*math.log10(Hb) - 3.2*math.log10(11.75*Hm) - 4.97 + (44.9 - 6.55*math.log10(Hb))*math.log10(d)

    def calculBtn(self):
        try:
            superficie = float(self.superficieValue.text().replace(',', '.'))
            frequenceV = float(self.frequenceValue.text().replace(',', '.'))
            hauteur = float(self.hauteurValue.text().replace(',', '.'))
            hauteur_mobile = float(self.hauteurRecepteurValue.text().replace(',', '.'))

            perteMSU_LD = self.calculPerteMSU_LD(
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )

            perteMU_LD = self.calculPerteMU_LD(
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )

            perteMR_LD = self.calculPerteMR_LD(
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )
            
            perteMR_LM = self.calculPerteMR_LM( 
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )
            
            perteMSU_LM = self.calculPerteMSU_LM(
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )

            perteMU_LM = self.calculPerteMU_LM(
                f=frequenceV, 
                Hm=float(self.hauteurRecepteurValue.text().replace(',', '.')),
                Hb=float(self.hauteurValue.text().replace(',', '.')),
                d=float(self.superficieValue.text().replace(',', '.'))
            )

            self.perteMaximaleRuraleValue_LM.setText(str(perteMR_LM))
            self.perteMaximaleSubUrbainValue_LM.setText(str(perteMSU_LM))
            self.perteMaximaleUrbainValue_LM.setText(str(perteMU_LM))

            coefZR = self.getCoefficientZR()
            coefZU = self.getCoefficientZU()
            coefZSU = self.getCoefficientZSU()

            self.rayonZRValue_LM.setText(
                str(self.calculRayon(
                        a=float(coefZR['A']),
                        b=float(coefZR['B']),
                        perteMaxi= perteMR_LM
                    )
                )
            )
            self.rayonZUValue_LM.setText(
                str(self.calculRayon(
                        a=float(coefZU['A']),
                        b=float(coefZU['B']),
                        perteMaxi= perteMU_LM
                    )
                )
            )
            self.rayonZSUValue_LM.setText(
                str(self.calculRayon(
                        a=float(coefZSU['A']),
                        b=float(coefZSU['B']),
                        perteMaxi= perteMSU_LM
                    )
                )
            )

        except Exception as error:
            self.show_dialog(error=str(error))

    def resetBtn(self):
        self.perteMaximaleRuraleValue_LM.setText("")
        self.perteMaximaleSubUrbainValue_LM.setText("")
        self.perteMaximaleUrbainValue_LM.setText("")
        self.rayonZRValue_LM.setText("")
        self.rayonZSUValue_LM.setText("")
        self.rayonZUValue_LM.setText("")

    def showGraphBtn(self):
        if (self.rayonZRValue_LM.text() != ""):
            self.window = ShowGraph(
                title= "Lmax vs Rayon (Model Hata Okumura)",
                x_label= "Rayon",
                y_label= "Lmax",
                x_data=[float(self.rayonZUValue_LM.text()),float(self.rayonZSUValue_LM.text()),float(self.rayonZRValue_LM.text())], 
                y_data=[float(self.perteMaximaleUrbainValue_LM.text()),float(self.perteMaximaleSubUrbainValue_LM.text()),float(self.perteMaximaleRuraleValue_LM.text())],
                graphType='plot'
                )
            self.window.show()

    def getFrequence(self):
        return 700


    def getCoefficientZU(self):
        return {
                'A': 138.5 , 'B': 35.2 
            }

    def getCoefficientZSU(self):
        return {
                'A': 141.65 , 'B': 35.22 
            }

    def getCoefficientZR(self):
        return {
                        'A': 80 , 'B': 12.25 
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
