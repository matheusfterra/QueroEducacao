import os
import time
import pipes
from DBHandler import *

def backup():
    DB_HOST = DBHandler.HOST
    DB_USER = DBHandler.USER
    DB_USER_PASSWORD = DBHandler.PASSWORD
    DB_NAME = DBHandler.DBNAME
    BACKUP_PATH = 'db'
    MYSQL_BIN_PATH = 'C:/wamp64/bin/mysql/mysql8.0.21/bin/'  # ENDEREÇO DA PASTA BIN MYSQL

    # Getting current DateTime to create the separate backup folder like "20180817-123433".
    DATETIME = time.strftime('%Y%m%d-%H%M%S')
    TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    # Checking if backup folder already exists or not. If not exists will create it.
    try:
        os.stat(TODAYBACKUPPATH)
    except:
        os.mkdir(TODAYBACKUPPATH)


    db = DB_NAME
    dumpcmd = MYSQL_BIN_PATH + 'mysqldump -h ' + DB_HOST + ' -u ' + DB_USER + ' -p' + DB_USER_PASSWORD + ' ' + db + ' > ' + pipes.quote(
            TODAYBACKUPPATH) + '/' + db + '.sql'
    os.system(dumpcmd)


    saida='Banco de Dados exportado com sucesso!'


    print(saida)