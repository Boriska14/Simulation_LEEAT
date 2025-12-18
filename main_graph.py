# main_graph.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from show_graph import ShowGraph

class GraphDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Demo Application")
        self.resize(800, 600)
        
        self.layout = QVBoxLayout()
        
        # Boutons pour différents types de graphiques
        button_layout = QHBoxLayout()
        
        self.line_btn = QPushButton("Graphique Ligne")
        self.line_btn.clicked.connect(self.show_line_graph)
        
        self.scatter_btn = QPushButton("Graphique Points")
        self.scatter_btn.clicked.connect(self.show_scatter_graph)
        
        self.close_btn = QPushButton("Fermer")
        self.close_btn.clicked.connect(self.close_all_graphs)
        
        button_layout.addWidget(self.line_btn)
        button_layout.addWidget(self.scatter_btn)
        button_layout.addWidget(self.close_btn)
        
        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)
        
        # Liste pour garder les références aux fenêtres de graphiques
        self.graph_windows = []
    
    def generate_sample_data(self, n_points=20):
        """Génère des données de test"""
        x_data = list(range(n_points))
        y_data = [random.randint(0, 100) for _ in range(n_points)]
        return x_data, y_data
    
    def show_line_graph(self):
        """Affiche un graphique en ligne"""
        x_data, y_data = self.generate_sample_data()
        
        graph = ShowGraph(
            title="Performance du Signal 5G (Ligne)",
            x_label="Temps (ms)",
            y_label="Puissance (dBm)",
            x_data=x_data,
            y_data=y_data,
            graphType='line'
        )
        
        graph.resize(600, 400)
        graph.show()
        self.graph_windows.append(graph)
    
    def show_scatter_graph(self):
        """Affiche un graphique en nuage de points"""
        x_data, y_data = self.generate_sample_data(15)
        
        graph = ShowGraph(
            title="Distribution des Stations de Base (Points)",
            x_label="Position X (km)",
            y_label="Position Y (km)",
            x_data=x_data,
            y_data=y_data,
            graphType='scatter'
        )
        
        graph.resize(600, 400)
        graph.show()
        self.graph_windows.append(graph)
    
    def close_all_graphs(self):
        """Ferme toutes les fenêtres de graphiques"""
        for window in self.graph_windows:
            window.close()
        self.graph_windows.clear()

def main():
    """Fonction principale"""
    app = QApplication(sys.argv)
    
    # Vérifier que matplotlib est installé
    try:
        import matplotlib
        print(f"✓ matplotlib version: {matplotlib.__version__}")
    except ImportError:
        print("✗ matplotlib n'est pas installé")
        print("Installez-le avec: pip install matplotlib")
        return
    
    # Créer et afficher la fenêtre de démonstration
    demo = GraphDemo()
    demo.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()