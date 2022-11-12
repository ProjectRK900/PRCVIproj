# Form implementation generated from reading ui file 'FuncWind.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem


class Ui_FuncWind(object):
    def setupUi(self, FuncWind):
        FuncWind.setObjectName("FuncWind")
        FuncWind.resize(1080, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FuncWind.setWindowIcon(icon)
        FuncWind.setStyleSheet("QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(FuncWind)
        self.centralwidget.setObjectName("centralwidget")
        self.AddNoteTable = QtWidgets.QTableWidget(self.centralwidget)
        self.AddNoteTable.setGeometry(QtCore.QRect(20, 10, 1041, 411))
        self.AddNoteTable.setObjectName("AddNoteTable")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 470, 1051, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CreateNote = QtWidgets.QPushButton(self.horizontalLayoutWidget,
                                                clicked=lambda: self.AddNoteTable.setRowCount(self.AddNoteTable.rowCount() + 1))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.CreateNote.setFont(font)
        self.CreateNote.setObjectName("CreateNote")
        self.horizontalLayout.addWidget(self.CreateNote)
        self.EditNote = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.EditNote.setFont(font)
        self.EditNote.setObjectName("EditNote")
        self.EditNote = QtWidgets.QPushButton(self.horizontalLayoutWidget,
                                               clicked=lambda: print(self.AddNoteTable.currentRow()))
        self.horizontalLayout.addWidget(self.EditNote)
        self.DeleteNote = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.DeleteNote.setFont(font)
        self.DeleteNote.setObjectName("DeleteNote")
        self.horizontalLayout.addWidget(self.DeleteNote)
        FuncWind.setCentralWidget(self.centralwidget)

        self.retranslateUi(FuncWind)
        QtCore.QMetaObject.connectSlotsByName(FuncWind)

    #def DeleteFromDB(self, conn=None):


    def UpdateMarkTable(self, queryStr="select 'no', 'data', 'found'", conn=None):
        if (conn):
            cur = conn.cursor()
            cur.execute(queryStr)
            self.AddNoteTable.setColumnCount(6)
            self.AddNoteTable.setHorizontalHeaderLabels(
                ['markup_id', 'Файл разметки', 'Оригинальный файл', 'Тип', 'Регион', 'Время съёмки'])
            for row in cur:
                rows = self.AddNoteTable.rowCount()
                self.AddNoteTable.setRowCount(rows + 1)
                # self.AddNoteTable.setItem(rows, cols, QTableWidgetItem(str(row[0])))
                self.AddNoteTable.setItem(rows, 0, QTableWidgetItem(str(row[0])))
                self.AddNoteTable.setItem(rows, 1, QTableWidgetItem(row[1]))
                self.AddNoteTable.setItem(rows, 2, QTableWidgetItem(row[2]))
                self.AddNoteTable.setItem(rows, 3, QTableWidgetItem(row[3]))
                self.AddNoteTable.setItem(rows, 4, QTableWidgetItem(row[4]))
                self.AddNoteTable.setItem(rows, 5, QTableWidgetItem(str(row[5])))
            self.AddNoteTable.resizeColumnsToContents()
            cur.close()
            conn.close()
            print("[INFO] Connection has been closed")
            if (self.AddNoteTable.rowCount() >= 0):
                self.AddNoteTable.selectRow(0)
            self.AddNoteTable.setColumnHidden(0, True)
        else:
            print("[ERROR] The table has not been updated as there is no connection")

    def retranslateUi(self, FuncWind):
        _translate = QtCore.QCoreApplication.translate
        FuncWind.setWindowTitle(_translate("FuncWind", "Работа с данными"))
        self.CreateNote.setText(_translate("FuncWind", "Добавить строку"))
        self.EditNote.setText(_translate("FuncWind", "Изменить строку в базе"))
        self.DeleteNote.setText(_translate("FuncWind", "Удалить данные из базы"))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FuncWind = QtWidgets.QMainWindow()
    ui = Ui_FuncWind()
    ui.setupUi(FuncWind)
    FuncWind.show()
    sys.exit(app.exec())"""
