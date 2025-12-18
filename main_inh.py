import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Import de la classe INH
from calcul_perte_maximal_inh import CalculPerteMaximaleModelInh


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (obligatoire pour Previous)
    bilan_window = QWidget()
    bilan_window.setWindowTitle("Bilan (Fake)")
    bilan_window.resize(400, 300)

    # Valeurs initiales exigées par le constructeur
    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    # Lancement de la fenêtre INH
    inh_window = CalculPerteMaximaleModelInh(
        bilan_window,
        pireDValueCalcul,
        totalMargeDValueCalcul,
        pireMValueCalcul,
        totalMargeMValueCalcul,
    )

    inh_window.show()
    sys.exit(app.exec_())
