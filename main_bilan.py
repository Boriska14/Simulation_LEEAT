import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Try to import all required modules
try:
    from calcul_debit_physique import CalculDebitPhysique
    CALCUL_DEBIT_AVAILABLE = True
except ImportError:
    print("Warning: calcul_debit_physique.py not found")
    CALCUL_DEBIT_AVAILABLE = False

try:
    from bilan_liaison_montante import BilanLiaisonMontante
    BILAN_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Cannot import BilanLiaisonMontante: {e}")
    BILAN_AVAILABLE = False

# Check for constant.py
try:
    import constant as const
    CONSTANT_AVAILABLE = True
except ImportError:
    print("Warning: constant.py not found")
    # Create minimal constants
    const = type('const', (), {})()
    const.font = "Arial"
    const.fontSizeText = 10
    const.fontSizeTitle = 14
    const.fontSizeText = 10  # For form text
    CONSTANT_AVAILABLE = False

class ApplicationController:
    """Manages navigation between application windows"""
    def __init__(self):
        self.debit_physique_window = None
        self.bilan_window = None
        
        # Initialize debit_physique_window first
        self.init_debit_physique()
        
    def init_debit_physique(self):
        """Initialize the Physical Data Rate window"""
        if CALCUL_DEBIT_AVAILABLE:
            # Create a fake window for the "previous" functionality
            fake_bilan = QWidget()
            fake_bilan.setWindowTitle("Bilan (Previous)")
            fake_bilan.resize(400, 300)
            
            self.debit_physique_window = CalculDebitPhysique(fake_bilan)
        else:
            print("CalculDebitPhysique not available")
            self.debit_physique_window = None
    
    def show_debit_physique(self):
        """Show the Physical Data Rate window"""
        if self.debit_physique_window:
            # Hide bilan window if it exists
            if self.bilan_window:
                self.bilan_window.hide()
            self.debit_physique_window.show()
        else:
            QMessageBox.warning(None, "Error", "Physical Data Rate window not available")
    
    def show_bilan_liaison(self, sens="uplink"):
        """Show the Link Report window"""
        if not BILAN_AVAILABLE:
            QMessageBox.warning(
                None, 
                "Error", 
                "BilanLiaisonMontante module not available.\n"
                "Please check bilan_liaison_montante.py exists."
            )
            return
        
        # Hide debit_physique window if it exists
        if self.debit_physique_window:
            self.debit_physique_window.hide()
        
        # Create and show the bilan window
        self.bilan_window = BilanLiaisonMontante(
            linkScreen=self.debit_physique_window,
            sens=sens
        )
        self.bilan_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create application controller
    controller = ApplicationController()
    
    # Start with BilanLiaisonMontante if available
    if BILAN_AVAILABLE:
        controller.show_bilan_liaison(sens="uplink")
    elif CALCUL_DEBIT_AVAILABLE:
        controller.show_debit_physique()
    else:
        QMessageBox.critical(
            None, 
            "Fatal Error", 
            "No application modules found.\n"
            "Please ensure at least one of these files exists:\n"
            "- calcul_debit_physique.py\n"
            "- bilan_liaison_montante.py"
        )
        sys.exit(1)
    
    sys.exit(app.exec_())