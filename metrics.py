# -*- coding: utf-8 -*-
import time
class MetricsCollector:
    def __init__(self):
      #Tiempo que se toma en traer los resultados totales
      self.time_response_search_api = 0.0
      self.time_response_items_api = 0.0
      self.amount_items = 0
      self.time_response_users_api = 0.0
      self.time_response_currencies_api = 0.0
      self.time_response_conversion_api = 0.0
      self.start_time_process = time.time()
      self.start_time_database = 0
      self.total_time_database = 0
    def __str__(self):
        return str(self.time_response_search_api) + " " + str(self.time_response_items_api) +\
            " " + str(self.amount_items) + " " + str(self.time_response_users_api) + " " \
            + str(self.time_response_currencies_api) + " " + str(self.time_response_conversion_api)\
            + " " + str(self.total_time_database)
      
    def setTimeResponseSearchAPI(self,time_response_search_api):
        self.time_response_search = time_response_search_api
        
    def getTimeResponseSearchAPI(self):
        return self.time_response_search_api
    
    def setTimeResponseItemsAPI(self,time_response_items_api):
        self.time_response_items_api = time_response_items_api

    def getTimeResponseItemsAPI(self):
        return self.time_response_items_api
    
    def setAmountItems(self,amount_items):
        self.amount_items = amount_items
        
    def getAmountItems(self):
        return self.amount_items
    
    def setTimeResponseUsersAPI(self,time_response_users_api):
      self.time_response_users_api = time_response_users_api

    def getTimeResponseUsersAPI(self):
        return self.time_response_users_api
    
    def setTimeResponseCurrenciesAPI(self,time_response_currencies_api):
        self.time_response_currencies_api = time_response_currencies_api
    
    def getTimeResponseCurrenciesAPI(self):
        return self.time_response_currencies_api
    
    def setTimeResponseConversionAPI(self,time_response_conversion_api):
        self.time_response_conversion_api = time_response_conversion_api 
        
    def getTimeResponseConversionAPI(self):
        return self.time_response_conversion_api
    
    def getTotalTimeProcess(self):
        return time.time() - self.start_time_process
    
    def setStartTimeDatabase(self,start_time):
        self.start_time_database = start_time
    
    def setTotalTimeDatabase(self,finish_time):
        self.total_time_database = finish_time - self.start_time_database
    
    def getTotalTimeDatabase(self):
        return self.total_time_database
    