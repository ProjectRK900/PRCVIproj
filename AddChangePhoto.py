from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddChangePhoto(object):

    def setupUi(self, AddChangePhoto, mode, FuncWind, _configNote=None, conn=None):
        AddChangePhoto.setObjectName("AddChangePhoto")
        AddChangePhoto.resize(711, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddChangePhoto.setWindowIcon(icon)
        AddChangePhoto.setStyleSheet("QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(AddChangePhoto)
        self.centralwidget.setObjectName("centralwidget")
        self.PathLabel = QtWidgets.QLabel(self.centralwidget)
        self.PathLabel.setGeometry(QtCore.QRect(100, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.PathLabel.setFont(font)
        self.PathLabel.setObjectName("PathLabel")
        self.PathBrowseBtn = QtWidgets.QPushButton(self.centralwidget,
                                                   clicked=lambda: self.BrowseBtn_clicked())
        self.PathBrowseBtn.setGeometry(QtCore.QRect(600, 30, 91, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.PathBrowseBtn.setFont(font)
        self.PathBrowseBtn.setObjectName("PathBrowseBtn")
        self.PathTEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.PathTEdit.setGeometry(QtCore.QRect(200, 20, 391, 71))
        self.PathTEdit.setReadOnly(True)
        self.PathTEdit.setObjectName("PathTEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(200, 190, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeEdit.setFont(font)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.RegionLabel = QtWidgets.QLabel(self.centralwidget)
        self.RegionLabel.setGeometry(QtCore.QRect(20, 110, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.RegionLabel.setFont(font)
        self.RegionLabel.setObjectName("RegionLabel")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(80, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.RegionTEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.RegionTEdit.setGeometry(QtCore.QRect(200, 110, 391, 71))
        self.RegionTEdit.textChanged.connect(lambda: self.TextChangedCheck())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RegionTEdit.setFont(font)
        self.RegionTEdit.setObjectName("RegionTEdit")
        if _configNote:
            id = int(_configNote["id"])
        else:
            id = None
        self.AddPhotoBtn = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked=lambda: self.SavePhotoBtn_clicked(mode, FuncWind, conn,
                                                                                           id, AddChangePhoto))
        self.AddPhotoBtn.setGeometry(QtCore.QRect(290, 220, 231, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.AddPhotoBtn.setFont(font)
        self.AddPhotoBtn.setObjectName("AddPhotoBtn")
        AddChangePhoto.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddChangePhoto, mode)
        QtCore.QMetaObject.connectSlotsByName(AddChangePhoto)
        if mode == "Изменить":
            fullpath = _configNote["path"].replace('/', '\\') + _configNote["name"]
            self.PathTEdit.setText(fullpath)
            self.RegionTEdit.setText(_configNote["region"])
            from PyQt6.QtCore import QTime
            time_strs = str(_configNote["time"]).split(':')
            hours = int(time_strs[0])
            minutes = int(time_strs[1])
            seconds = int(time_strs[2])
            self.timeEdit.setTime(QTime(hours, minutes, seconds))

    def SavePhotoBtn_clicked(self, mode, oldWin, conn=None, id=None, win=None):
        if conn and len(self.PathTEdit.toPlainText()) > 1 and self.PathTEdit.toPlainText() != "*файл не выбран*":
            cur = conn.cursor()
            path = self.PathTEdit.toPlainText().split('\\')
            name = path[len(path) - 1]
            path = path[:-1]
            path_without_name = ""
            for dir in path:
                path_without_name = path_without_name + dir
                path_without_name = path_without_name + '\\'
            if mode == "Добавить":
                cur.execute(f"""insert into sources (region, date, image, name) 
                                values ('{self.RegionTEdit.toPlainText()}',
                                 '{self.timeEdit.text()}', '{path_without_name}', '{name}')""")
            if mode == "Изменить":
                cur.execute(f"""update sources 
                                set region = '{self.RegionTEdit.toPlainText()}',
                                date = '{self.timeEdit.text()}',
                                image = '{path_without_name}',
                                name = '{name}'
                                where image_id = {id}""")
            cur.close()
            conn.commit()
            oldWin.UpdateTables(conn)
            win.close()
        else:
            print("[ERROR] Cannot change database")

    def TextChangedCheck(self):
        if len(self.RegionTEdit.toPlainText()) > 100:
            text = self.RegionTEdit.toPlainText()
            text = text[:100]
            self.RegionTEdit.setPlainText(text)
            cursor = self.RegionTEdit.textCursor()
            cursor.setPosition(100)
            self.RegionTEdit.setTextCursor(cursor)

    def BrowseBtn_clicked(self):
        from PyQt6.QtWidgets import QFileDialog
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        dlg.setNameFilters(["Images (*.jpg *.png)"])
        if dlg.exec():
            self.PathTEdit.setText(dlg.selectedFiles()[0].replace('/', '\\'))

    def retranslateUi(self, AddChangePhoto, mode):
        _translate = QtCore.QCoreApplication.translate
        AddChangePhoto.setWindowTitle(_translate("AddChangePhoto", f"{mode} фото"))
        self.PathLabel.setText(_translate("AddChangePhoto", "Путь к фото:"))
        self.PathBrowseBtn.setText(_translate("AddChangePhoto", "Открыть..."))
        self.PathTEdit.setHtml(_translate("AddChangePhoto",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">*файл не выбран*</span></p></body></html>"))
        self.timeEdit.setDisplayFormat(_translate("AddChangePhoto", "HH:mm:ss"))
        self.RegionLabel.setText(_translate("AddChangePhoto", "Место/регион съёмки:"))
        self.TimeLabel.setText(_translate("AddChangePhoto", "Время съёмки:"))
        self.RegionTEdit.setHtml(_translate("AddChangePhoto",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AddPhotoBtn.setText(_translate("AddChangePhoto", "Сохранить запись в базу данных"))
