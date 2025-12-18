import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Import de la classe Okumura-Hata
from calcul_perte_maximal_okumura import CalculPerteMaximaleModelOkumura


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre bilan factice (nécessaire pour le bouton Previous)
    bilan_window = QWidget()
    bilan_window.setWindowTitle("Bilan (Fake)")
    bilan_window.resize(400, 300)

    # Valeurs initiales exigées par le constructeur
    pireDValueCalcul = 0
    totalMargeDValueCalcul = 0
    pireMValueCalcul = 0
    totalMargeMValueCalcul = 0

    # Lancement du modèle Okumura-Hata
    okumura_window = CalculPerteMaximaleModelOkumura(
        bilan_window,
        pireDValueCalcul,
        totalMargeDValueCalcul,
        pireMValueCalcul,
        totalMargeMValueCalcul,
    )

    okumura_window.show()
    sys.exit(app.exec_())
