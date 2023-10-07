import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
import matplotlib.pyplot as plt
import numpy as np

class InteractiveVectorPlot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = FigureCanvas(plt.figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.canvas.mpl_connect('button_press_event', self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1)
        self.canvas.draw()

    def on_click(self, event):
        if event.inaxes is not self.ax:
            return
        self.ax.quiver(0, 0, event.xdata, event.ydata, angles='xy', scale_units='xy', scale=1)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = InteractiveVectorPlot()
    main_window.show()
    sys.exit(app.exec_())
