import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from caller_UI import Ui_SIMCaller

# class SIMCaller(Ui_SIMCaller):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         print('Simcaller loaded step2')
#
#     def initUI(self):
#
#         self.tb = QTextBrowser()
#         self.tb.setAcceptRichText(True)
#         self.tb.setOpenExternalLinks(True)
#
#         self.FindPortButtMod_1.clicked.connect(print('pohj.mfjfgjf'))
#
#     def bp(self):
#         print('Ghbdsn ')
#         # textBrowserMod_1


class Modem:
    def __init__(self):
        pass


class ATcommands:
    pass


class Connector:
    def find_ports(self):
        pass


# if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SIMCaller = QtWidgets.QMainWindow()
    ui = Ui_SIMCaller()
    ui.setupUi(SIMCaller)
    SIMCaller.show()

#-----------------------------------------------------------------------------


    # ui.FindPortButtMod_1.clicked.connect(bp)
    # ui.FindPortButtMod_2.clicked.connect(bp)





#-----------------------------------------------------------------------------

    sys.exit(app.exec_())
