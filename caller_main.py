# Імпортуємо наш графічний інтерфейс з файлу
from caller_UI import Ui_SIMCaller
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo



class SIMCaller(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_SIMCaller()
        self.ui.setupUi(self)
        # Описуємо реакції на натискання кнопок
        self.ui.FindPortButtMod_1.clicked.connect(self.FindPort)
        self.ui.ConnButtMod_1.clicked.connect(self.Connect)
        self.ui.DisconnButtMod_1.clicked.connect(self.Disconnect)
        self.ui.FindPortButtMod_2.clicked.connect(self.FindPort)
        self.ui.ConnButtMod_2.clicked.connect(self.Connect)
        self.ui.DisconnButtMod_2.clicked.connect(self.Disconnect)

    def FindPort(self):
        print("Find ports button click")
        text = "Find ports button click"
        self.ui.textBrowserMod_1.append(text)

    def Connect(self):
        print("ConnButtMod_1.clicked")
        text = "ConnButtMod_1.clicked"
        self.ui.textBrowserMod_1.append(text)

    def Disconnect(self):
        print("DisconnButtMod_1.clicked")
        text = "DisconnButtMod_1.clicked"
        self.ui.textBrowserMod_1.append(text)




    # def bp(self):
    #     print('Ghbdsn ')
    #     # textBrowserMod_1


class Modem:
    def __init__(self):
        pass

class ATcommands:
    pass


class Connector:
    def find_ports(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = SIMCaller()
    myapp.show()
    sys.exit(app.exec_())
#-----------------------------------------------------------------------------

    # class SIMCaller(Ui_SIMCaller):
# -----------
# if __name__ == "__main__":
    #     app = QtWidgets.QApplication(sys.argv)
    #     SIMCaller = QtWidgets.QMainWindow()
    #     ui = Ui_SIMCaller()
    #     ui.setupUi(SIMCaller)
    #     SIMCaller.show()
    #     sys.exit(app.exec_())
#-----------------------------------------------------------------------------


