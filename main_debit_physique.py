import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Import de la classe Physical Data Rate
from calcul_debit_physique import CalculDebitPhysique


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (utilisée par le bouton Previous)
    bilan_window = QWidget()
    bilan_window.setWindowTitle("Bilan (Fake)")
    bilan_window.resize(400, 300)

    # Lancement de la fenêtre Calcul Debit Physique
    debit_physique_window = CalculDebitPhysique(
        bilan_window
    )

    debit_physique_window.show()
    sys.exit(app.exec_())
