import json
import sys

from PRCVI import *

if __name__ == "__main__":
    _configDB = {
        "database": "",
        "user": "",
        "password": "",
        "host": "",
        "port": ""
    }

    with open("configDB.json", "r") as settingsDB:
        _configDB = json.loads(settingsDB.read())
        _configDB["password"] = ""

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, _configDB)
    MainWindow.show()
    sys.exit(app.exec())


