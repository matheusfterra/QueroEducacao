import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import Constants

class DBHandler:
    def __init__(self):
        DBHandler.HOST = Constants.HOST
        DBHandler.USER = Constants.USER
        DBHandler.DBNAME = Constants.DATABASE
        DBHandler.PASSWORD = Constants.PASS
    HOST = Constants.HOST
    USER = Constants.USER
    DBNAME = Constants.DATABASE
    PASSWORD = Constants.PASS
    @staticmethod
    def get_mydb():
        if DBHandler.DBNAME == '':
            Constants.init()
        db = DBHandler()
        mydb = db.connect()
        return mydb

    def connect(self):
        try:
            mydb = mysql.connector.connect(
                host=DBHandler.HOST,
                user=DBHandler.USER,
                passwd=DBHandler.PASSWORD,
                database = DBHandler.DBNAME
            )
            return mydb
        except mysql.connector.Error as err:
            print("Error while connecting to MySQL", err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Erro de Conexão com o Banco de Dados")
            msg.setInformativeText("Falha na Comunicação com o Servidor!")
            msg.setWindowTitle("Error")
            msg.setDetailedText(
                "Confira sua conexão com banco de dados!\nCaso seu Acesso esteja normalizado, Contacte o ADM do Servidor.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
