import sys
import os
from PyQt5.QtGui import QPixmap, QFont, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp, QSize
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton,
    QSpacerItem, QSizePolicy, QDialog
)

from bilan_liaison_montante import BilanLiaisonMontante
import constant as const

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
        
        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(main_layout)
        self.resize(500, 415)
        
        # Add logo/image
        self.logo_label = QLabel(self)
        pixmap = QPixmap(self.resource_path('./images/icon.png'))
        if pixmap.isNull():
            print("Warning: Could not load icon.png")
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.logo_label)

        # Title
        self.title = QLabel(
            "Test bench Propagation attenuation simulation tool on mobility "
            "(coverage and capacity) for the 5G network"
        )
        title_font = QFont(const.font, const.fontSizeTitle, QFont.Bold)
        self.title.setFont(title_font)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        main_layout.addWidget(self.title)
        
        # Add spacer
        main_layout.addSpacing(20)

        # Login form
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Admin"])
        
        self.passwordValue = QLineEdit()
        self.passwordValue.setEchoMode(QLineEdit.Password)
        
        form_layout = QFormLayout()
        form_layout.addRow("Login:", self.pageCombo)
        form_layout.addRow("Password:", self.passwordValue)
        
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(30)

        # Buttons
        button_layout = QHBoxLayout()
        
        close_btn = QPushButton("Close")
        close_btn.setMinimumWidth(150)
        close_btn.clicked.connect(self.close)
        
        login_btn = QPushButton("Login")
        login_btn.setMinimumWidth(150)
        login_btn.clicked.connect(self.validateBtn)
        
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        button_layout.addSpacing(20)
        button_layout.addWidget(login_btn)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Warning")
        dialog.resize(300, 100)
        
        layout = QVBoxLayout()
        message = QLabel("Please enter the correct login credentials.")
        message.setAlignment(Qt.AlignCenter)
        
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(dialog.accept)
        
        layout.addWidget(message)
        layout.addWidget(ok_btn)
        dialog.setLayout(layout)
        
        dialog.exec_()

    def validateBtn(self):
        username = self.pageCombo.currentText()
        password = self.passwordValue.text()
        
        print(f"Login attempt: Username={username}, Password={'*' * len(password)}")
        
        if username == "Admin" and password == "Azerty@12":
            print("Login successful!")
            
            # Show success message
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(
                self, 
                "Success", 
                "Login successful!\n\nNext step: Connect to bilan_liaison_montante window."
            )
            
            # For now, we'll keep it simple and not open the next window
            # We'll fix the linkScreen issue separately
        else:
            self.show_dialog()
    
    def validatePassword(self):
        # This method is defined but not called in the current code
        # Keep it for future use if needed
        reg_ex = QRegExp(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$&*~]).{8,}$")
        validator = QRegExpValidator(reg_ex, self.passwordValue)
        self.passwordValue.setValidator(validator)