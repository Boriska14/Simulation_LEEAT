# main_login.py
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    try:
        from login import Login
        
        # Check if constant.py exists
        try:
            import constant
            print("✓ constant.py loaded")
        except ImportError:
            print("⚠ constant.py not found. Creating default constants.")
            # Create a minimal constant module
            import sys
            constant = type('constant', (), {})()
            constant.font = "Arial"
            constant.fontSizeText = 10
            constant.fontSizeTitle = 14
            sys.modules['constant'] = constant
        
        # Create and show the login window
        window = Login()
        window.show()
        
        sys.exit(app.exec_())
        
    except ImportError as e:
        print(f"✗ Import Error: {e}")
        print("\nPlease ensure these files exist:")
        print("1. login.py - The login window")
        print("2. constant.py - With font constants")
        input("Press Enter to exit...")