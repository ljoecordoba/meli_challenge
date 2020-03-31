# -*- coding: utf-8 -*-
import json
from db_manager import DBManager
from datetime import datetime
import sys
import os
from create_queries_module import create_queries_best_sellers,create_queries_metrics
from api_requester import APIResquester
from metrics import MetricsCollector



#Se obtiene la fecha en formato numerico yyyymmdd
current_date = int(datetime.today().strftime('%Y%m%d'))
#Este objeto nos servira para juntar las metricas
metrics_collector = MetricsCollector()
#Se toman todos los parametros de configuracion
with open('config.json') as json_file:
    data_configuration = json.load(json_file)
    user_db = data_configuration['user_db']
    password_db = data_configuration['password_db']
    host = data_configuration['host']
    database = data_configuration['database']

#1-IMPORTAR LA DATA DESDE LA API DE MERCADO LIBRE
api_requester = APIResquester(data_configuration,metrics_collector)
# Se toman solo los primeros 200 results
json_results=api_requester.get_results()
# Se obtiene el detalle de los items
json_items = api_requester.get_items(json_results)
#Se obtienen los vendedores
json_users = api_requester.get_users(json_results)
#Se obtienen las monedas y su conversion al dolar
currency_conversion_list = api_requester.get_currency_conversion()

#2-CARGAR LAS TABLAS EN MYSQL
db_manager = DBManager(user_db,password_db,host,database,metrics_collector)

db_manager.insertResults(json_results,current_date)
db_manager.insertItems(json_items,current_date)
db_manager.insertUsers(json_users,current_date)
db_manager.insertRatioConversion(currency_conversion_list,current_date)
metrics_collector.setTotalTimeDatabase(time.time())
#print(json_items)


#3-Crear las queries
current_dir = str(os.getcwd())
create_queries_best_sellers(current_dir,current_date)


#4-Exportar las metricas como queries(Utilizo un objeto que haya tomado los tiempos antes)
create_queries_metrics(current_dir,current_date)
db_manager.insertMetrics(current_date)

db_manager.closeConnection()


