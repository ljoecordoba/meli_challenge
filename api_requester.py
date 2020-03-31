# -*- coding: utf-8 -*-
import requests

def split_list (list,x):
   return [list[i:i+x] for i in range(0, len(list), x)]
class APIResquester:
    def __init__(self, data_configuration,metrics_collector):
        self.data_configuration = data_configuration
        self.metrics_collector = metrics_collector


    def get_results(self):
        json_results = []
        queries = self.data_configuration['api_query']
        accum = 0.0
        for query in queries:
            response = requests.get(query)
            accum += response.elapsed.total_seconds()
            json_results = json_results + response.json()['results']
        
        time_average_response = accum / float(len(queries))
        self.metrics_collector.setTimeResponseSearchAPI(time_average_response)
        self.metrics_collector.setAmountItems(len(json_results))
        return json_results

    def get_items(self,json_results):
        items_id = []
        accum = 0.0
        for i in json_results:
            items_id.append(i['id'])    
        list_id_items = split_list(items_id,20)
        json_items = []
        for lista in list_id_items:
            items_query = self.data_configuration['items_query']
            for i in lista:
                items_query = items_query + i +","
        
            items_query = items_query.rstrip(',')
            response = requests.get(items_query)
            accum += response.elapsed.total_seconds()
            json_items = json_items + response.json()
        
        time_average_response = accum / float(len(list_id_items))
        self.metrics_collector.setTimeResponseItemsAPI(time_average_response)
        return json_items

    def get_users(self,json_results):
        users_id = []
        accum = 0.0
        for i in json_results:
            users_id.append(i['seller']['id'])
        
        #Remuevo repetidos de la lista de vendedores
        users_id = list(dict.fromkeys(users_id))
        
        list_id_users = split_list(users_id,20)
        json_users = []
        for lista in list_id_users:
            users_query = self.data_configuration['users_query']
            for i in lista:
                users_query = users_query + str(i) +","
        
            users_query = users_query.rstrip(',')
            response = requests.get(users_query)
            accum += response.elapsed.total_seconds()
            json_users = json_users + response.json()
        
        time_average_response = accum / float(len(list_id_users))
        self.metrics_collector.setTimeResponseUsersAPI(time_average_response)
        return json_users

    def get_currency_conversion(self):
        currency_conversion_query = self.data_configuration['currency_conversion_query']
        currency_query = self.data_configuration['currency_query']
        response_currencies = requests.get(currency_query)
        self.metrics_collector.setTimeResponseCurrenciesAPI(response_currencies.elapsed.total_seconds())
        json_currencies = response_currencies.json()
        currency_conversion_list = []
        accum = 0.0
        for i in json_currencies:
            currency_id = i['id']
            currency_query_effective = currency_conversion_query.replace('XXX',currency_id)
            response = requests.get(currency_query_effective)
            accum += response.elapsed.total_seconds()
            currency_conversion = response.json()
            currency_conversion['id'] = currency_id
            currency_conversion_list.append(currency_conversion)
            
        time_average_response = accum / float(len(json_currencies))        
        self.metrics_collector.setTimeResponseConversionAPI(time_average_response)
        return currency_conversion_list
