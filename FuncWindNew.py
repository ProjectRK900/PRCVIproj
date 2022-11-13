from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from AddChangePhoto import Ui_AddChangePhoto


class Ui_FuncWind(object):

    def setupUi(self, FuncWind, _config):
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
        self.AddNoteTable.setGeometry(QtCore.QRect(455, 50, 611, 401))
        self.AddNoteTable.setObjectName("AddNoteTable")
        self.AddNoteTable.setColumnCount(0)
        self.AddNoteTable.setRowCount(0)
        self.OriginalPhotoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.OriginalPhotoTable.setGeometry(QtCore.QRect(15, 50, 431, 401))
        self.OriginalPhotoTable.setObjectName("OriginalPhotoTable")
        self.OriginalPhotoTable.setColumnCount(0)
        self.OriginalPhotoTable.setRowCount(0)
        self.origLabel = QtWidgets.QLabel(self.centralwidget)
        self.origLabel.setGeometry(QtCore.QRect(20, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.origLabel.setFont(font)
        self.origLabel.setObjectName("origLabel")
        self.origLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.origLabel_2.setGeometry(QtCore.QRect(460, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.origLabel_2.setFont(font)
        self.origLabel_2.setObjectName("origLabel_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 460, 1061, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CreateMarkup = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.CreateMarkup.setFont(font)
        self.CreateMarkup.setObjectName("CreateMarkup")
        self.horizontalLayout_2.addWidget(self.CreateMarkup)
        self.ChangeMarkup = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.ChangeMarkup.setFont(font)
        self.ChangeMarkup.setObjectName("ChangeMarkup")
        self.horizontalLayout_2.addWidget(self.ChangeMarkup)
        self.DeleteMarkup = QtWidgets.QPushButton(self.layoutWidget,
                                                  clicked=lambda: self.DeleteBtn_clicked("разметку", _config))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.DeleteMarkup.setFont(font)
        self.DeleteMarkup.setObjectName("DeleteMarkup")
        self.horizontalLayout_2.addWidget(self.DeleteMarkup)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CreatePhoto = QtWidgets.QPushButton(self.layoutWidget,
                                                 clicked=lambda: self.AddPhotoBtn_clicked(_config))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.CreatePhoto.setFont(font)
        self.CreatePhoto.setObjectName("CreatePhoto")
        self.horizontalLayout.addWidget(self.CreatePhoto)
        self.ChangePhoto = QtWidgets.QPushButton(self.layoutWidget,
                                                 clicked=lambda: self.ChangePhotoBtn_clicked(_config))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.ChangePhoto.setFont(font)
        self.ChangePhoto.setObjectName("ChangePhoto")
        self.horizontalLayout.addWidget(self.ChangePhoto)
        self.DeletePhoto = QtWidgets.QPushButton(self.layoutWidget,
                                                 clicked=lambda: self.DeleteBtn_clicked("фото", _config))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.DeletePhoto.setFont(font)
        self.DeletePhoto.setObjectName("DeletePhoto")
        self.horizontalLayout.addWidget(self.DeletePhoto)
        self.verticalLayout.addLayout(self.horizontalLayout)
        FuncWind.setCentralWidget(self.centralwidget)

        self.retranslateUi(FuncWind)
        QtCore.QMetaObject.connectSlotsByName(FuncWind)

    def AddPhotoBtn_clicked(self, _configDB):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddChangePhoto()
        self.ui.setupUi(self.window, "Добавить", self, conn=self.CreateDBConnection(_configDB))
        self.window.show()

    def ChangePhotoBtn_clicked(self, _configDB):
        _configNote = {
            "id": self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 0).text(),
            "path": self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 2).text(),
            "name": self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 1).text(),
            "region": self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 3).text(),
            "time": self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 4).text()
        }

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddChangePhoto()
        self.ui.setupUi(self.window, "Изменить", self, _configNote, conn=self.CreateDBConnection(_configDB))
        self.window.show()

    def DeleteBtn_clicked(self, mode, _configDB):
        if mode == "разметку":
            self.OpenDeleteDialog(self.AddNoteTable.item(self.AddNoteTable.currentRow(), 2).text(), mode, _configDB)
        if mode == "фото":
            self.OpenDeleteDialog(self.OriginalPhotoTable.item(
                self.OriginalPhotoTable.currentRow(), 1).text(), mode, _configDB)

    def DeleteFromDB(self, id, table, conn, new_id=0):
        cur = conn.cursor()
        id = int(id)
        if table == 'sources':
            col = 'image_id'
        else:
            col = 'markup_id'
        cur.execute(f"delete from {table} where {col} = {id}")
        conn.commit()
        self.UpdateTables(conn)
        if table == 'sources' and new_id >= 0:
            self.OriginalPhotoTable.selectRow(new_id)
        if table == 'markup' and new_id >= 0:
            self.AddNoteTable.selectRow(new_id)
        conn.close()

    def OpenDeleteDialog(self, path, mode, _configDB):
        dlg = QMessageBox()
        dlg.setWindowIcon(QtGui.QIcon("icons/logo_vert.png"))
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.addButton(QMessageBox.StandardButton.Cancel)
        dlg.addButton(QMessageBox.StandardButton.Apply)
        dlg.setWindowTitle("Внимание!")
        dlg.setText(f'Вы действительно хотите удалить {mode}\n"{path}"?')
        if dlg.exec() == 33554432:
            if mode == "разметку":
                self.DeleteFromDB(self.AddNoteTable.item(self.AddNoteTable.currentRow(), 0).text(),
                                  "markup",
                                  self.CreateDBConnection(_configDB),
                                  self.AddNoteTable.currentRow() - 1)
            if mode == "фото":
                self.DeleteFromDB(self.OriginalPhotoTable.item(self.OriginalPhotoTable.currentRow(), 0).text(),
                                  "sources",
                                  self.CreateDBConnection(_configDB),
                                  self.OriginalPhotoTable.currentRow() - 1)

    def UpdateTables(self, conn=None):
        if conn:
            cur = conn.cursor()
            cur.execute("select * from main_view")

            self.AddNoteTable.setColumnCount(0)
            self.AddNoteTable.setRowCount(0)
            self.OriginalPhotoTable.setColumnCount(0)
            self.OriginalPhotoTable.setRowCount(0)

            self.AddNoteTable.setColumnCount(9)
            self.AddNoteTable.setHorizontalHeaderLabels(
                ['markup_id', 'image_id', 'Файл разметки', 'Оригинальный файл', 'Тип', 'Регион',
                 'Время съёмки', 'Путь разметки', 'Путь оригинала'])
            for row in cur:
                rows = self.AddNoteTable.rowCount()
                self.AddNoteTable.setRowCount(rows + 1)
                self.AddNoteTable.setItem(rows, 0, QTableWidgetItem(str(row[0])))
                self.AddNoteTable.setItem(rows, 1, QTableWidgetItem(str(row[1])))
                self.AddNoteTable.setItem(rows, 2, QTableWidgetItem(row[3]))
                self.AddNoteTable.setItem(rows, 3, QTableWidgetItem(row[5]))
                self.AddNoteTable.setItem(rows, 4, QTableWidgetItem(row[6]))
                self.AddNoteTable.setItem(rows, 5, QTableWidgetItem(row[7]))
                self.AddNoteTable.setItem(rows, 6, QTableWidgetItem(str(row[8])))
                self.AddNoteTable.setItem(rows, 7, QTableWidgetItem(row[2]))
                self.AddNoteTable.setItem(rows, 8, QTableWidgetItem(row[4]))
            self.AddNoteTable.resizeColumnsToContents()
            if self.AddNoteTable.rowCount() >= 1:
                self.AddNoteTable.selectRow(0)
            self.AddNoteTable.setColumnHidden(0, True)
            self.AddNoteTable.setColumnHidden(1, True)

            cur.execute("select * from sources")
            self.OriginalPhotoTable.setColumnCount(5)
            self.OriginalPhotoTable.setHorizontalHeaderLabels(
                ['image_id', 'Файл', 'Путь фото', 'Регион', 'Время съёмки'])
            for row in cur:
                rows = self.OriginalPhotoTable.rowCount()
                self.OriginalPhotoTable.setRowCount(rows + 1)
                self.OriginalPhotoTable.setItem(rows, 0, QTableWidgetItem(str(row[0])))
                self.OriginalPhotoTable.setItem(rows, 1, QTableWidgetItem(row[4]))
                self.OriginalPhotoTable.setItem(rows, 2, QTableWidgetItem(row[3]))
                self.OriginalPhotoTable.setItem(rows, 3, QTableWidgetItem(row[1]))
                self.OriginalPhotoTable.setItem(rows, 4, QTableWidgetItem(str(row[2])))
            self.OriginalPhotoTable.resizeColumnsToContents()
            if self.OriginalPhotoTable.rowCount() >= 1:
                self.OriginalPhotoTable.selectRow(0)
            self.OriginalPhotoTable.setColumnHidden(0, True)

            cur.close()
            conn.close()
            print("[INFO] Connection has been closed")
        else:
            print("[ERROR] The tables has not been updated as there is no connection")

    def CreateDBConnection(self, config):
        try:
            import psycopg2
            conn = psycopg2.connect(database=config["database"], user=config["user"],
                                    password=config["password"], host=config["host"], port=int(config["port"]))
            print("[INFO] Connection to the database was successful!")
            return conn
        except Exception as _ex:
            print(f"[INFO] Error while connection with PostgreSQL - {_ex}")

    def retranslateUi(self, FuncWind):
        _translate = QtCore.QCoreApplication.translate
        FuncWind.setWindowTitle(_translate("FuncWind", "Работа с данными"))
        self.origLabel.setText(_translate("FuncWind", "Оригинальные снимки:"))
        self.origLabel_2.setText(_translate("FuncWind", "Разметка снимков:"))
        self.CreateMarkup.setText(_translate("FuncWind", "Добавить разметку"))
        self.ChangeMarkup.setText(_translate("FuncWind", "Изменить разметку"))
        self.DeleteMarkup.setText(_translate("FuncWind", "Удалить разметку из базы"))
        self.CreatePhoto.setText(_translate("FuncWind", "Добавить оригинальный снимок"))
        self.ChangePhoto.setText(_translate("FuncWind", "Изменить оригинальный снимок"))
        self.DeletePhoto.setText(_translate("FuncWind", "Удалить оригинальный снимок из базы"))
