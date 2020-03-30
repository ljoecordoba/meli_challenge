import requests
import json
from db_manager import DBManager
from datetime import datetime
import sys

def split_list (list,x):
   return [list[i:i+x] for i in range(0, len(list), x)]


def get_results():
    api_query_0 = "https://api.mercadolibre.com/sites/MLA/search?q=“​Samsung%20Galaxy%20A20&limit=50&offset=0#json"
    api_query_1 = "https://api.mercadolibre.com/sites/MLA/search?q=“​Samsung%20Galaxy%20A20&limit=50&offset=49#json"
    api_query_2 = "https://api.mercadolibre.com/sites/MLA/search?q=“​Samsung%20Galaxy%20A20&limit=50&offset=99#json"
    api_query_3 = "https://api.mercadolibre.com/sites/MLA/search?q=“​Samsung%20Galaxy%20A20&limit=50&offset=149#json"
    api_query_4 = "https://api.mercadolibre.com/sites/MLA/search?q=“​Samsung%20Galaxy%20A20&limit=50&offset=199#json"
    json_results = requests.get(api_query_0).json()['results']
    json_results = json_results + requests.get(api_query_1).json()['results']
    json_results = json_results + requests.get(api_query_2).json()['results']
    json_results = json_results + requests.get(api_query_3).json()['results']
    json_results = json_results + requests.get(api_query_4).json()['results']
    return json_results

def get_items(json_results):
    items_id = []
    for i in json_results:
        items_id.append(i['id'])    
    list_id_items = split_list(items_id,20)
    json_items = []
    for lista in list_id_items:
        items_query = "https://api.mercadolibre.com/items?ids="
        for i in lista:
            items_query = items_query + i +","
    
        items_query.rstrip(',')
        json_items = json_items + requests.get(items_query).json()
        
    return json_items

def get_users(json_results):
    users_id = []
    for i in json_results:
        users_id.append(i['seller']['id'])
    
    list_id_users = split_list(users_id,20)
    json_users = []
    for lista in list_id_users:
        users_query = "https://api.mercadolibre.com/users?ids="
        for i in lista:
            users_query = users_query + str(i) +","
    
        users_query.rstrip(',')
        json_users = json_users + requests.get(users_query).json()
        
    return json_users

current_date = int(datetime.today().strftime('%Y%m%d'))

with open('config.json') as json_file:
    data = json.load(json_file)
    user_db = data['user_db']
    password_db = data['password_db']
    host = data['host']
    database = data['database']





   


#1-IMPORTAR LA DATA DESDE LA API DE MERCADO LIBRE
    
# Se toman solo los primeros 200 results
json_results=get_results()
# Se obtiene el detalle de los items
json_items = get_items(json_results)
#Se obtienen los vendedores
json_users = get_users(json_results)

#Se obtienen las monedas y su conversion al dolar
currency_conversion_query = 'https://api.mercadolibre.com/currency_conversions/search?from=XXX&to=USD'
currency_query = 'https://api.mercadolibre.com/currencies'
json_currencies = requests.get(currency_query).json()
currency_conversion_list = []
for i in json_currencies:
    currency_id = i['id']
    currency_query_effective = currency_conversion_query.replace('XXX',currency_id)
    currency_conversion = requests.get(currency_query_effective).json()
    currency_conversion['id'] = currency_id
    currency_conversion_list.append(currency_conversion)


#2-CARGAR LAS TABLAS EN MYSQL
db_manager = DBManager(user_db,password_db,host,database)

#db_manager.insertResults(json_results,current_date)
#db_manager.insertItems(json_items,current_date)
#db_manager.insertUsers(json_users,current_date)
#db_manager.insertRatioConversion(currency_conversion_list,current_date)
print(json_items)

db_manager.closeConnection()

#3-Crear las queries





#4-Exportar las metricas como queries(Utilizo un objeto que haya tomado los tiempos antes)



