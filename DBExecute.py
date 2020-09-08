from DBHandler import *

def create_table(coluna,tipo):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'caged'")
    if cursor.fetchone()[0] == 1:
        print("A tabela já existe!")
    else:

        cursor.execute("CREATE TABLE caged (db_id INT NOT NULL AUTO_INCREMENT,{} {}, {} {}, {} {}, {} {},{} {}, {} {}, {} {}, {} {},{} {},"
                       " {} {}, {} {}, {} {},{} {}, {} {}, {} {}, {} {},{} {}, {} {}, {} {}, {} {},{} {}, {} {}, {} {}, {} {},{} {},PRIMARY KEY (db_id))".format(
            coluna[0],tipo[0],
            coluna[1], tipo[1],
            coluna[2], tipo[2],
            coluna[3], tipo[3],
            coluna[4], tipo[4],
            coluna[5], tipo[5],
            coluna[6], tipo[6],
            coluna[7], tipo[7],
            coluna[8], tipo[8],
            coluna[9], tipo[9],
            coluna[10], tipo[10],
            coluna[11], tipo[11],
            coluna[12], tipo[12],
            coluna[13], tipo[13],
            coluna[14], tipo[14],
            coluna[15], tipo[15],
            coluna[16], tipo[16],
            coluna[17], tipo[17],
            coluna[18], tipo[18],
            coluna[19], tipo[19],
            coluna[20], tipo[20],
            coluna[21], tipo[21],
            coluna[22], tipo[22],
            coluna[23], tipo[23],
            coluna[24], tipo[24]))
        print("Sucesso na criação da Tabela do Banco de Dados")


def insert_data(coluna,dados):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO caged({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}) "
                   "VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(
    coluna[0],coluna[1],coluna[2],coluna[3],coluna[4],coluna[5],coluna[6],coluna[7],coluna[8],
    coluna[9],coluna[10],coluna[11],coluna[12],coluna[13],coluna[14],coluna[15],coluna[16],coluna[17],coluna[18],
    coluna[19],coluna[20],coluna[21],coluna[22],coluna[23],coluna[24],dados[0],dados[1],dados[2],dados[3],dados[4],
    dados[5],dados[6],dados[7],dados[8],dados[9],dados[10],dados[11],dados[12],dados[13],dados[14],dados[15],dados[16],
    dados[17],dados[18],dados[19],dados[20],dados[21],dados[22],dados[23],dados[24]))

    mydb.commit()

