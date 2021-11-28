# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VGG16.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import cv2
import numpy as np
import keras


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 58, 15))
        self.label.setObjectName("label")
        self.But1 = QtWidgets.QPushButton(self.centralwidget)
        self.But1.setGeometry(QtCore.QRect(70, 60, 200, 40))
        self.But1.setObjectName("But1")
        self.But2 = QtWidgets.QPushButton(self.centralwidget)
        self.But2.setGeometry(QtCore.QRect(70, 120, 200, 40))
        self.But2.setObjectName("But2")
        self.But3 = QtWidgets.QPushButton(self.centralwidget)
        self.But3.setGeometry(QtCore.QRect(70, 180, 200, 40))
        self.But3.setObjectName("But3")
        self.But4 = QtWidgets.QPushButton(self.centralwidget)
        self.But4.setGeometry(QtCore.QRect(70, 240, 200, 40))
        self.But4.setObjectName("But4")
        self.But5 = QtWidgets.QPushButton(self.centralwidget)
        self.But5.setGeometry(QtCore.QRect(70, 340, 200, 40))
        self.But5.setObjectName("But5")
        self.InputData = QtWidgets.QLineEdit(self.centralwidget)
        self.InputData.setGeometry(QtCore.QRect(70, 300, 200, 22))
        self.InputData.setObjectName("InputData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.But1.clicked.connect(self.ShowImg)
        self.But2.clicked.connect(self.ShowPara)
        self.But3.clicked.connect(self.ShowModel)
        self.But4.clicked.connect(self.ShowAcc)
        self.But5.clicked.connect(self.Test)

    def Test(self):
        try:
            case = int(self.InputData.text())
            case -= 1
            if case > 59999 or case < 0:
                print("Valid range is between 1 ~ 60000")
            else:
                temp = self.test_x[case].reshape((1, 32, 32, 3))
                result = self.model.predict(temp)
                plt.figure(figsize = (10, 10))
                plt.bar(self.namelist, result.reshape(10))
                plt.show()
                plt.figure(figsize = (6, 6))
                plt.imshow(self.test_x[case])
                plt.show()
        except:
            print("Not a valid number!")

    def ShowAcc(self):
        acc = cv2.imread("Q5_Image/model4_2.png")
        loss = cv2.imread("Q5_Image/model4_1.png")
        cv2.imshow("Accuracy", acc)
        cv2.imshow("Loss", loss)

    def ShowModel(self):
        import keras
        self.model = keras.models.load_model("model4.h5")
        print(self.model.summary())

    def ShowPara(self):
        print("hyperparameters:")
        print("\tbatch size: ", 512)
        print("\toptimizer: ", "adam")
        print("\tlearning rate: ", "0.01")

    def ShowImg(self):
        from keras.datasets import cifar10  
        import ssl
        import random
        ssl._create_default_https_context = ssl._create_unverified_context 
        (train_x, train_y), (self.test_x, self.test_y) = cifar10.load_data() 
        self.namelist = ["airplane", "automobile", "bird", "cat", "deer",
                            "dog", "frag", "horse", "ship", "truck"]
        self.test_x = np.append(self.test_x, train_x)
        self.test_y = np.append(self.test_y, train_y)
        self.test_x = self.test_x.reshape((60000, 32, 32, 3))
        self.test_y = self.test_y.reshape(60000)

        self.test_x = self.test_x.astype('float32')
        #self.test_x /= 255
        for i in range(60000):
            self.test_x[i, :, :, 0] = (self.test_x[i, :, :, 0] - self.test_x[i, :, :, 0].mean()) / self.test_x[i, :, :, 0].std()
            self.test_x[i, :, :, 1] = (self.test_x[i, :, :, 1] - self.test_x[i, :, :, 1].mean()) / self.test_x[i, :, :, 1].std()
            self.test_x[i, :, :, 2] = (self.test_x[i, :, :, 2] - self.test_x[i, :, :, 2].mean()) / self.test_x[i, :, :, 2].std()
            self.test_x[i, :, :, 0] = (self.test_x[i, :, :, 0] - self.test_x[i, :, :, 0].min()) / (self.test_x[i, :, :, 0].max() - self.test_x[i, :, :, 0].min())
            self.test_x[i, :, :, 1] = (self.test_x[i, :, :, 1] - self.test_x[i, :, :, 1].min()) / (self.test_x[i, :, :, 1].max() - self.test_x[i, :, :, 1].min())
            self.test_x[i, :, :, 2] = (self.test_x[i, :, :, 2] - self.test_x[i, :, :, 2].min()) / (self.test_x[i, :, :, 2].max() - self.test_x[i, :, :, 2].min())
        self.test_y = keras.utils.np_utils.to_categorical(self.test_y, 10)
        for i in range(9):
            myrand = random.randint(0, self.test_x.shape[0] - 1)
            plt.subplot(3, 3, i + 1)
            plt.axis("off")
            plt.title(self.namelist[np.where(self.test_y[myrand] == self.test_y[myrand].max())[0][0]])
            plt.imshow(self.test_x[myrand])
        plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VGG16"))
        self.label.setText(_translate("MainWindow", "VGG16"))
        self.But1.setText(_translate("MainWindow", "1. Show Train Image"))
        self.But2.setText(_translate("MainWindow", "2. Show HyperParameter"))
        self.But3.setText(_translate("MainWindow", "3. Show Model Shortcut"))
        self.But4.setText(_translate("MainWindow", "4. Show Accuracy"))
        self.But5.setText(_translate("MainWindow", "5. Test"))


if __name__ == "__main__":
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    """
    import seaborn as sns
    #sns.histplot(data=np.float32([1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]))
    namelist = ["airplane", "automobile", "bird", "cat", "deer",
                            "dog", "frag", "horse", "ship", "truck"]
    plt.bar(namelist, np.float32([1, 0, 1, 0, 0, 1, 0, 1, 0, 1]))
    plt.show()