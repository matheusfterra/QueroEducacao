import json
import urllib.request as urllib2
import time
import pandas as pd
import DBExecute
from DBBackup import *

#Criação do Dataframe
df = pd.DataFrame()

#Classe Principal
class DataManipulation:
    def __init__(self):
        print("Software Inicializado!\n")

    @staticmethod
    def show_data():
        #Apresentação dos dados diretamente da API
        url = 'http://dataeng.quero.com:5000/caged-data'
        json_obj = urllib2.urlopen(url)

        data = json.load(json_obj)
        print(data)

    @staticmethod
    def get_dataframe():
        #Obteção dos dados e inserção no dataframe
        global df
        df = pd.read_csv('dataset/EmployData.csv')
        df['salario'] = df['salario'].str.replace(',', '')
        df['salario'] = df['salario'].astype('float')

    @staticmethod
    def get_column_dataframe():
        #Recuperação das colunas da tabela
        title = df.columns
        return title

    @staticmethod
    def get_type_data():
        #Recuperação do tipo de dados das colunas, para criação automática da tabela do BD
        tipo = df.dtypes
        print("Há {} colunas a serem criadas na Tabela.\n".format(len(tipo)))
        tipos = []
        for tip in tipo:
            if tip == "int64":
                tipos.append('int(11)')
            elif tip == "object":
                tipos.append('VARCHAR(255)')
            elif tip == "float":
                tipos.append('float(11)')

        return tipos

    @staticmethod
    def create_table(coluna, tipo):
        #Chama a função para criação da tabela no BD
        DBExecute.create_table(coluna, tipo)

    @staticmethod
    def insert_data():
        #Inserção dos dados na tabela já criada
        print(
            "Os dados do dataset serão inseridos no Banco de Dados ({} linhas).\n\nEste processo pode demorar alguns "
            "minutos! (Aproximadamente, 4min)\n".format(
                len(df)))

        title = df.columns
        for i in range(0, len(df)):
            data_send = [df.iloc[i]]
            DBExecute.insert_data(title, data_send[0])
            time.sleep(0.01)

        print("Inserção no Banco de Dados concluída com Sucesso!")

    @staticmethod
    def export_db():
        #Exportação do banco de dados

        #OBS: Para funcionamento da função de exportação, deve-se alterar o diretorio do MySQL, na classe DBBackup.py
        print("\nExportando Banco de Dados")
        backup()


if __name__ == '__main__':
    mydata = DataManipulation()
    mydata.get_dataframe()
    column_name = mydata.get_column_dataframe()
    type_data = mydata.get_type_data()
    mydata.create_table(column_name, type_data)
    mydata.insert_data()
    mydata.export_db()
