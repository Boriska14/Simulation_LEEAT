import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from result_bilan_liason_up_screen import ResultBilanLiaisonUpScreen
import constant as const
import math

class BilanLiaisonMontante(QWidget):
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0

    puissance_transmission = 23
    gain_antenne_transition = 0
    sinr = -4.13
    density_bruit = -174
    puissance_bruit = -110.66
    facteur_bruit = 2
    gain_antenne_reception = 17
    perte_cable = 0.5
    sensibility = -129.29
    interference = 3
    effet_masque = 7.68
    corps_humain = 1
    penetration_interrieur_batiment = 15

    nbreEltAntenne = 192
    nbreTXRU = 64
    nbrePortAntenne = 2
    gainReseauAntenne = 25.05
    gainSousReseauAntenne = 10
    layoutV = QVBoxLayout()
    tabsIndex = 0
    sens = ""
    model = ""
    
    def __init__(self, linkScreen:QWidget, sens):
        super().__init__()
        self.linkScreen = linkScreen
        self.linkScreen.hide()
        self.sens = sens
        font = QFont(const.font, const.fontSizeText, QFont.Bold)

        self.tabs = QTabWidget()
        self.tabs.currentChanged.connect(self.onglet_change)
        self.setLayout(self.layoutV)

        self.setWindowTitle('Link Report')

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        
        self.tabs.addTab(self.tab1, 'Okumura Hata 5G model')
        self.tabs.addTab(self.tab2, 'UMa 5G model')
        self.tabs.addTab(self.tab3, 'UMi 5G model')

        self.layoutV.addWidget(self.tabs)

    def showEltModelOkumura(self):
        tab1Information = QWidget()
        layout1 = QVBoxLayout()
        layoutTab = QGridLayout()
        
        fourTitle = QLabel('Parameters')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourTitle.setFont(font)
        fourTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(fourTitle)

        fourSubTitle1 = QLabel('Duplex Mode')
        fourSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle1Value.setText("FDD")
        fourSubTitle1Value.setDisabled(True)
        fourSubTitle1.setFont(font)

        fourSubTitle2 = QLabel('Rate [Mbps]')
        fourSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle2Value.setText('variable')
        fourSubTitle2Value.setDisabled(True)
        fourSubTitle2.setFont(font)

        fourSubTitle3 = QLabel('Frequency [MHz]')
        fourSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle3Value.setValidator(QDoubleValidator())
        fourSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle3Value.setText('700')
        fourSubTitle3.setFont(font)

        fourSubTitle4 = QLabel('Bandwidth [MHz]')
        fourSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle4Value.setText('10, 20 ou 30')
        fourSubTitle4Value.setDisabled(True)
        fourSubTitle4.setFont(font)

        fourSubTitle5 = QLabel('Antenna Height BS [m]')
        fourSubTitle5Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle5Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle5Value.setText('30')
        fourSubTitle5Value.setDisabled(True)
        fourSubTitle5Value.setValidator(QDoubleValidator())
        fourSubTitle5.setFont(font)

        fourSubTitle6 = QLabel('Antenna Height UE [m]')
        fourSubTitle6Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle6Value.setText('1,70')
        fourSubTitle6Value.setDisabled(True)
        fourSubTitle6Value.setValidator(QDoubleValidator())
        fourSubTitle6.setFont(font)

        fourSubTitle7 = QLabel('Coverage Probability')
        fourSubTitle7Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle7Value.setText('0.9')
        fourSubTitle7Value.setDisabled(True)
        fourSubTitle7Value.setValidator(QDoubleValidator())
        fourSubTitle7.setFont(font)

        fourSubTitle8 = QLabel('Standard deviation of the masking  effect [dB]')
        fourSubTitle8Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle8Value.setText('6')
        fourSubTitle8Value.setValidator(QDoubleValidator())
        fourSubTitle8Value.setDisabled(True)
        fourSubTitle8.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(fourSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(fourSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel('Mbps'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(fourSubTitle3Value, 0, 0)
        layoutFormTransmitter2.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(fourSubTitle4Value, 0, 0)
        layoutFormTransmitter3.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        layoutFormTransmitter4 = QGridLayout()
        layoutWidgetTransmitter4 = QWidget()
        layoutFormTransmitter4.addWidget(fourSubTitle5Value, 0, 0)
        layoutFormTransmitter4.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter4.setLayout(layoutFormTransmitter4)

        layoutFormTransmitter5 = QGridLayout()
        layoutWidgetTransmitter5 = QWidget()
        layoutFormTransmitter5.addWidget(fourSubTitle6Value, 0, 0)
        layoutFormTransmitter5.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter5.setLayout(layoutFormTransmitter5)

        layoutFormTransmitter6 = QGridLayout()
        layoutWidgetTransmitter6 = QWidget()
        layoutFormTransmitter6.addWidget(fourSubTitle7Value, 0, 0)
        layoutFormTransmitter6.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter6.setLayout(layoutFormTransmitter6)

        layoutFormTransmitter7 = QGridLayout()
        layoutWidgetTransmitter7 = QWidget()
        layoutFormTransmitter7.addWidget(fourSubTitle8Value, 0, 0)
        layoutFormTransmitter7.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter7.setLayout(layoutFormTransmitter7)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(fourSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(fourSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(fourSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(fourSubTitle4, layoutWidgetTransmitter3)
        formLayout.addRow(fourSubTitle5, layoutWidgetTransmitter4)
        formLayout.addRow(fourSubTitle6, layoutWidgetTransmitter5)
        formLayout.addRow(fourSubTitle7, layoutWidgetTransmitter6)
        formLayout.addRow(fourSubTitle8, layoutWidgetTransmitter7)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        firstTitle = QLabel('Transmission (UE)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstTitle.setFont(font)
        firstTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(firstTitle)

        firstSubTitle1 = QLabel('Transmission Power')
        firstSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle1Value.setValidator(QDoubleValidator())
        firstSubTitle1Value.setText(str(self.puissance_transmission))
        firstSubTitle1Value.setDisabled(True)
        firstSubTitle1.setFont(font)

        firstSubTitle2 = QLabel('Antenna Gain')
        firstSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle2Value.setValidator(QDoubleValidator())
        firstSubTitle2Value.setText(str(self.gain_antenne_transition))
        firstSubTitle2Value.setDisabled(True)
        firstSubTitle2.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(firstSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(firstSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(firstSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(firstSubTitle2, layoutWidgetTransmitter1)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        secondTitle = QLabel('Reception (Base Station)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondTitle.setFont(font)
        secondTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(secondTitle)

        secondSubTitle1 = QLabel('SINR [dB]')
        secondSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle1Value.setText(str(self.sinr))
        secondSubTitle1Value.setDisabled(True)
        secondSubTitle1.setFont(font)

        secondSubTitle2 = QLabel('Noise Density [dBm/Hz]')
        secondSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle2Value.setValidator(QDoubleValidator())
        secondSubTitle2Value.setText(str(self.density_bruit))
        secondSubTitle2Value.setDisabled(True)
        secondSubTitle2.setFont(font)

        secondSubTitle3 = QLabel('Noise Power [dBm]')
        secondSubTitle3Value = QLineEdit(self)
        secondSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle3Value.setValidator(QDoubleValidator())
        secondSubTitle3Value.setText(str(self.puissance_bruit))
        secondSubTitle3Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle3.setFont(font)

        secondSubTitle4 = QLabel('Noise Figure [dB]')
        secondSubTitle4Value = QLineEdit(self)
        secondSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle4Value.setValidator(QDoubleValidator())
        secondSubTitle4Value.setText(str(self.facteur_bruit))
        secondSubTitle4Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle4.setFont(font)

        secondSubTitle5 = QLabel('Antenna Gain [dBi]')
        secondSubTitle5Value = QLineEdit(self)
        secondSubTitle5Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle5Value.setValidator(QDoubleValidator())
        secondSubTitle5Value.setText(str(self.gain_antenne_reception))
        secondSubTitle5Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle5.setFont(font)

        secondSubTitle6 = QLabel('Cable Loss [dB]')
        secondSubTitle6Value = QLineEdit(self)
        secondSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle6Value.setValidator(QDoubleValidator())
        secondSubTitle6Value.setText(str(self.perte_cable))
        secondSubTitle6Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle6.setFont(font)

        secondSubTitle7 = QLabel('Sensitivity [dBm]')
        secondSubTitle7Value = QLineEdit(self)
        secondSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle7Value.setValidator(QDoubleValidator())
        secondSubTitle7Value.setText(str(self.sensibility))
        secondSubTitle7Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle7.setFont(font)

        secondSubTitle8 = QLabel('Received Power [dBm]')
        secondSubTitle8Value = QLineEdit(self)
        secondSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle8Value.setValidator(QDoubleValidator())
        secondSubTitle8Value.setText("Variable")
        secondSubTitle8Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle8.setFont(font)

        decibel = QLabel('dB')
        decibel.setFont(QFont(const.font, const.fontSizeText,))

        layoutForm = QGridLayout()
        layoutWidget = QWidget()
        layoutForm2 = QGridLayout()
        layoutWidget2 = QWidget()
        layoutForm3 = QGridLayout()
        layoutWidget3 = QWidget()
        layoutForm4 = QGridLayout()
        layoutWidget4 = QWidget()
        layoutForm5 = QGridLayout()
        layoutWidget5 = QWidget()
        layoutForm6 = QGridLayout()
        layoutWidget6 = QWidget()
        layoutForm7 = QGridLayout()
        layoutWidget7 = QWidget()
        layoutForm8 = QGridLayout()
        layoutWidget8 = QWidget()
    
        layoutForm.addWidget(secondSubTitle1Value, 0, 0)
        # layoutForm.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm.addWidget(QLabel('dB'), 0, 1)
        layoutWidget.setLayout(layoutForm)

        layoutForm2.addWidget(secondSubTitle2Value, 0, 0)
        # layoutForm2.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm2.addWidget(QLabel('dBm/Hz'), 0, 1)
        layoutWidget2.setLayout(layoutForm2)

        layoutForm3.addWidget(secondSubTitle3Value, 0, 0)
        # layoutForm3.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm3.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget3.setLayout(layoutForm3)

        layoutForm4.addWidget(secondSubTitle4Value, 0, 0)
        # layoutForm4.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm4.addWidget(QLabel('dB'), 0, 1)
        layoutWidget4.setLayout(layoutForm4)

        layoutForm5.addWidget(secondSubTitle5Value, 0, 0)
        # layoutForm5.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm5.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget5.setLayout(layoutForm5)

        layoutForm6.addWidget(secondSubTitle6Value, 0, 0)
        # layoutForm6.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm6.addWidget(QLabel('dB'), 0, 1)
        layoutWidget6.setLayout(layoutForm6)

        layoutForm7.addWidget(secondSubTitle7Value, 0, 0)
        # layoutForm7.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm7.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget7.setLayout(layoutForm7)

        layoutForm8.addWidget(secondSubTitle8Value, 0, 0)
        # layoutForm8.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutForm8.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget8.setLayout(layoutForm8)

        form2 = QWidget()
        formLayout1 = QFormLayout()
        formLayout1.addRow(secondSubTitle1, layoutWidget)
        formLayout1.addRow(secondSubTitle2, layoutWidget2)
        formLayout1.addRow(secondSubTitle3, layoutWidget3)
        formLayout1.addRow(secondSubTitle4, layoutWidget4)
        formLayout1.addRow(secondSubTitle5, layoutWidget5)
        formLayout1.addRow(secondSubTitle6, layoutWidget6)
        formLayout1.addRow(secondSubTitle7, layoutWidget7)
        formLayout1.addRow(secondSubTitle8, layoutWidget8)
        form2.setLayout(formLayout1)
        layout1.addWidget(form2)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        thirdTitle = QLabel('Margin')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdTitle.setFont(font)
        thirdTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(thirdTitle)

        thirdSubTitle1 = QLabel('Interference [dB]')
        thirdSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle1Value.setValidator(QDoubleValidator())
        thirdSubTitle1Value.setText(str(self.interference))
        thirdSubTitle1Value.setDisabled(True)
        thirdSubTitle1.setFont(font)

        thirdSubTitle2 = QLabel('Mask Effect [dB]')
        thirdSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle2Value.setValidator(QDoubleValidator())
        thirdSubTitle2Value.setDisabled(True)
        thirdSubTitle2Value.setText(str(self.effet_masque))
        thirdSubTitle2.setFont(font)

        thirdSubTitle3 = QLabel('Human Body [dB]')
        thirdSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle3Value.setValidator(QDoubleValidator())
        thirdSubTitle3Value.setText(str(self.corps_humain))
        thirdSubTitle3Value.setDisabled(True)
        thirdSubTitle3.setFont(font)

        thirdSubTitle4 = QLabel('Indoor Penetration [dB]')
        thirdSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle4Value.setValidator(QDoubleValidator())
        thirdSubTitle4Value.setText(str(self.penetration_interrieur_batiment))
        thirdSubTitle4Value.setDisabled(True)
        thirdSubTitle4.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(thirdSubTitle1Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(thirdSubTitle2Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter1.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(thirdSubTitle3Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2)
        layoutFormTransmitter2.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(thirdSubTitle4Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        layoutFormTransmitter3.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        form3 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(thirdSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(thirdSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(thirdSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(thirdSubTitle4, layoutWidgetTransmitter3)
        form3.setLayout(formLayout)
        layout1.addWidget(form3)

        tab1Information.setLayout(layout1)
        scroll = QScrollArea()
        scroll.setWidget(tab1Information)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        layoutTab.addWidget(scroll, 0,0)

        self.tab1.setLayout(layoutTab)

        buttonLayout = QHBoxLayout()
        calculLayout = QVBoxLayout()

        titleLM = QLabel("Uplink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLM.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLM.setStyleSheet("QLabel{color:green;}")

        titleLD = QLabel("Downlink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLD.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLD.setStyleSheet("QLabel{color:green;}")

        previousBtn = QPushButton('Previous', self)
        previousBtn.setFont(QFont(const.font, const.fontSizeText,))
        previousBtn.clicked.connect(self.previousBtn)

        suivantBtn = QPushButton('Next', self)
        suivantBtn.setFont(QFont(const.font, const.fontSizeText,))
        suivantBtn.clicked.connect(self.suivantBtn)

        buttonLayout.addWidget(previousBtn)
        buttonLayout.addStretch()
        buttonLayout.addWidget(suivantBtn)
        
        buttons = QWidget()
        buttons.setLayout(buttonLayout)
        layoutTab.addWidget(buttons, 1,0)

    def showEltModelUMA(self):
        tab1Information = QWidget()
        layout1 = QVBoxLayout()
        layoutTab = QGridLayout()

        fourTitle = QLabel('Parameters')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourTitle.setFont(font)
        fourTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(fourTitle)

        fourSubTitle1 = QLabel('Duplex Mode')
        fourSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle1Value.setText("TDD")
        fourSubTitle1Value.setDisabled(True)
        fourSubTitle1.setFont(font)

        fourSubTitle2 = QLabel('Rate [Mbps]')
        fourSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle2Value.setText('variable')
        fourSubTitle2Value.setDisabled(True)
        fourSubTitle2.setFont(font)

        fourSubTitle3 = QLabel('Frequency [MHz]')
        fourSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle3Value.setValidator(QDoubleValidator())
        fourSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle3Value.setText('3500')
        fourSubTitle3.setFont(font)

        fourSubTitle4 = QLabel('Bandwidth [MHz]')
        fourSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle4Value.setText('50 ou 100')
        fourSubTitle4Value.setDisabled(True)
        fourSubTitle4.setFont(font)

        fourSubTitle5 = QLabel('Antenna Height BS [m]')
        fourSubTitle5Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle5Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle5Value.setText('30')
        fourSubTitle5Value.setDisabled(True)
        fourSubTitle5Value.setValidator(QDoubleValidator())
        fourSubTitle5.setFont(font)

        fourSubTitle6 = QLabel('Antenna Height UE [m]')
        fourSubTitle6Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle6Value.setText('1,70')
        fourSubTitle6Value.setDisabled(True)
        fourSubTitle6Value.setValidator(QDoubleValidator())
        fourSubTitle6.setFont(font)

        fourSubTitle7 = QLabel('Coverage Probability')
        fourSubTitle7Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle7Value.setText('0.9')
        fourSubTitle7Value.setDisabled(True)
        fourSubTitle7Value.setValidator(QDoubleValidator())
        fourSubTitle7.setFont(font)

        fourSubTitle8 = QLabel('Standard deviation mask effect [dB]')
        fourSubTitle8Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle8Value.setText('7')
        fourSubTitle8Value.setValidator(QDoubleValidator())
        fourSubTitle8Value.setDisabled(True)
        fourSubTitle8.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(fourSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(fourSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel('Mbps'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(fourSubTitle3Value, 0, 0)
        layoutFormTransmitter2.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(fourSubTitle4Value, 0, 0)
        layoutFormTransmitter3.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        layoutFormTransmitter4 = QGridLayout()
        layoutWidgetTransmitter4 = QWidget()
        layoutFormTransmitter4.addWidget(fourSubTitle5Value, 0, 0)
        layoutFormTransmitter4.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter4.setLayout(layoutFormTransmitter4)

        layoutFormTransmitter5 = QGridLayout()
        layoutWidgetTransmitter5 = QWidget()
        layoutFormTransmitter5.addWidget(fourSubTitle6Value, 0, 0)
        layoutFormTransmitter5.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter5.setLayout(layoutFormTransmitter5)

        layoutFormTransmitter6 = QGridLayout()
        layoutWidgetTransmitter6 = QWidget()
        layoutFormTransmitter6.addWidget(fourSubTitle7Value, 0, 0)
        layoutFormTransmitter6.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter6.setLayout(layoutFormTransmitter6)

        layoutFormTransmitter7 = QGridLayout()
        layoutWidgetTransmitter7 = QWidget()
        layoutFormTransmitter7.addWidget(fourSubTitle8Value, 0, 0)
        layoutFormTransmitter7.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter7.setLayout(layoutFormTransmitter7)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(fourSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(fourSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(fourSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(fourSubTitle4, layoutWidgetTransmitter3)
        formLayout.addRow(fourSubTitle5, layoutWidgetTransmitter4)
        formLayout.addRow(fourSubTitle6, layoutWidgetTransmitter5)
        formLayout.addRow(fourSubTitle7, layoutWidgetTransmitter6)
        formLayout.addRow(fourSubTitle8, layoutWidgetTransmitter7)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        firstTitle = QLabel('Transmission (UE)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstTitle.setFont(font)
        firstTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(firstTitle)

        firstSubTitle1 = QLabel('Transmission Power')
        firstSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle1Value.setValidator(QDoubleValidator())
        firstSubTitle1Value.setText(str(self.puissance_transmission))
        firstSubTitle1Value.setDisabled(True)
        firstSubTitle1.setFont(font)

        firstSubTitle2 = QLabel('Antenna Gain')
        firstSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle2Value.setValidator(QDoubleValidator())
        firstSubTitle2Value.setText(str(self.gain_antenne_transition))
        firstSubTitle2Value.setDisabled(True)
        firstSubTitle2.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(firstSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(firstSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(firstSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(firstSubTitle2, layoutWidgetTransmitter1)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        secondTitle = QLabel('Reception (Base Station)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondTitle.setFont(font)
        secondTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(secondTitle)

        secondSubTitle1 = QLabel('SINR [dB]')
        secondSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle1Value.setText(str(self.sinr))
        secondSubTitle1Value.setDisabled(True)
        secondSubTitle1.setFont(font)

        secondSubTitle2 = QLabel('Noise Density [dBm/Hz]')
        secondSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle2Value.setValidator(QDoubleValidator())
        secondSubTitle2Value.setDisabled(True)
        secondSubTitle2Value.setText(str(self.density_bruit))
        secondSubTitle2.setFont(font)

        secondSubTitle3 = QLabel('Noise Power [dBm]')
        secondSubTitle3Value = QLineEdit(self)
        secondSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle3Value.setValidator(QDoubleValidator())
        secondSubTitle3Value.setText(str(self.puissance_bruit))
        secondSubTitle3Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle3.setFont(font)

        secondSubTitle4 = QLabel('Noise Figure [dB]')
        secondSubTitle4Value = QLineEdit(self)
        secondSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle4Value.setValidator(QDoubleValidator())
        secondSubTitle4Value.setText(str(self.facteur_bruit))
        secondSubTitle4Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle4.setFont(font)

        secondSubTitle6 = QLabel('Cable Loss [dB]')
        secondSubTitle6Value = QLineEdit(self)
        secondSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle6Value.setValidator(QDoubleValidator())
        secondSubTitle6Value.setText(str(self.perte_cable))
        secondSubTitle6Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle6.setFont(font)

        secondSubTitle7 = QLabel('Sensitivity [dBm]')
        secondSubTitle7Value = QLineEdit(self)
        secondSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle7Value.setValidator(QDoubleValidator())
        secondSubTitle7Value.setText(str(self.sensibility))
        secondSubTitle7Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle7.setFont(font)

        secondSubTitle8 = QLabel('Number of Antenna Elements')
        secondSubTitle8Value = QLineEdit(self)
        secondSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle8Value.setValidator(QDoubleValidator())
        secondSubTitle8Value.setText(str(self.nbreEltAntenne))
        secondSubTitle8Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle8.setFont(font)

        secondSubTitle9 = QLabel('Nomber of TXRU')
        secondSubTitle9Value = QLineEdit(self)
        secondSubTitle9Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle9Value.setValidator(QDoubleValidator())
        secondSubTitle9Value.setText(str(self.nbreTXRU))
        secondSubTitle9Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle9.setFont(font)

        secondSubTitle10 = QLabel('Nomber of Antenna Ports')
        secondSubTitle10Value = QLineEdit(self)
        secondSubTitle10Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle10Value.setValidator(QDoubleValidator())
        secondSubTitle10Value.setText(str(self.nbrePortAntenne))
        secondSubTitle10Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle10.setFont(font)

        secondSubTitle11 = QLabel('Network Antenna Gain [dBi]')
        secondSubTitle11Value = QLineEdit(self)
        secondSubTitle11Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle11Value.setValidator(QDoubleValidator())
        secondSubTitle11Value.setText(str(self.gainReseauAntenne))
        secondSubTitle11Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle11.setFont(font)

        secondSubTitle12 = QLabel('Subnetwork Antenna Gain [dBi]')
        secondSubTitle12Value = QLineEdit(self)
        secondSubTitle12Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle12Value.setValidator(QDoubleValidator())
        secondSubTitle12Value.setText(str(self.gainSousReseauAntenne))
        secondSubTitle12Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle12.setFont(font)

        secondSubTitle13 = QLabel('Received Power [dBm]')
        secondSubTitle13Value = QLineEdit(self)
        secondSubTitle13Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle13Value.setValidator(QDoubleValidator())
        secondSubTitle13Value.setText("Variable")
        secondSubTitle13Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle13.setFont(font)

        decibel = QLabel('dB')
        decibel.setFont(QFont(const.font, const.fontSizeText,))

        layoutForm = QGridLayout()
        layoutWidget = QWidget()
        layoutForm2 = QGridLayout()
        layoutWidget2 = QWidget()
        layoutForm3 = QGridLayout()
        layoutWidget3 = QWidget()
        layoutForm4 = QGridLayout()
        layoutWidget4 = QWidget()
        layoutForm6 = QGridLayout()
        layoutWidget6 = QWidget()
        layoutForm7 = QGridLayout()
        layoutWidget7 = QWidget()
        layoutForm8 = QGridLayout()
        layoutWidget8 = QWidget()
        layoutForm9 = QGridLayout()
        layoutWidget9 = QWidget()
        layoutForm10 = QGridLayout()
        layoutWidget10 = QWidget()
        layoutForm11 = QGridLayout()
        layoutWidget11 = QWidget()
        layoutForm12 = QGridLayout()
        layoutWidget12 = QWidget()
        layoutForm13 = QGridLayout()
        layoutWidget13 = QWidget()

        layoutForm.addWidget(secondSubTitle1Value, 0, 0)
        layoutForm.addWidget(QLabel('dB'), 0, 1)
        layoutWidget.setLayout(layoutForm)

        layoutForm2.addWidget(secondSubTitle2Value, 0, 0)
        layoutForm2.addWidget(QLabel('dBm/Hz'), 0, 1)
        layoutWidget2.setLayout(layoutForm2)

        layoutForm3.addWidget(secondSubTitle3Value, 0, 0)
        layoutForm3.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget3.setLayout(layoutForm3)

        layoutForm4.addWidget(secondSubTitle4Value, 0, 0)
        layoutForm4.addWidget(QLabel('dB'), 0, 1)
        layoutWidget4.setLayout(layoutForm4)

        layoutForm6.addWidget(secondSubTitle6Value, 0, 0)
        layoutForm6.addWidget(QLabel('dB'), 0, 1)
        layoutWidget6.setLayout(layoutForm6)

        layoutForm7.addWidget(secondSubTitle7Value, 0, 0)
        layoutForm7.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget7.setLayout(layoutForm7)

        layoutForm8.addWidget(secondSubTitle8Value, 0, 0)
        layoutForm8.addWidget(QLabel(''), 0, 1)
        layoutWidget8.setLayout(layoutForm8)

        layoutForm9.addWidget(secondSubTitle9Value, 0, 0)
        layoutForm9.addWidget(QLabel(''), 0, 1)
        layoutWidget9.setLayout(layoutForm9)

        layoutForm10.addWidget(secondSubTitle10Value, 0, 0)
        layoutForm10.addWidget(QLabel(''), 0, 1)
        layoutWidget10.setLayout(layoutForm10)

        layoutForm11.addWidget(secondSubTitle11Value, 0, 0)
        layoutForm11.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget11.setLayout(layoutForm11)

        layoutForm12.addWidget(secondSubTitle12Value, 0, 0)
        layoutForm12.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget12.setLayout(layoutForm12)

        layoutForm13.addWidget(secondSubTitle13Value, 0, 0)
        layoutForm13.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget13.setLayout(layoutForm13)

        form2 = QWidget()
        formLayout1 = QFormLayout()
        formLayout1.addRow(secondSubTitle1, layoutWidget)
        formLayout1.addRow(secondSubTitle2, layoutWidget2)
        formLayout1.addRow(secondSubTitle3, layoutWidget3)
        formLayout1.addRow(secondSubTitle4, layoutWidget4)
        formLayout1.addRow(secondSubTitle6, layoutWidget6)
        formLayout1.addRow(secondSubTitle7, layoutWidget7)
        formLayout1.addRow(secondSubTitle8, layoutWidget8)
        formLayout1.addRow(secondSubTitle9, layoutWidget9)
        formLayout1.addRow(secondSubTitle10, layoutWidget10)
        formLayout1.addRow(secondSubTitle11, layoutWidget11)
        formLayout1.addRow(secondSubTitle12, layoutWidget12)
        formLayout1.addRow(secondSubTitle13, layoutWidget13)
        form2.setLayout(formLayout1)
        layout1.addWidget(form2)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        thirdTitle = QLabel('Margin')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdTitle.setFont(font)
        thirdTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(thirdTitle)

        thirdSubTitle1 = QLabel('Interference [dB]')
        thirdSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle1Value.setValidator(QDoubleValidator())
        thirdSubTitle1Value.setText(str(self.interference))
        thirdSubTitle1Value.setDisabled(True)
        thirdSubTitle1.setFont(font)

        thirdSubTitle2 = QLabel('Mask Effect [dB]')
        thirdSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle2Value.setValidator(QDoubleValidator())
        thirdSubTitle2Value.setText(str(self.effet_masque))
        thirdSubTitle2Value.setDisabled(True)
        thirdSubTitle2.setFont(font)

        thirdSubTitle3 = QLabel('Human Body [dB]')
        thirdSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle3Value.setValidator(QDoubleValidator())
        thirdSubTitle3Value.setText(str(self.corps_humain))
        thirdSubTitle3Value.setDisabled(True)
        thirdSubTitle3.setFont(font)

        thirdSubTitle4 = QLabel('Indoor Penetration [dB]')
        thirdSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle4Value.setValidator(QDoubleValidator())
        thirdSubTitle4Value.setText(str(self.penetration_interrieur_batiment))
        thirdSubTitle4Value.setDisabled(True)
        thirdSubTitle4.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(thirdSubTitle1Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(thirdSubTitle2Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter1.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(thirdSubTitle3Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2)
        layoutFormTransmitter2.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(thirdSubTitle4Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        layoutFormTransmitter3.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        form3 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(thirdSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(thirdSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(thirdSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(thirdSubTitle4, layoutWidgetTransmitter3)
        form3.setLayout(formLayout)
        layout1.addWidget(form3)


        tab1Information.setLayout(layout1)
        scroll = QScrollArea()
        scroll.setWidget(tab1Information)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        layoutTab.addWidget(scroll, 0,0)

        self.tab2.setLayout(layoutTab)

        buttonLayout = QHBoxLayout()
        calculLayout = QVBoxLayout()

        titleLM = QLabel("Uplink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLM.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLM.setStyleSheet("QLabel{color:green;}")

        titleLD = QLabel("Downlink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLD.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLD.setStyleSheet("QLabel{color:green;}")

        previousBtn = QPushButton('Previous', self)
        previousBtn.setFont(QFont(const.font, const.fontSizeText,))
        previousBtn.clicked.connect(self.previousBtn)

        suivantBtn = QPushButton('Next', self)
        suivantBtn.setFont(QFont(const.font, const.fontSizeText,))
        suivantBtn.clicked.connect(self.suivantBtn)

        buttonLayout.addWidget(previousBtn)
        buttonLayout.addStretch()
        buttonLayout.addWidget(suivantBtn)
        
        buttons = QWidget()
        buttons.setLayout(buttonLayout)
        layoutTab.addWidget(buttons, 1,0)

    def showEltModelUMI(self):
        tab1Information = QWidget()
        layout1 = QVBoxLayout()
        layoutTab = QGridLayout()

        fourTitle = QLabel('Parameters')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourTitle.setFont(font)
        fourTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(fourTitle)

        fourSubTitle1 = QLabel('Duplex Mode')
        fourSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle1Value.setText("TDD")
        fourSubTitle1Value.setDisabled(True)
        fourSubTitle1.setFont(font)

        fourSubTitle2 = QLabel('Rate [Mbps]')
        fourSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle2Value.setText('variable')
        fourSubTitle2Value.setDisabled(True)
        fourSubTitle2.setFont(font)

        fourSubTitle3 = QLabel('Frequency [MHz]')
        fourSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle3Value.setValidator(QDoubleValidator())
        fourSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle3Value.setText('3500')
        fourSubTitle3.setFont(font)

        fourSubTitle4 = QLabel('Bandwidth [MHz]')
        fourSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle4Value.setText('50 ou 100')
        fourSubTitle4Value.setDisabled(True)
        fourSubTitle4.setFont(font)

        fourSubTitle5 = QLabel('Antenna Height BS [m]')
        fourSubTitle5Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle5Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle5Value.setText('30')
        fourSubTitle5Value.setDisabled(True)
        fourSubTitle5Value.setValidator(QDoubleValidator())
        fourSubTitle5.setFont(font)

        fourSubTitle6 = QLabel('Antenna Height UE [m]')
        fourSubTitle6Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle6Value.setText('1,70')
        fourSubTitle6Value.setDisabled(True)
        fourSubTitle6Value.setValidator(QDoubleValidator())
        fourSubTitle6.setFont(font)

        fourSubTitle7 = QLabel('Coverage Probability')
        fourSubTitle7Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle7Value.setText('0.9')
        fourSubTitle7Value.setDisabled(True)
        fourSubTitle7Value.setValidator(QDoubleValidator())
        fourSubTitle7.setFont(font)

        fourSubTitle8 = QLabel('Standard deviation mask effect [dB]')
        fourSubTitle8Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle8Value.setText('7')
        fourSubTitle8Value.setValidator(QDoubleValidator())
        fourSubTitle8Value.setDisabled(True)
        fourSubTitle8.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(fourSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(fourSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel('Mbps'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(fourSubTitle3Value, 0, 0)
        layoutFormTransmitter2.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(fourSubTitle4Value, 0, 0)
        layoutFormTransmitter3.addWidget(QLabel('MHz'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        layoutFormTransmitter4 = QGridLayout()
        layoutWidgetTransmitter4 = QWidget()
        layoutFormTransmitter4.addWidget(fourSubTitle5Value, 0, 0)
        layoutFormTransmitter4.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter4.setLayout(layoutFormTransmitter4)

        layoutFormTransmitter5 = QGridLayout()
        layoutWidgetTransmitter5 = QWidget()
        layoutFormTransmitter5.addWidget(fourSubTitle6Value, 0, 0)
        layoutFormTransmitter5.addWidget(QLabel('m'), 0, 1)
        layoutWidgetTransmitter5.setLayout(layoutFormTransmitter5)

        layoutFormTransmitter6 = QGridLayout()
        layoutWidgetTransmitter6 = QWidget()
        layoutFormTransmitter6.addWidget(fourSubTitle7Value, 0, 0)
        layoutFormTransmitter6.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter6.setLayout(layoutFormTransmitter6)

        layoutFormTransmitter7 = QGridLayout()
        layoutWidgetTransmitter7 = QWidget()
        layoutFormTransmitter7.addWidget(fourSubTitle8Value, 0, 0)
        layoutFormTransmitter7.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter7.setLayout(layoutFormTransmitter7)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(fourSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(fourSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(fourSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(fourSubTitle4, layoutWidgetTransmitter3)
        formLayout.addRow(fourSubTitle5, layoutWidgetTransmitter4)
        formLayout.addRow(fourSubTitle6, layoutWidgetTransmitter5)
        formLayout.addRow(fourSubTitle7, layoutWidgetTransmitter6)
        formLayout.addRow(fourSubTitle8, layoutWidgetTransmitter7)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        firstTitle = QLabel('Transmission (UE)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstTitle.setFont(font)
        firstTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(firstTitle)

        firstSubTitle1 = QLabel('Transmission Power')
        firstSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle1Value.setValidator(QDoubleValidator())
        firstSubTitle1Value.setText(str(self.puissance_transmission))
        firstSubTitle1Value.setDisabled(True)
        firstSubTitle1.setFont(font)

        firstSubTitle2 = QLabel('Antenna Gain')
        firstSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle2Value.setValidator(QDoubleValidator())
        firstSubTitle2Value.setText(str(self.gain_antenne_transition))
        firstSubTitle2Value.setDisabled(True)
        firstSubTitle2.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(firstSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(firstSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel(''), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(firstSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(firstSubTitle2, layoutWidgetTransmitter1)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        secondTitle = QLabel('Reception (Base Station)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondTitle.setFont(font)
        secondTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(secondTitle)

        secondSubTitle1 = QLabel('SINR [dB]')
        secondSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle1Value.setText(str(self.sinr))
        secondSubTitle1Value.setDisabled(True)
        secondSubTitle1.setFont(font)

        secondSubTitle2 = QLabel('Noise Density [dBm/Hz]')
        secondSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle2Value.setValidator(QDoubleValidator())
        secondSubTitle2Value.setDisabled(True)
        secondSubTitle2Value.setText(str(self.density_bruit))
        secondSubTitle2.setFont(font)

        secondSubTitle3 = QLabel('Noise Power [dBm]')
        secondSubTitle3Value = QLineEdit(self)
        secondSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle3Value.setValidator(QDoubleValidator())
        secondSubTitle3Value.setText(str(self.puissance_bruit))
        secondSubTitle3Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle3.setFont(font)

        secondSubTitle4 = QLabel('Noise figure [dB]')
        secondSubTitle4Value = QLineEdit(self)
        secondSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle4Value.setValidator(QDoubleValidator())
        secondSubTitle4Value.setText(str(self.facteur_bruit))
        secondSubTitle4Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle4.setFont(font)

        secondSubTitle6 = QLabel('Cable Loss[dB]')
        secondSubTitle6Value = QLineEdit(self)
        secondSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle6Value.setValidator(QDoubleValidator())
        secondSubTitle6Value.setText(str(self.perte_cable))
        secondSubTitle6Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle6.setFont(font)

        secondSubTitle7 = QLabel('Sensitivity [dBm]')
        secondSubTitle7Value = QLineEdit(self)
        secondSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle7Value.setValidator(QDoubleValidator())
        secondSubTitle7Value.setText(str(self.sensibility))
        secondSubTitle7Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle7.setFont(font)

        secondSubTitle8 = QLabel('Number of Antenna Elements')
        secondSubTitle8Value = QLineEdit(self)
        secondSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle8Value.setValidator(QDoubleValidator())
        secondSubTitle8Value.setText(str(self.nbreEltAntenne))
        secondSubTitle8Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle8.setFont(font)

        secondSubTitle9 = QLabel('Number of TXRU')
        secondSubTitle9Value = QLineEdit(self)
        secondSubTitle9Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle9Value.setValidator(QDoubleValidator())
        secondSubTitle9Value.setText(str(self.nbreTXRU))
        secondSubTitle9Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle9.setFont(font)

        secondSubTitle10 = QLabel('Number of antenna ports')
        secondSubTitle10Value = QLineEdit(self)
        secondSubTitle10Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle10Value.setValidator(QDoubleValidator())
        secondSubTitle10Value.setText(str(self.nbrePortAntenne))
        secondSubTitle10Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle10.setFont(font)

        secondSubTitle11 = QLabel('Network Antenna Gain [dBi]')
        secondSubTitle11Value = QLineEdit(self)
        secondSubTitle11Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle11Value.setValidator(QDoubleValidator())
        secondSubTitle11Value.setText(str(self.gainReseauAntenne))
        secondSubTitle11Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle11.setFont(font)

        secondSubTitle12 = QLabel('Subnet Antenna Gain [dBi]')
        secondSubTitle12Value = QLineEdit(self)
        secondSubTitle12Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle12Value.setValidator(QDoubleValidator())
        secondSubTitle12Value.setText(str(self.gainSousReseauAntenne))
        secondSubTitle12Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle12.setFont(font)

        secondSubTitle13 = QLabel('Received Power [dBm]')
        secondSubTitle13Value = QLineEdit(self)
        secondSubTitle13Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle13Value.setValidator(QDoubleValidator())
        secondSubTitle13Value.setText("Variable")
        secondSubTitle13Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle13.setFont(font)

        decibel = QLabel('dB')
        decibel.setFont(QFont(const.font, const.fontSizeText,))

        layoutForm = QGridLayout()
        layoutWidget = QWidget()
        layoutForm2 = QGridLayout()
        layoutWidget2 = QWidget()
        layoutForm3 = QGridLayout()
        layoutWidget3 = QWidget()
        layoutForm4 = QGridLayout()
        layoutWidget4 = QWidget()
        layoutForm6 = QGridLayout()
        layoutWidget6 = QWidget()
        layoutForm7 = QGridLayout()
        layoutWidget7 = QWidget()
        layoutForm8 = QGridLayout()
        layoutWidget8 = QWidget()
        layoutForm9 = QGridLayout()
        layoutWidget9 = QWidget()
        layoutForm10 = QGridLayout()
        layoutWidget10 = QWidget()
        layoutForm11 = QGridLayout()
        layoutWidget11 = QWidget()
        layoutForm12 = QGridLayout()
        layoutWidget12 = QWidget()
        layoutForm13 = QGridLayout()
        layoutWidget13 = QWidget()

        layoutForm.addWidget(secondSubTitle1Value, 0, 0)
        layoutForm.addWidget(QLabel('dB'), 0, 1)
        layoutWidget.setLayout(layoutForm)

        layoutForm2.addWidget(secondSubTitle2Value, 0, 0)
        layoutForm2.addWidget(QLabel('dBm/Hz'), 0, 1)
        layoutWidget2.setLayout(layoutForm2)

        layoutForm3.addWidget(secondSubTitle3Value, 0, 0)
        layoutForm3.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget3.setLayout(layoutForm3)

        layoutForm4.addWidget(secondSubTitle4Value, 0, 0)
        layoutForm4.addWidget(QLabel('dB'), 0, 1)
        layoutWidget4.setLayout(layoutForm4)

        layoutForm6.addWidget(secondSubTitle6Value, 0, 0)
        layoutForm6.addWidget(QLabel('dB'), 0, 1)
        layoutWidget6.setLayout(layoutForm6)

        layoutForm7.addWidget(secondSubTitle7Value, 0, 0)
        layoutForm7.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget7.setLayout(layoutForm7)

        layoutForm8.addWidget(secondSubTitle8Value, 0, 0)
        layoutForm8.addWidget(QLabel(''), 0, 1)
        layoutWidget8.setLayout(layoutForm8)

        layoutForm9.addWidget(secondSubTitle9Value, 0, 0)
        layoutForm9.addWidget(QLabel(''), 0, 1)
        layoutWidget9.setLayout(layoutForm9)

        layoutForm10.addWidget(secondSubTitle10Value, 0, 0)
        layoutForm10.addWidget(QLabel(''), 0, 1)
        layoutWidget10.setLayout(layoutForm10)

        layoutForm11.addWidget(secondSubTitle11Value, 0, 0)
        layoutForm11.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget11.setLayout(layoutForm11)

        layoutForm12.addWidget(secondSubTitle12Value, 0, 0)
        layoutForm12.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget12.setLayout(layoutForm12)

        layoutForm13.addWidget(secondSubTitle13Value, 0, 0)
        layoutForm13.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget13.setLayout(layoutForm13)

        form2 = QWidget()
        formLayout1 = QFormLayout()
        formLayout1.addRow(secondSubTitle1, layoutWidget)
        formLayout1.addRow(secondSubTitle2, layoutWidget2)
        formLayout1.addRow(secondSubTitle3, layoutWidget3)
        formLayout1.addRow(secondSubTitle4, layoutWidget4)
        formLayout1.addRow(secondSubTitle6, layoutWidget6)
        formLayout1.addRow(secondSubTitle7, layoutWidget7)
        formLayout1.addRow(secondSubTitle8, layoutWidget8)
        formLayout1.addRow(secondSubTitle9, layoutWidget9)
        formLayout1.addRow(secondSubTitle10, layoutWidget10)
        formLayout1.addRow(secondSubTitle11, layoutWidget11)
        formLayout1.addRow(secondSubTitle12, layoutWidget12)
        formLayout1.addRow(secondSubTitle13, layoutWidget13)
        form2.setLayout(formLayout1)
        layout1.addWidget(form2)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        thirdTitle = QLabel('Margin')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdTitle.setFont(font)
        thirdTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(thirdTitle)

        thirdSubTitle1 = QLabel('Interference [dB]')
        thirdSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle1Value.setValidator(QDoubleValidator())
        thirdSubTitle1Value.setText(str(self.interference))
        thirdSubTitle1Value.setDisabled(True)
        thirdSubTitle1.setFont(font)

        thirdSubTitle2 = QLabel('Mask Effect [dB]')
        thirdSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle2Value.setValidator(QDoubleValidator())
        thirdSubTitle2Value.setText(str(self.effet_masque))
        thirdSubTitle2Value.setDisabled(True)
        thirdSubTitle2.setFont(font)

        thirdSubTitle3 = QLabel('Human Body [dB]')
        thirdSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle3Value.setValidator(QDoubleValidator())
        thirdSubTitle3Value.setText(str(self.corps_humain))
        thirdSubTitle3Value.setDisabled(True)
        thirdSubTitle3.setFont(font)

        thirdSubTitle4 = QLabel('Indoor Penetration [dB]')
        thirdSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle4Value.setValidator(QDoubleValidator())
        thirdSubTitle4Value.setText(str(self.penetration_interrieur_batiment))
        thirdSubTitle4Value.setDisabled(True)
        thirdSubTitle4.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(thirdSubTitle1Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(thirdSubTitle2Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter1.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(thirdSubTitle3Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2)
        layoutFormTransmitter2.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(thirdSubTitle4Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        layoutFormTransmitter3.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        form3 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(thirdSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(thirdSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(thirdSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(thirdSubTitle4, layoutWidgetTransmitter3)
        form3.setLayout(formLayout)
        layout1.addWidget(form3)


        tab1Information.setLayout(layout1)
        scroll = QScrollArea()
        scroll.setWidget(tab1Information)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        layoutTab.addWidget(scroll, 0,0)

        self.tab3.setLayout(layoutTab)

        buttonLayout = QHBoxLayout()
        calculLayout = QVBoxLayout()

        titleLM = QLabel("Uplink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLM.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLM.setStyleSheet("QLabel{color:green;}")

        titleLD = QLabel("Downlink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLD.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLD.setStyleSheet("QLabel{color:green;}")

        self.pireD_ModelUmi = QLabel('EIRP[dBm]')
        self.pireD_ModelUmi.setFont(font)
        self.pireD_ModelUmiValue = QLineEdit(self)
        self.pireD_ModelUmiValue.setValidator(QDoubleValidator())
        self.pireD_ModelUmiValue.setDisabled(True)
        self.pireD_ModelUmiValue.setStyleSheet("QLineEdit{color:green;}")
        self.pireD_ModelUmiValue.setFont(font)
        
        self.margeD_ModelUmi = QLabel('Total Margin [dB]')
        self.margeD_ModelUmi.setFont(font)
        self.margeD_ModelUmiValue = QLineEdit(self)
        self.margeD_ModelUmiValue.setDisabled(True)
        self.margeD_ModelUmiValue.setStyleSheet("QLineEdit{color:green;}")
        self.margeD_ModelUmiValue.setValidator(QDoubleValidator())
        self.margeD_ModelUmiValue.setFont(font)

        formCalcul = QWidget()
        formCalculLayout = QFormLayout()
        formCalculLayout.addRow(titleLD, QLabel(''))
        formCalculLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalculLayout.addRow(self.pireD_ModelUmi, self.pireD_ModelUmiValue)
        formCalculLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalculLayout.addRow(self.margeD_ModelUmi, self.margeD_ModelUmiValue)
        formCalculLayout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul.setLayout(formCalculLayout)

        self.pireM_ModelUmi = QLabel('EIRP [dBm]')
        self.pireM_ModelUmi.setFont(font)
        self.pireM_ModelUmiValue = QLineEdit(self)
        self.pireM_ModelUmiValue.setValidator(QDoubleValidator())
        self.pireM_ModelUmiValue.setDisabled(True)
        self.pireM_ModelUmiValue.setStyleSheet("QLineEdit{color:green;}")
        self.pireM_ModelUmiValue.setFont(font)

        self.margeM_ModelUmi = QLabel('Total Margin [dB]')
        self.margeM_ModelUmi.setFont(font)
        self.margeM_ModelUmiValue = QLineEdit(self)
        self.margeM_ModelUmiValue.setDisabled(True)
        self.margeM_ModelUmiValue.setValidator(QDoubleValidator())
        self.margeM_ModelUmiValue.setStyleSheet("QLineEdit{color:green;}")
        self.margeM_ModelUmiValue.setFont(font)

        formCalcul1 = QWidget()
        formCalcul1Layout = QFormLayout()
        formCalcul1Layout.addRow(titleLM, QLabel(''))
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1Layout.addRow(self.pireM_ModelUmi, self.pireM_ModelUmiValue)
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1Layout.addRow(self.margeM_ModelUmi, self.margeM_ModelUmiValue)
        formCalcul1Layout.addItem(QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Expanding))
        formCalcul1.setLayout(formCalcul1Layout)

        previousBtn = QPushButton('Previous', self)
        previousBtn.setFont(QFont(const.font, const.fontSizeText,))
        previousBtn.clicked.connect(self.previousBtn)

        calculBtn = QPushButton('Calculate', self)
        calculBtn.setFont(QFont(const.font, const.fontSizeText,))
        calculBtn.clicked.connect(self.calculModelUmiBtn)

        suivantBtn = QPushButton('Next', self)
        suivantBtn.setFont(QFont(const.font, const.fontSizeText,))
        suivantBtn.clicked.connect(self.suivantBtn)

        buttonLayout.addWidget(previousBtn)
        buttonLayout.addStretch()
        buttonLayout.addWidget(suivantBtn)
        
        buttons = QWidget()
        buttons.setLayout(buttonLayout)
        layoutTab.addWidget(buttons, 1,0)

    def showEltModelINH(self):
        tab1Information = QWidget()
        layout1 = QVBoxLayout()
        layoutTab = QGridLayout()

        fourTitle = QLabel('Parameters')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourTitle.setFont(font)
        fourTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(fourTitle)

        fourSubTitle1 = QLabel('Duplex Mode')
        fourSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle1Value.setText("TDD")
        fourSubTitle1Value.setDisabled(True)
        fourSubTitle1.setFont(font)

        fourSubTitle2 = QLabel('Rate [Mbps]')
        fourSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle2Value.setText('variable')
        fourSubTitle2Value.setDisabled(True)
        fourSubTitle2.setFont(font)

        fourSubTitle3 = QLabel('Frequency [MHz]')
        fourSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle3Value.setValidator(QDoubleValidator())
        fourSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle3Value.setText('3500')
        fourSubTitle3.setFont(font)

        fourSubTitle4 = QLabel('Bandwidth [MHz]')
        fourSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle4Value.setText('50 ou 100')
        fourSubTitle4Value.setDisabled(True)
        fourSubTitle4.setFont(font)

        fourSubTitle5 = QLabel('Antenna Height BS [m]')
        fourSubTitle5Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle5Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle5Value.setText('30')
        fourSubTitle5Value.setDisabled(True)
        fourSubTitle5Value.setValidator(QDoubleValidator())
        fourSubTitle5.setFont(font)

        fourSubTitle6 = QLabel('Antenna Height UE [m]')
        fourSubTitle6Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle6Value.setText('1,70')
        fourSubTitle6Value.setDisabled(True)
        fourSubTitle6Value.setValidator(QDoubleValidator())
        fourSubTitle6.setFont(font)

        fourSubTitle7 = QLabel('Coverage Probability')
        fourSubTitle7Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle7Value.setText('0.9')
        fourSubTitle7Value.setDisabled(True)
        fourSubTitle7Value.setValidator(QDoubleValidator())
        fourSubTitle7.setFont(font)

        fourSubTitle8 = QLabel('Standard deviation mask effect [dB]')
        fourSubTitle8Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        fourSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        fourSubTitle8Value.setText('7')
        fourSubTitle8Value.setValidator(QDoubleValidator())
        fourSubTitle8Value.setDisabled(True)
        fourSubTitle8.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(fourSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel('dBm'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(fourSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(fourSubTitle3Value, 0, 0)
        layoutFormTransmitter2.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(fourSubTitle4Value, 0, 0)
        layoutFormTransmitter3.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        layoutFormTransmitter4 = QGridLayout()
        layoutWidgetTransmitter4 = QWidget()
        layoutFormTransmitter4.addWidget(fourSubTitle5Value, 0, 0)
        layoutFormTransmitter4.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter4.setLayout(layoutFormTransmitter4)

        layoutFormTransmitter5 = QGridLayout()
        layoutWidgetTransmitter5 = QWidget()
        layoutFormTransmitter5.addWidget(fourSubTitle6Value, 0, 0)
        layoutFormTransmitter5.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter5.setLayout(layoutFormTransmitter5)

        layoutFormTransmitter6 = QGridLayout()
        layoutWidgetTransmitter6 = QWidget()
        layoutFormTransmitter6.addWidget(fourSubTitle7Value, 0, 0)
        layoutFormTransmitter6.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter6.setLayout(layoutFormTransmitter6)

        layoutFormTransmitter7 = QGridLayout()
        layoutWidgetTransmitter7 = QWidget()
        layoutFormTransmitter7.addWidget(fourSubTitle8Value, 0, 0)
        layoutFormTransmitter7.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter7.setLayout(layoutFormTransmitter7)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(fourSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(fourSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(fourSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(fourSubTitle4, layoutWidgetTransmitter3)
        formLayout.addRow(fourSubTitle5, layoutWidgetTransmitter4)
        formLayout.addRow(fourSubTitle6, layoutWidgetTransmitter5)
        formLayout.addRow(fourSubTitle7, layoutWidgetTransmitter6)
        formLayout.addRow(fourSubTitle8, layoutWidgetTransmitter7)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        firstTitle = QLabel('Transmission (UE)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstTitle.setFont(font)
        firstTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(firstTitle)

        firstSubTitle1 = QLabel('Transmission Power')
        firstSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle1Value.setValidator(QDoubleValidator())
        firstSubTitle1Value.setText(str(self.puissance_transmission))
        firstSubTitle1Value.setDisabled(True)
        firstSubTitle1.setFont(font)

        firstSubTitle2 = QLabel('Antenna Gain')
        firstSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        firstSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        firstSubTitle2Value.setValidator(QDoubleValidator())
        firstSubTitle2Value.setText(str(self.gain_antenne_transition))
        firstSubTitle2Value.setDisabled(True)
        firstSubTitle2.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(firstSubTitle1Value, 0, 0)
        layoutFormTransmitter.addWidget(QLabel('dBm'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(firstSubTitle2Value, 0, 0)
        layoutFormTransmitter1.addWidget(QLabel('dBi'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        form1 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(firstSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(firstSubTitle2, layoutWidgetTransmitter1)
        form1.setLayout(formLayout)
        layout1.addWidget(form1)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        secondTitle = QLabel('Reception (Base Station)')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondTitle.setFont(font)
        secondTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(secondTitle)

        secondSubTitle1 = QLabel('SINR [dB]')
        secondSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle1Value.setText(str(self.sinr))
        secondSubTitle1Value.setDisabled(True)
        secondSubTitle1.setFont(font)

        secondSubTitle2 = QLabel('Noise Density [dBm/Hz]')
        secondSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle2Value.setValidator(QDoubleValidator())
        secondSubTitle2Value.setDisabled(True)
        secondSubTitle2Value.setText(str(self.density_bruit))
        secondSubTitle2.setFont(font)

        secondSubTitle3 = QLabel('Noise Power [dBm]')
        secondSubTitle3Value = QLineEdit(self)
        secondSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle3Value.setValidator(QDoubleValidator())
        secondSubTitle3Value.setText(str(self.puissance_bruit))
        secondSubTitle3Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle3.setFont(font)

        secondSubTitle4 = QLabel('Noise Figure [dB]')
        secondSubTitle4Value = QLineEdit(self)
        secondSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle4Value.setValidator(QDoubleValidator())
        secondSubTitle4Value.setText(str(self.facteur_bruit))
        secondSubTitle4Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle4.setFont(font)

        secondSubTitle6 = QLabel('Cable Loss [dB]')
        secondSubTitle6Value = QLineEdit(self)
        secondSubTitle6Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle6Value.setValidator(QDoubleValidator())
        secondSubTitle6Value.setText(str(self.perte_cable))
        secondSubTitle6Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle6.setFont(font)

        secondSubTitle7 = QLabel('Sensitivity [dBm]')
        secondSubTitle7Value = QLineEdit(self)
        secondSubTitle7Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle7Value.setValidator(QDoubleValidator())
        secondSubTitle7Value.setText(str(self.sensibility))
        secondSubTitle7Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle7.setFont(font)

        secondSubTitle8 = QLabel('Number of antenna elements')
        secondSubTitle8Value = QLineEdit(self)
        secondSubTitle8Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle8Value.setValidator(QDoubleValidator())
        secondSubTitle8Value.setText(str(self.nbreEltAntenne))
        secondSubTitle8Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle8.setFont(font)

        secondSubTitle9 = QLabel('Number of TXRU')
        secondSubTitle9Value = QLineEdit(self)
        secondSubTitle9Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle9Value.setValidator(QDoubleValidator())
        secondSubTitle9Value.setText(str(self.nbreTXRU))
        secondSubTitle9Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle9.setFont(font)

        secondSubTitle10 = QLabel('Number of antenna ports')
        secondSubTitle10Value = QLineEdit(self)
        secondSubTitle10Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle10Value.setValidator(QDoubleValidator())
        secondSubTitle10Value.setText(str(self.nbrePortAntenne))
        secondSubTitle10Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle10.setFont(font)

        secondSubTitle11 = QLabel('Network Antenna Gain [dBi]')
        secondSubTitle11Value = QLineEdit(self)
        secondSubTitle11Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle11Value.setValidator(QDoubleValidator())
        secondSubTitle11Value.setText(str(self.gainReseauAntenne))
        secondSubTitle11Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle11.setFont(font)

        secondSubTitle12 = QLabel('Subnet Antenna Gain [dBi]')
        secondSubTitle12Value = QLineEdit(self)
        secondSubTitle12Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle12Value.setValidator(QDoubleValidator())
        secondSubTitle12Value.setText(str(self.gainSousReseauAntenne))
        secondSubTitle12Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle12.setFont(font)

        secondSubTitle13 = QLabel('Received Power [dBm]')
        secondSubTitle13Value = QLineEdit(self)
        secondSubTitle13Value.setFont(QFont(const.font, const.fontSizeText,))
        secondSubTitle13Value.setValidator(QDoubleValidator())
        secondSubTitle13Value.setText("Variable")
        secondSubTitle13Value.setDisabled(True)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        secondSubTitle13.setFont(font)

        decibel = QLabel('dB')
        decibel.setFont(QFont(const.font, const.fontSizeText,))

        layoutForm = QGridLayout()
        layoutWidget = QWidget()
        layoutForm2 = QGridLayout()
        layoutWidget2 = QWidget()
        layoutForm3 = QGridLayout()
        layoutWidget3 = QWidget()
        layoutForm4 = QGridLayout()
        layoutWidget4 = QWidget()
        layoutForm6 = QGridLayout()
        layoutWidget6 = QWidget()
        layoutForm7 = QGridLayout()
        layoutWidget7 = QWidget()
        layoutForm8 = QGridLayout()
        layoutWidget8 = QWidget()
        layoutForm9 = QGridLayout()
        layoutWidget9 = QWidget()
        layoutForm10 = QGridLayout()
        layoutWidget10 = QWidget()
        layoutForm11 = QGridLayout()
        layoutWidget11 = QWidget()
        layoutForm12 = QGridLayout()
        layoutWidget12 = QWidget()
        layoutForm13 = QGridLayout()
        layoutWidget13 = QWidget()

        layoutForm.addWidget(secondSubTitle1Value, 0, 0)
        layoutForm.addWidget(QLabel('dB'), 0, 1)
        layoutWidget.setLayout(layoutForm)

        layoutForm2.addWidget(secondSubTitle2Value, 0, 0)
        layoutForm2.addWidget(QLabel('dBm/Hz'), 0, 1)
        layoutWidget2.setLayout(layoutForm2)

        layoutForm3.addWidget(secondSubTitle3Value, 0, 0)
        layoutForm3.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget3.setLayout(layoutForm3)

        layoutForm4.addWidget(secondSubTitle4Value, 0, 0)
        layoutForm4.addWidget(QLabel('dB'), 0, 1)
        layoutWidget4.setLayout(layoutForm4)

        layoutForm6.addWidget(secondSubTitle6Value, 0, 0)
        layoutForm6.addWidget(QLabel('dB'), 0, 1)
        layoutWidget6.setLayout(layoutForm6)

        layoutForm7.addWidget(secondSubTitle7Value, 0, 0)
        layoutForm7.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget7.setLayout(layoutForm7)

        layoutForm8.addWidget(secondSubTitle8Value, 0, 0)
        layoutForm8.addWidget(QLabel(''), 0, 1)
        layoutWidget8.setLayout(layoutForm8)

        layoutForm9.addWidget(secondSubTitle9Value, 0, 0)
        layoutForm9.addWidget(QLabel(''), 0, 1)
        layoutWidget9.setLayout(layoutForm9)

        layoutForm10.addWidget(secondSubTitle10Value, 0, 0)
        layoutForm10.addWidget(QLabel(''), 0, 1)
        layoutWidget10.setLayout(layoutForm10)

        layoutForm11.addWidget(secondSubTitle11Value, 0, 0)
        layoutForm11.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget11.setLayout(layoutForm11)

        layoutForm12.addWidget(secondSubTitle12Value, 0, 0)
        layoutForm12.addWidget(QLabel('dBi'), 0, 1)
        layoutWidget12.setLayout(layoutForm12)

        layoutForm13.addWidget(secondSubTitle13Value, 0, 0)
        layoutForm13.addWidget(QLabel('dBm'), 0, 1)
        layoutWidget13.setLayout(layoutForm13)

        form2 = QWidget()
        formLayout1 = QFormLayout()
        formLayout1.addRow(secondSubTitle1, layoutWidget)
        formLayout1.addRow(secondSubTitle2, layoutWidget2)
        formLayout1.addRow(secondSubTitle3, layoutWidget3)
        formLayout1.addRow(secondSubTitle4, layoutWidget4)
        formLayout1.addRow(secondSubTitle6, layoutWidget6)
        formLayout1.addRow(secondSubTitle7, layoutWidget7)
        formLayout1.addRow(secondSubTitle8, layoutWidget8)
        formLayout1.addRow(secondSubTitle9, layoutWidget9)
        formLayout1.addRow(secondSubTitle10, layoutWidget10)
        formLayout1.addRow(secondSubTitle11, layoutWidget11)
        formLayout1.addRow(secondSubTitle12, layoutWidget12)
        formLayout1.addRow(secondSubTitle13, layoutWidget13)
        form2.setLayout(formLayout1)
        layout1.addWidget(form2)
        layout1.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        thirdTitle = QLabel('Margin')
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdTitle.setFont(font)
        thirdTitle.setStyleSheet("QLabel{color:red;}")
        layout1.addWidget(thirdTitle)

        thirdSubTitle1 = QLabel('Interference [dB]')
        thirdSubTitle1Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle1Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle1Value.setValidator(QDoubleValidator())
        thirdSubTitle1Value.setText(str(self.interference))
        thirdSubTitle1Value.setDisabled(True)
        thirdSubTitle1.setFont(font)

        thirdSubTitle2 = QLabel('Mask Effect [dB]')
        thirdSubTitle2Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle2Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle2Value.setValidator(QDoubleValidator())
        thirdSubTitle2Value.setText(str(self.effet_masque))
        thirdSubTitle2Value.setDisabled(True)
        thirdSubTitle2.setFont(font)

        thirdSubTitle3 = QLabel('Human Body [dB]')
        thirdSubTitle3Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle3Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle3Value.setValidator(QDoubleValidator())
        thirdSubTitle3Value.setText(str(self.corps_humain))
        thirdSubTitle3Value.setDisabled(True)
        thirdSubTitle3.setFont(font)

        thirdSubTitle4 = QLabel('Indoor Penetration [dB]')
        thirdSubTitle4Value = QLineEdit(self)
        font = QFont(const.font, const.fontSizeText, QFont.Bold)
        thirdSubTitle4Value.setFont(QFont(const.font, const.fontSizeText,))
        thirdSubTitle4Value.setValidator(QDoubleValidator())
        thirdSubTitle4Value.setText(str(self.penetration_interrieur_batiment))
        thirdSubTitle4Value.setDisabled(True)
        thirdSubTitle4.setFont(font)

        layoutFormTransmitter = QGridLayout()
        layoutWidgetTransmitter = QWidget()
        layoutFormTransmitter.addWidget(thirdSubTitle1Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter.setLayout(layoutFormTransmitter)

        layoutFormTransmitter1 = QGridLayout()
        layoutWidgetTransmitter1 = QWidget()
        layoutFormTransmitter1.addWidget(thirdSubTitle2Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 1)
        layoutFormTransmitter1.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter1.setLayout(layoutFormTransmitter1)

        layoutFormTransmitter2 = QGridLayout()
        layoutWidgetTransmitter2 = QWidget()
        layoutFormTransmitter2.addWidget(thirdSubTitle3Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 2)
        layoutFormTransmitter2.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter2.setLayout(layoutFormTransmitter2)

        layoutFormTransmitter3 = QGridLayout()
        layoutWidgetTransmitter3 = QWidget()
        layoutFormTransmitter3.addWidget(thirdSubTitle4Value, 0, 0)
        # layoutFormTransmitter.addWidget(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 3)
        layoutFormTransmitter3.addWidget(QLabel('dB'), 0, 1)
        layoutWidgetTransmitter3.setLayout(layoutFormTransmitter3)

        form3 = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow(thirdSubTitle1, layoutWidgetTransmitter)
        formLayout.addRow(thirdSubTitle2, layoutWidgetTransmitter1)
        formLayout.addRow(thirdSubTitle3, layoutWidgetTransmitter2)
        formLayout.addRow(thirdSubTitle4, layoutWidgetTransmitter3)
        form3.setLayout(formLayout)
        layout1.addWidget(form3)


        tab1Information.setLayout(layout1)
        scroll = QScrollArea()
        scroll.setWidget(tab1Information)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        layoutTab.addWidget(scroll, 0,0)

        self.tab4.setLayout(layoutTab)

        buttonLayout = QHBoxLayout()
        calculLayout = QVBoxLayout()

        titleLM = QLabel("Uplink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLM.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLM.setStyleSheet("QLabel{color:green;}")

        titleLD = QLabel("Downlink")
        font = QFont(const.font, const.fontSizeText, QFont.Medium)
        titleLD.setFont(QFont(const.font, const.fontSizeText, QFont.Bold))
        titleLD.setStyleSheet("QLabel{color:green;}")

        self.pireD_ModelInh = QLabel('EIRP [dBm]')
        self.pireD_ModelInh.setFont(font)
        self.pireD_ModelInhValue = QLineEdit(self)
        self.pireD_ModelInhValue.setValidator(QDoubleValidator())
        self.pireD_ModelInhValue.setStyleSheet("QLineEdit{color:green;}")
        self.pireD_ModelInhValue.setDisabled(True)
        self.pireD_ModelInhValue.setFont(font)
        
        self.margeD_ModelInh = QLabel('Total Margin [dB]')
        self.margeD_ModelInh.setFont(font)
        self.margeD_ModelInhValue = QLineEdit(self)
        self.margeD_ModelInhValue.setStyleSheet("QLineEdit{color:green;}")
        self.margeD_ModelInhValue.setDisabled(True)
        self.margeD_ModelInhValue.setValidator(QDoubleValidator())
        self.margeD_ModelInhValue.setFont(font)


        previousBtn = QPushButton('Previous', self)
        previousBtn.setFont(QFont(const.font, const.fontSizeText,))
        previousBtn.clicked.connect(self.previousBtn)

        suivantBtn = QPushButton('Next', self)
        suivantBtn.setFont(QFont(const.font, const.fontSizeText,))
        suivantBtn.clicked.connect(self.suivantBtn)

        buttonLayout.addWidget(previousBtn)
        buttonLayout.addStretch()
        buttonLayout.addWidget(suivantBtn)
        
        buttons = QWidget()
        buttons.setLayout(buttonLayout)
        layoutTab.addWidget(buttons, 1,0)

    def previousBtn(self):
        self.close()
        self.linkScreen.show()
        # self.
        # self.window = ChooseLiaisonScreen()
        # self.window.show()

    def onglet_change(self):
        self.tabsIndex = self.tabs.currentIndex()
        if self.tabs.currentIndex() == 0:
            self.model = 'Okumura Hata 5G Model'
            self.puissance_transmission = 23
            self.gain_antenne_transition = 0
            self.sinr = -4.13
            self.density_bruit = -174
            self.puissance_bruit = -110.66
            self.facteur_bruit = 2
            self.gain_antenne_reception = 17
            self.perte_cable = 0.5
            self.sensibility = -129.29
            self.interference = 3
            self.effet_masque = 7.68
            self.corps_humain = 1
            self.penetration_interrieur_batiment = 15
            self.showEltModelOkumura()
            self.repaint()
            self.update()
        elif self.tabs.currentIndex() == 1:
            self.corps_humain = 5
            self.model = 'Modèle UMa 5G'
            # self.tab2.setLayout(self.layoutTab)
            self.puissance_transmission = 23
            self.gain_antenne_transition = 0
            self.density_bruit = -174
            self.interference = 3
            self.effet_masque = 8.96
            self.corps_humain = 1
            self.penetration_interrieur_batiment = 25
            self.sinr = -4.48
            self.puissance_bruit = -103.97 
            self.facteur_bruit = 3
            self.perte_cable = 0
            self.sensibility = -130.50
            self.nbreEltAntenne = 192
            self.nbreTXRU = 64
            self.nbrePortAntenne = 2
            self.gainReseauAntenne = 25.05
            self.gainSousReseauAntenne = 10
            self.showEltModelUMA()
            self.repaint()
            self.update()
        elif self.tabs.currentIndex() == 2:
            self.model = 'UMi 5G Model'
            # self.tab2.setLayout(self.layoutTab)
            self.puissance_transmission = 23
            self.gain_antenne_transition = 0
            self.density_bruit = -174
            self.interference = 3
            self.effet_masque = 8.96
            self.corps_humain = 1
            self.penetration_interrieur_batiment = 25
            self.sinr = -4.48
            self.puissance_bruit = -103.97 
            self.facteur_bruit = 3
            self.perte_cable = 0
            self.sensibility = -130.50
            self.nbreEltAntenne = 192
            self.nbreTXRU = 64
            self.nbrePortAntenne = 2
            self.gainReseauAntenne = 25.05
            self.gainSousReseauAntenne = 10
            self.showEltModelUMI()
            self.repaint()
            self.update()
        elif self.tabs.currentIndex() == 3:
            self.model = 'InH 5G Model'
            # self.tab2.setLayout(self.layoutTab)
            self.puissance_transmission = 23
            self.gain_antenne_transition = 0
            self.density_bruit = -174
            self.interference = 3
            self.effet_masque = 8.96
            self.corps_humain = 1
            self.penetration_interrieur_batiment = 25
            self.sinr = -4.48
            self.puissance_bruit = -103.97 
            self.facteur_bruit = 3
            self.perte_cable = 0
            self.sensibility = -130.50
            self.nbreEltAntenne = 192
            self.nbreTXRU = 64
            self.nbrePortAntenne = 2
            self.gainReseauAntenne = 25.05
            self.gainSousReseauAntenne = 10
            self.showEltModelINH()
            self.repaint()
            self.update()

    def calculModelOkumuraBtn(self):
        self.pireMValueCalcul = self.puissance_transmission + self.gain_antenne_transition
        self.totalMargeMValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment

        self.pireDValueCalcul = self.puissance_transmission + self.gain_antenne_transition
        self.totalMargeDValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment

        self.margeM_ModelOkumuraValue.setText(str(self.totalMargeMValueCalcul))
        self.pireM_ModelOkumuraValue.setText(str(self.pireMValueCalcul))

        self.margeD_ModelOkumuraValue.setText(str(self.totalMargeDValueCalcul))
        self.pireD_ModelOkumuraValue.setText(str(self.pireDValueCalcul))

    def calculModelUmaBtn(self):
        self.pireDValueCalcul = self.puissance_transmission + (10 * math.log10(self.nbreTXRU)) + self.gainReseauAntenne
        self.totalMargeDValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment
       
        self.pireMValueCalcul = self.puissance_transmission + self.gain_antenne_transition
        self.totalMargeMValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment 
 
        self.margeM_ModelUmaValue.setText(str(self.totalMargeMValueCalcul))
        self.pireM_ModelUmaValue.setText(str(self.pireMValueCalcul))

        self.margeD_ModelUmaValue.setText(str(self.totalMargeDValueCalcul))
        self.pireD_ModelUmaValue.setText(str(self.pireDValueCalcul))

    def calculModelUmiBtn(self):
        self.pireDValueCalcul = self.puissance_transmission + (10 * math.log10(self.nbreTXRU)) + self.gainReseauAntenne
        self.totalMargeDValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment
       
        self.pireMValueCalcul = self.puissance_transmission + self.gain_antenne_transition
        self.totalMargeMValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment 
 
        self.margeM_ModelUmiValue.setText(str(self.totalMargeMValueCalcul))
        self.pireM_ModelUmiValue.setText(str(self.pireMValueCalcul))

        self.margeD_ModelUmiValue.setText(str(self.totalMargeDValueCalcul))
        self.pireD_ModelUmiValue.setText(str(self.pireDValueCalcul))

    def calculModelInhBtn(self):
        self.pireDValueCalcul = self.puissance_transmission + (10 * math.log10(self.nbreTXRU)) + self.gainReseauAntenne
        self.totalMargeDValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment
       
        self.pireMValueCalcul = self.puissance_transmission + self.gain_antenne_transition
        self.totalMargeMValueCalcul = self.interference + self.effet_masque + self.corps_humain + self.penetration_interrieur_batiment 
 
        self.margeM_ModelInhValue.setText(str(self.totalMargeMValueCalcul))
        self.pireM_ModelInhValue.setText(str(self.pireMValueCalcul))

        self.margeD_ModelInhValue.setText(str(self.totalMargeDValueCalcul))
        self.pireD_ModelInhValue.setText(str(self.pireDValueCalcul))

    def suivantBtn(self):
        self.window = ResultBilanLiaisonUpScreen(linkScreen=self,model= self.model, pireMValueCalcul=self.pireMValueCalcul,totalMargeMValueCalcul=self.totalMargeMValueCalcul, pireDValueCalcul=self.pireDValueCalcul,totalMargeDValueCalcul=self.totalMargeDValueCalcul)
        self.window.show()

    def resetBtn(self):
        self.secondSubTitle7Value.setText('')
        self.secondSubTitle6Value.setText('')
        self.secondSubTitle5Value.setText('')
        self.secondSubTitle4Value.setText('')
        self.secondSubTitle3Value.setText('')
        self.secondSubTitle2Value.setText('')
        self.firstSubTitle3Value.setText('')
        self.firstSubTitle2Value.setText('')
        self.firstSubTitle1Value.setText('')

#auto-py-to-exe