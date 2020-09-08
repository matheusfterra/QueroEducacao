import json
import urllib.request as urllib2
import time
import pandas as pd

import DBExecute

df = pd.DataFrame()


class GetData:
    def __init__(self):
        print("Software Inicializado!\n")

    @staticmethod
    def get_api():
        # result = requests.get('http://dataeng.quero.com:5000/caged-data')
        # status_request = result.status_code
        # tamanho=result.headers['content-length']
        # #my_data = result.json()
        # print(tamanho)

        url = 'http://dataeng.quero.com:5000/caged-data'
        json_obj = urllib2.urlopen(url)

        data = json.load(json_obj)
        print(data)

    @staticmethod
    def get_dataframe():
        global df
        df = pd.read_csv('dataset/EmployData.csv')
        df['salario'] = df['salario'].str.replace(',','')
        df['salario'] = df['salario'].astype('float')

    @staticmethod
    def get_column_dataframe():
        title = df.columns
        return title

    @staticmethod
    def get_type_data():
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
        DBExecute.create_table(coluna, tipo)

    @staticmethod
    def insert_data():
        print("Os dados do dataset serão inseridos no Banco de Dados({} linhas).\n\nEste processo pode demorar alguns minutos!\n".format(len(df)))
        # for i in range(0,len(df)):
        #     data_send=[]
        #     for j in range(0,len(df.dtypes)):
        #         data_send.append(df.iloc[i][j])
        # print(data_send)
        title = df.columns
        for i in range(0,len(df)):
            data_send=[]
            data_send.append(df.iloc[i])
            DBExecute.insert_data(title, data_send[0])
            time.sleep(0.003)


        print("Inserção no Banco de Dados concluída com Sucesso!")


if __name__ == '__main__':
    mydata = GetData()
    mydata.get_dataframe()
    column_name = mydata.get_column_dataframe()
    type_data = mydata.get_type_data()
    mydata.create_table(column_name, type_data)
    mydata.insert_data()
