import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Import de ta classe
from calcul_perte_maximal_umi import CalculPerteMaximaleModelUmi


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (requise par le constructeur)
    bilan_window = QWidget()
    bilan_window.setWindowTitle("Bilan (Fake)")
    bilan_window.resize(400, 300)

    # Valeurs initiales requises par le constructeur
    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    # Création de la fenêtre UMI
    umi_window = CalculPerteMaximaleModelUmi(
        bilan_window,
        pireDValueCalcul,
        totalMargeDValueCalcul,
        pireMValueCalcul,
        totalMargeMValueCalcul,
    )

    umi_window.show()
    sys.exit(app.exec_())
