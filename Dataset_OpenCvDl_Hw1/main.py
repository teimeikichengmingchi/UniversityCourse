from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ImageProcessing
import VGG16


def main():
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui1 = ImageProcessing.Window()
    ui1.setupUi(MainWindow)
    MainWindow.show()

    SubWindow = QMainWindow()
    ui2 = VGG16.Window()
    ui2.setupUi(SubWindow)
    SubWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
