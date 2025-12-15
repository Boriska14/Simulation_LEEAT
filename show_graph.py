# show_graph.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ShowGraph(QWidget):
    def __init__(self, title="", x_label="", y_label="", x_data=None, y_data=None, graphType='line'):
        super().__init__()
        self.setWindowTitle(title)

        x_data = x_data or []
        y_data = y_data or []

        self.figure = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        if graphType == 'scatter':
            self.ax.scatter(x_data, y_data)
        else:
            self.ax.plot(x_data, y_data)

        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_title(title)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
