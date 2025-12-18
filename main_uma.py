import sys
from PyQt5.QtWidgets import QApplication, QWidget

# IMPORT CORRECT (nom du fichier + nom de la classe)
from calcul_perte_maximal_uma import CalculPerteMaximaleModelUma


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (obligatoire pour ton constructeur)
    fake_bilan = QWidget()
    fake_bilan.setWindowTitle("Bilan (fake)")

    # Valeurs par défaut pour les paramètres
    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    # Lancement de la fenêtre UMA
    window = CalculPerteMaximaleModelUma(
        fake_bilan,
        pireDValueCalcul,
        totalMargeDValueCalcul,
        pireMValueCalcul,
        totalMargeMValueCalcul,
    )

    window.show()
    sys.exit(app.exec_())
