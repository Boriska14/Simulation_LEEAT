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

class CalculDebitCrete(QWidget):
    bitValueCalcul = 0
    totalMargeMValueCalcul = 0

    bitCreteValueCalcul = 0
    totalMargeCreteValueCalcul = 0

    bitPhysiqueValueCalcul = 0
    totalMargePhysiqueValueCalcul = 0

    w_array = [float(10), float(20), float(30)]
    w_array_string = ['10Mhz','20Mhz', '30Mhz']

    totalMarge = 0
    bit = 0
    model = ""

    def __init__(self, bilanWidows:QWidget):
        self.bilanWidows = bilanWidows
        self.bilanWidows.hide()

        super().__init__()
        self.setWindowTitle("Calculation of Peak Data Rate")
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
        
        self.μ = QLabel('μ')
        self.μ.setFont(font)
        self.μ.setWordWrap(True)
        self.μ_Value = QComboBox()
        self.μ_Value.setFont(font)
        self.μ_Value.activated.connect(self.switchMu)
        self.μ_Value.addItems(["0","1"])
        
        self.t_su = QLabel('T_s^μ')
        self.t_su.setFont(font)
        self.t_su.setWordWrap(True)
        self.t_su_Value = QLineEdit(self)
        self.t_su_Value.setValidator(QDoubleValidator())
        self.t_su_Value.setFont(font)
        self.t_su_Value.setDisabled(True)
        self.t_su_Value.setText(str(0.001/(14.2**(float(self.μ_Value.currentText())))))

        self.n_cc = QLabel('n_cc')
        self.n_cc.setFont(font)
        self.n_cc.setWordWrap(True)
        self.n_cc_Value = QLineEdit(self)
        self.n_cc_Value.setValidator(QDoubleValidator())
        self.n_cc_Value.setFont(font)
        self.n_cc_Value.setDisabled(True)
        self.n_cc_Value.setText("1")
        
        self.v = QLabel('v')
        self.v.setFont(font)
        self.v.setWordWrap(True)
        self.v_Value = QLineEdit(self)
        self.v_Value.setValidator(QDoubleValidator())
        self.v_Value.setFont(font)
        self.v_Value.setDisabled(True)
        self.v_Value.setText("2")
        
        self.Q_m = QLabel('Q_m')
        self.Q_m.setFont(font)
        self.Q_m.setWordWrap(True)
        self.Q_m_Value = QLineEdit(self)
        self.Q_m_Value.setValidator(QDoubleValidator())
        self.Q_m_Value.setFont(font)
        self.Q_m_Value.setDisabled(True)
        self.Q_m_Value.setText("6")
        
        self.f = QLabel('f')
        self.f.setFont(font)
        self.f.setWordWrap(True)
        self.f_Value = QLineEdit(self)
        self.f_Value.setValidator(QDoubleValidator())
        self.f_Value.setFont(font)
        self.f_Value.setDisabled(True)
        self.f_Value.setText("1")
        
        self.r_max = QLabel('R_max')
        self.r_max.setFont(font)
        self.r_max.setWordWrap(True)
        self.r_max_Value = QLineEdit(self)
        self.r_max_Value.setValidator(QDoubleValidator())
        self.r_max_Value.setFont(font)
        self.r_max_Value.setDisabled(True)
        self.r_max_Value.setText(str(948/1024))
                
        self.OH = QLabel('OH')
        self.OH.setFont(font)
        self.OH.setWordWrap(True)
        self.OH_Value = QLineEdit(self)
        self.OH_Value.setValidator(QDoubleValidator())
        self.OH_Value.setFont(font)
        self.OH_Value.setDisabled(True)
        self.OH_Value.setText("0.14")
        
        self.α = QLabel('alpha')
        self.α.setFont(font)
        self.α.setWordWrap(True)
        self.α_Value = QLineEdit(self)
        self.α_Value.setValidator(QDoubleValidator())
        self.α_Value.setFont(font)
        self.α_Value.setDisabled(True)
        self.α_Value.setText("1")
     
        self.frequence = QLabel('Frequency')
        self.frequence.setFont(font)
        self.frequence.setWordWrap(True)
        self.frequence_Value = QComboBox()
        self.frequence_Value.setFont(font)
        self.frequence_Value.activated.connect(self.switchPage)
        self.frequence_Value.addItems(["700MHz","3.5GHz" ])

        self.w = QLabel('W')
        self.w.setFont(font)
        self.w.setWordWrap(True)
        self.w_Value = QComboBox()
        self.w_Value.setFont(font)
        self.w_Value.activated.connect(self.switchPage)
        self.w_Value.addItems(self.w_array_string)

        self.MIMO = QLabel('MIMO')
        self.MIMO.setFont(font)
        self.MIMO.setWordWrap(True)
        self.MIMO_Value = QComboBox()
        self.MIMO_Value.setFont(font)
        self.MIMO_Value.activated.connect(self.switchMimo)
        self.MIMO_Value.addItems(["2×2"])
        
        # Create the first page
        self.form = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addRow(title)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.μ, self.μ_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.t_su, self.t_su_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.n_cc, self.n_cc_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.v, self.v_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.Q_m, self.Q_m_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.f, self.f_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.r_max, self.r_max_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.OH, self.OH_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.α, self.α_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.frequence, self.frequence_Value)
        self.formLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.formLayout.addRow(self.MIMO, self.MIMO_Value)
        self.form.setLayout(self.formLayout)
        layout.addWidget(self.form)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.title1 = QLabel("Peak Data Rate W = 10Mhz")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        self.title1.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        self.title1.setStyleSheet("QLabel{color:green;}")

        self.title2 = QLabel("Peak Data Rate W = 20Mhz")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        self.title2.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        self.title2.setStyleSheet("QLabel{color:green;}")

        self.title3 = QLabel("Peak Data Rate W = 30Mhz")
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

        self.megaBit1 = QLabel('Rate (Mbits/s)')
        self.megaBit1.setFont(font)
        self.megaBit1Value = QLineEdit(self)
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

        self.megaBit2 = QLabel('Rate (Mbits/s)')
        self.megaBit2.setFont(font)
        self.megaBit2Value = QLineEdit(self)
        self.megaBit2Value.setDisabled(True)
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

        self.megaBit3 = QLabel('Rate (Mbits/s)')
        self.megaBit3.setFont(font)
        self.megaBit3Value = QLineEdit(self)
        self.megaBit3Value.setDisabled(True)
        self.megaBit3Value.setValidator(QDoubleValidator())
        self.megaBit3Value.setFont(font)
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

        calculContainerLayout.addStretch()
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
                    title= "(Débit vs W) Frequence (" + self.frequence_Value.currentText() + ")",
                    x_label= "W",
                    y_label= "Débit en Megabits",
                    x_data=self.w_array, 
                    y_data=[float(self.megaBit1Value.text()), float(self.megaBit2Value.text()), float(self.megaBit3Value.text())],
                    graphType='plot'
                    )
                self.window.show()
        else:
            if (self.bit2Value.text() != "" and self.bit1Value.text() != ""):
                self.window = ShowGraph(
                    title= "(Débit vs W) Frequence (" + self.frequence_Value.currentText() + ")",
                    x_label= "W",
                    y_label= "Débit en Megabits",
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
            n_cc = float(self.n_cc_Value.text())
            v = float(self.v_Value.text())
            alpha = float(self.α_Value.text())
            Q_m = float(self.Q_m_Value.text())
            f = float(self.f_Value.text())
            R_max = float(self.r_max_Value.text())
            mu = float(self.μ_Value.currentText())
            OH = float(self.OH_Value.text())
            T_s = float(self.t_su_Value.text())
      
            if self.frequence_Value.currentIndex() == 0:
                bits1 = ((n_cc * v * alpha * Q_m * f * R_max * 24 * 12 * (1 - OH)) / T_s)
                bits2 = ((n_cc * v * alpha * Q_m * f * R_max * 51 * 12 * (1 - OH)) / T_s)
                bits3 = ((n_cc * v * alpha * Q_m * f * R_max * 78 * 12 * (1 - OH)) / T_s)
            
                self.bit1Value.setText(str(round(bits1, 6)))
                self.megaBit1Value.setText(str(round(bits1 * 0.00001, 6)))
            
                self.bit2Value.setText(str(round(bits2, 6)))
                self.megaBit2Value.setText(str(round(bits2 * 0.00001, 6)))
            
                self.bit3Value.setText(str(round(bits3, 6)))
                self.megaBit3Value.setText(str(round(bits3 * 0.00001, 6)))
            elif self.frequence_Value.currentIndex() == 1:
                NRB_1 = 133 if mu == 1 else 270
                bits1 = ((n_cc * v * alpha * Q_m * f * R_max * NRB_1 * 12 * (1 - OH)) / T_s)

                NRB_2 = 273
                mu = 1
                
                bits2 = ((n_cc * v * alpha * Q_m * f * R_max * NRB_2 * 12 * (1 - OH)) / T_s)
       
                self.bit1Value.setText(str(round(bits1, 6)))
                self.megaBit1Value.setText(str(round(bits1 * 0.00001, 6)))
            
                self.bit2Value.setText(str(round(bits2, 6)))
                self.megaBit2Value.setText(str(round(bits2 * 0.00001, 6)))
            
        except Exception as error:
            self.show_dialog(error=str(error))

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
                self.v_Value.setText("2")
        else:
            if self.MIMO_Value.currentIndex() == 0:
                self.v_Value.setText("4")
            elif self.MIMO_Value.currentIndex() == 1:
                self.v_Value.setText("8")

    def switchMu(self):
        # print('u : ' + str(float(self.μ_Value.currentText())))
        # print('u : ' + str((14.2**(float(self.μ_Value.currentText())))))
        self.t_su_Value.setText(str(0.001/(14.2**(float(self.μ_Value.currentText())))))

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
            self.v_Value.setText("2")
            self.Q_m_Value.setText("6")
            self.OH_Value.setText("0.14")
            self.α_Value.setText("1")
            self.MIMO_Value.addItems(["2×2"])
            self.w_array = [float(10), float(20), float(30)]
            self.title1.setText("Peak Data Rate W = 10Mhz")
            self.title2.setText("Peak Data Rate W = 20Mhz")
            self.title3.setText("Peak Data Rate W = 30Mhz")
            self.formCalcul3.show()
        elif self.frequence_Value.currentIndex() == 1:
            #3.5
            self.v_Value.setText("4")
            self.Q_m_Value.setText("6")
            self.OH_Value.setText("0.18")
            self.α_Value.setText("0.74")
            self.MIMO_Value.addItems(["4×4","8×8"])
            self.w_array = [float(50), float(100)]
            self.title1.setText("Peak Data Rate W = 50MHz")
            self.title2.setText("Peak Data Rate W = 100MHz")
            self.title3.setText("")
            self.formCalcul3.hide()
