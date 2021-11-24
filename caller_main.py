# Імпортуємо наш графічний інтерфейс з файлу
from caller_UI import Ui_SIMCaller
# import os
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice



class SIMCaller(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.serial = QSerialPort()
        self.ui = Ui_SIMCaller()
        self.ui.setupUi(self)

# Описуємо реакції на натискання кнопок
        # та вибір чекбоксів та комбобоксів модема 1:
        self.ui.FindPortButtMod_1.clicked.connect(self.findPort)
        self.ui.ConnButtMod_1.clicked.connect(self.connect)
        self.ui.boudrateComboBoxMod_1.currentTextChanged.connect\
            (self.IChangeCB)
        self.ui.DisconnButtMod_1.clicked.connect(self.disconnect)
        # self.ui.portComboBoxMod_1.currentIndexChanged.connect(self.test)
        # self.ui.ActivationCBMod_1.stateChanged.connect(self.IChangeCB)
        # self.ui.CallingCBMod_1.stateChanged.connect(ledControl)
        # self.ui.ProvComboBoxMod_1
        # self.ui.CallTimeSBMod_1

# Описуємо реакції на натискання кнопок
        # та вибір чекбоксів та комбобоксів модема 2:

        self.ui.FindPortButtMod_2.clicked.connect(self.findPort)
        self.ui.ConnButtMod_2.clicked.connect(self.connect)
        self.ui.DisconnButtMod_2.clicked.connect(self.disconnect)

        # Під'єднання до функцій натискання кнопок глобального керування
        # всіма модемами
        self.ui.StartAllButt.clicked.connect(self.startall)
        self.ui.StopAllButt.clicked.connect(self.stopall)
        self.ui.ResetAllButt.clicked.connect(self.resetall)

    def findPort(self):
        """
        What to do: Finding free serial ports
        :return: displays available ports in combobox
        """
        #очищаємо ComboBox від попереднього списку портів
        self.ui.portComboBoxMod_1.clear()
        # створюємо список всіх доступних портів у системі
        portlist = []
        descrportlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
            descrportlist.append(port.description())
        # розміщуємо список знайдених компортів до ComboBox
        fullnameport = list(zip(portlist, descrportlist))
        self.ui.portComboBoxMod_1.addItems(portlist)
        # self.ui.textBrowserMod_1.append(f'Знайдено порти{fullnameport}')
        self.ui.textBrowserMod_1.append(f"<font color = Green>Знайдено порти:"
                                        f" {fullnameport}</font>")

    def connect(self):
        # Open the serial port
        self.serial.setPortName(self.ui.portComboBoxMod_1.currentText())
        self.serial.setBaudRate(
            int(self.ui.boudrateComboBoxMod_1.currentText()))
        if not self.serial.isOpen():
            self.serial.open(QIODevice.ReadWrite)
            self.ui.textBrowserMod_1.append\
                (f"<font color = Green>Порт "
                 f"{self.ui.portComboBoxMod_1.currentText()}"
                 f" відкрито на швидкості"
                 f" {int(self.ui.boudrateComboBoxMod_1.currentText())}</font>")
            time.sleep(2)
            # test commands
            cmds = [
                b'ATE0\n',  # Turn command echo on (ATE1) or off (ATE0)
                b'AT\n', # test if basic function is working
                b'AT+GMI\n', # Request Manufacturer Identification
                b'AT+GMM\n', # Request TA Model Identification
                b'AT+GMR\n', # Request TA Revision Identification of Software Release
                b'AT+GSN\n', # Request TA Serial Number Identification(IMEI)
                b'AT\n',  # test if basic function is workinG
                # b'ATD 0665791106;\r\n' # ring to number
            ]
            for cmd in cmds:
                try:
                    self.serial.write(cmd)
                    self.ui.textBrowserMod_1.append \
                        (f"<font color = Black>{cmd}</font>")
                    time.sleep(2)
                    try:
                        if self.serial.isOpen():
                            if self.serial.waitForReadyRead():
                                while self.serial.canReadLine():
                                    txt = self.serial.readLine()
                                    # txt = self.serial.readAll()
                                    print(txt)
                                    self.ui.textBrowserMod_1.append(f"<font color = Blue>{txt}</font>")
                                    time.sleep(1)
                        else: print("Помилка! Не можу відкрити заданий порт.")
                    except:
                        print("Помилка прийому")
                except:
                    print("Помилка передачі")

    def readPort(self):
        while True:
            # rcv = self.serial.readline()  # receive data
            rcv = self.serial.readAll()
            print(rcv)
            return rcv
            # self.process_bytes(bytes(self.serial.readAll()))
        # rx = self.serial.readline()
        # # rxs = str(rx, 'UTF-8')
        # print(rx)
        #

    def writePort(self, cmd):
        # Write to serial port
        self.serial.write(cmd)

    def disconnect(self):
        # Close the serial port
        if self.serial.isOpen():
            self.serial.close()
            self.ui.textBrowserMod_1.append\
                (f"<font color = Green>Порт "
                 f"{self.ui.portComboBoxMod_1.currentText()} закрито</font>")
        else:
            print("Serial no open")

    def IChangeCB(self):
        print(f"<< Було змінено швидкість порту на "
              f"{self.ui.boudrateComboBoxMod_1.currentText()} >>")
        self.ui.textBrowserMod_1.append\
            (f"<< Було змінено швидкість порту на"
             f" {self.ui.boudrateComboBoxMod_1.currentText()} >>")

    def startall(self):
        pass

    def stopall(self):
        pass

    def resetall(self):
        pass


class Modem:
    def __init__(self, ):
        pass

class ATcommands:
    pass


class Connector(Modem):
    def find_ports(self):
        pass


#Main function that calls other functions - Makes script reusable
def main():
    app = QtWidgets.QApplication(sys.argv) # Створюємо новий екземпляр QApplication
    myapp = SIMCaller()  # Створюємо об'єкт класу SIMCaller
    myapp.show() # Показуємо вікно
    sys.exit(app.exec_()) # Коректне завершення процесів при закритті програми


if __name__ == "__main__": # Якщо ми запускаємо файл навпростець, а не імпортуємо
    main()                 # то запускаємо функцію main()




