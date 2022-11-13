from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OpenFile(object):
    def setupUi(self, OpenFile):
        OpenFile.setObjectName("OpenFile")
        OpenFile.resize(1080, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo_vert.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        OpenFile.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OpenFile)
        self.centralwidget.setObjectName("centralwidget")
        OpenFile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OpenFile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        OpenFile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OpenFile)
        self.statusbar.setObjectName("statusbar")
        OpenFile.setStatusBar(self.statusbar)

        self.retranslateUi(OpenFile)
        QtCore.QMetaObject.connectSlotsByName(OpenFile)

    def retranslateUi(self, OpenFile):
        _translate = QtCore.QCoreApplication.translate
        OpenFile.setWindowTitle(_translate("OpenFile", "OpenFileWind"))