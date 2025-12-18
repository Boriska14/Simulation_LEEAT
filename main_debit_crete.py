import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Import de la classe Peak Data Rate
from calcul_debit_crete import CalculDebitCrete


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (utilisée par le bouton Previous)
    bilan_window = QWidget()
    bilan_window.setWindowTitle("Bilan (Fake)")
    bilan_window.resize(400, 300)

    # Lancement de la fenêtre Calcul Débit Crête
    debit_crete_window = CalculDebitCrete(
        bilan_window
    )

    debit_crete_window.show()
    sys.exit(app.exec_())
