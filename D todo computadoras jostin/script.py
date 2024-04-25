import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget

class MultiWindowsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ventana')
        self.setGeometry(100, 100, 400, 300)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Definir la cantidad de ventanas que quieres abrir
    num_windows = 3

    for i in range(num_windows):
        if i == 0:
            subprocess.Popen('cmd', shell=True)
        elif i == 1:
            subprocess.Popen('notepad', shell=True)
        elif i == 2:
            subprocess.Popen('start chrome', shell=True)

        window = MultiWindowsApp()
        window.move(100 + i*50, 100 + i*50)

    sys.exit(app.exec_())