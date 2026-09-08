import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Başlık")
    win.setGeometry(1500,500,1000,1000)

    win.show()
    sys.exit(app.exec())

main()