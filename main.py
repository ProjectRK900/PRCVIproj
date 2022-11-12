import json
import sys

import psycopg2

from PRCVI import *


def CreateDBConnection(config):
    try:
        conn = psycopg2.connect(database=config["database"], user=config["user"],
                                password=config["password"], host=config["host"], port=int(config["port"]))
        # connection.autocommit = True
        print("[INFO] Connection to the database was successful!")
        return conn
    except Exception as _ex:
        print(f"[INFO] Error while connection with PostgreSQL - {_ex}")


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


