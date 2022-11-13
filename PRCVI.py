from PyQt6 import QtCore, QtGui, QtWidgets
from FuncWindNew import Ui_FuncWind


class Ui_MainWindow(object):

    def openFuncWind(self, _configDB):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FuncWind()
        self.ui.setupUi(self.window, _configDB)
        self.ui.UpdateTables(self.CreateDBConnection(_configDB))
        self.window.show()

    def setupUi(self, MainWindow, _configDB):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 666)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("PT Sans Caption")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "    background-color: #4CAF50;\n"
                                 "    border: none;\n"
                                 "    color: #fff;\n"
                                 "    padding: 14px;\n"
                                 "    text-align: center;\n"
                                 "    text-decoration: none;\n"
                                 "    display: inline-block;\n"
                                 "    font-size: 12px;\n"
                                 "    margin: 4px 2px;\n"
                                 "    border-radius: 12px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #3e8e41\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget,
                                              clicked=lambda: MainWindow.close())
        self.OpenFile.setGeometry(QtCore.QRect(10, 30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.OpenFile.setFont(font)
        self.OpenFile.setObjectName("OpenFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(196, 22, 851, 611))
        self.label.setObjectName("label")
        self.AddNote = QtWidgets.QPushButton(self.centralwidget,
                                             clicked=lambda: self.openFuncWind(_configDB))
        self.AddNote.setGeometry(QtCore.QRect(10, 570, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.AddNote.setFont(font)
        self.AddNote.setObjectName("AddNote")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def CreateDBConnection(self, config):
        try:
            import psycopg2
            conn = psycopg2.connect(database=config["database"], user=config["user"],
                                    password=config["password"], host=config["host"], port=int(config["port"]))
            # connection.autocommit = True
            print("[INFO] Connection to the database was successful!")
            return conn
        except Exception as _ex:
            print(f"[INFO] Error while connection with PostgreSQL - {_ex}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр изображения"))
        self.OpenFile.setText(_translate("MainWindow", "Открыть файл"))
        self.label.setText(_translate("MainWindow", "ImageLabel"))
        self.AddNote.setText(_translate("MainWindow", "Добавить данные"))
