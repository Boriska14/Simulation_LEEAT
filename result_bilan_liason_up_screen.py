import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import constant as const

class ResultBilanLiaisonUpScreen(QWidget):
    def __init__(self, linkScreen=None, model="", pireMValueCalcul=0, totalMargeMValueCalcul=0, 
                 pireDValueCalcul=0, totalMargeDValueCalcul=0):
        super().__init__()
        self.linkScreen = linkScreen
        self.model = model
        self.pireMValueCalcul = pireMValueCalcul
        self.totalMargeMValueCalcul = totalMargeMValueCalcul
        self.pireDValueCalcul = pireDValueCalcul
        self.totalMargeDValueCalcul = totalMargeDValueCalcul
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculation Results")
        self.resize(600, 500)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel(f"Results - {self.model}")
        title_font = QFont(const.font, const.fontSizeTitle, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Results display
        results_text = f"""
        <h3>Uplink Results:</h3>
        <b>EIRP:</b> {self.pireMValueCalcul} dBm<br>
        <b>Total Margin:</b> {self.totalMargeMValueCalcul} dB<br><br>
        
        <h3>Downlink Results:</h3>
        <b>EIRP:</b> {self.pireDValueCalcul} dBm<br>
        <b>Total Margin:</b> {self.totalMargeDValueCalcul} dB
        """
        
        results_label = QLabel(results_text)
        results_label.setAlignment(Qt.AlignLeft)
        results_label.setWordWrap(True)
        
        # Scroll area for results
        scroll = QScrollArea()
        scroll.setWidget(results_label)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        
        # Navigation buttons
        button_layout = QVBoxLayout()
        
        previous_btn = QPushButton("Previous")
        previous_btn.setFont(QFont(const.font, const.fontSizeText))
        previous_btn.clicked.connect(self.previousBtn)
        
        close_btn = QPushButton("Close")
        close_btn.setFont(QFont(const.font, const.fontSizeText))
        close_btn.clicked.connect(self.closeBtn)
        
        button_layout.addWidget(previous_btn)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def previousBtn(self):
        """Return to the previous screen"""
        if self.linkScreen:
            self.linkScreen.show()
        self.close()
    
    def closeBtn(self):
        """Close the application"""
        self.close()