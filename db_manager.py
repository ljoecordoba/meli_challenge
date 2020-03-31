# -*- coding: utf-8 -*-
import mysql.connector
import time

class DBManager:
    
    def __init__(self, user_db, password_db, host, database,metrics_collector):
        
        self.cnx = mysql.connector.connect(user=user_db, password=password_db,
                              host=host,
                              database=database)
        self.metrics_collector = metrics_collector
        self.metrics_collector.setStartTimeDatabase(time.time())
    
    def insertResults(self,results,fecha):
        cursor = self.cnx.cursor()
        delete_command = "delete from results where fecha = " + str(fecha)
        cursor.execute(delete_command)
        insert_command = "insert into results(id,site_id,title,seller_id,price\
        ,currency_id,available_quantity,sold_quantity,buying_mode,listing_type_id,\
        stop_time,permalink,thumbnail,accepts_mercadopago,shipping,original_price,\
        category_id,official_store_id,catalog_product_id,\
        fecha) select \
                \'%s\', \'%s\',\'%s\',%s,%s,\'%s\',%s,%s,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\
                %s,\'%s\',%s,\'%s\',\'%s\',\'%s\'," \
                + str(fecha)+ " where not exists (select id from results where id = \'%s\')" 
        

        for i in results:
           if(i['original_price'] == None or i['original_price'] == 'None'):
               original_price = 'null'
           else:
               original_price = i['original_price']
           insert_effective = insert_command % (i['id'],i['site_id'],i['title']\
                                                ,i['seller']['id'],i['price']\
                                                ,i['currency_id'],i['available_quantity']\
                                                ,i['sold_quantity'],i['buying_mode']\
                                                ,i['listing_type_id'],i['stop_time']\
                                                ,i['permalink'],i['thumbnail'],i['accepts_mercadopago']\
                                                ,i['shipping']['mode'],original_price\
                                                ,i['category_id'],i['official_store_id']\
                                                ,i['catalog_product_id'],i['id'])
           cursor.execute(insert_effective)           
        self.cnx.commit()
        
        print("Se han insertardo los resultados de busqueda")
        cursor.close()

    def insertItems(self,json_items,fecha):
        cursor = self.cnx.cursor()
        delete_command = "delete from items where fecha = " +str(fecha)
        cursor.execute(delete_command)
        insert_command = "insert into items(id,warranty,fecha) select \'%s\',\'%s\', " +str(fecha)+\
        " where not exists (select id from items where id = \'%s\')" 
        for i in json_items:
           insert_effective = insert_command % (i['body']['id'],i['body']['warranty'],i['body']['id'])
           cursor.execute(insert_effective)           
        self.cnx.commit()
        print("Se han insertardo los items")
        cursor.close()
        
    def insertUsers(self,json_users,fecha):
        cursor = self.cnx.cursor()
        delete_command = "delete from sellers where fecha = " + str(fecha)
        cursor.execute(delete_command)
        insert_command = "insert into sellers (id , nickname , adress , \
        user_type , permalink , level_id , power_seller_status , \
        transactions_canceled , \
        transactions_completed , ratings_negative ,\
        ratings_neutral , ratings_positive , fecha) \
        select %s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\',\
        \'%s\', %s, %s, %s, %s, %s," \
                +str(fecha)+" where not exists(select id from sellers where id = %s)" 
        for i in json_users:
           adress =  i['body']['address']['city'] + " " + i['body']['address']['state']
           insert_effective = insert_command % (i['body']['id'],i['body']['nickname'],\
                                                adress,i['body']['user_type'],i['body']['permalink'],\
                                                i['body']['seller_reputation']['level_id'],i['body']['seller_reputation']['power_seller_status'],\
                                                i['body']['seller_reputation']['transactions']['canceled'],\
                                                i['body']['seller_reputation']['transactions']['completed'],\
                                                i['body']['seller_reputation']['transactions']['ratings']['negative'],\
                                                i['body']['seller_reputation']['transactions']['ratings']['neutral'],\
                                                i['body']['seller_reputation']['transactions']['ratings']['positive'],\
                                                i['body']['id']
                                                )
           cursor.execute(insert_effective)           
        self.cnx.commit()
        print("Se han insertardo los vendedores")
        cursor.close()
         
    def insertRatioConversion(self,currency_conversion_list,fecha):
        cursor = self.cnx.cursor()
        delete_command = "delete from currency_ratio_conversion where fecha = " + str(fecha)
        cursor.execute(delete_command)
        insert_command = "insert into currency_ratio_conversion(ratio,id,fecha) select %s,\'%s\',"+ str(fecha) \
        + " where not exists (select id from currency_ratio_conversion where id = \'%s\')"
        for i in currency_conversion_list:
           try:
               insert_effective = insert_command % (i['ratio'],i['id'],i['id'])
               cursor.execute(insert_effective)           
               self.cnx.commit()
           except:
               continue
        print("Se han insertardo las conversiones de moneda")
        cursor.close()
        
    def insertMetrics(self,fecha):
        cursor = self.cnx.cursor()
        delete_command = "delete from process_metrics where fecha = "+ str(fecha)
        cursor.execute(delete_command)
        insert_command = "insert into process_metrics select\n\
        %s,%s,%s,%s,%s,%s,%s,%s,%s where not exists (select fecha from process_metrics\n\
         where fecha = %s)"
        insert_effective = insert_command % (self.metrics_collector.getTimeResponseSearchAPI(),\
                                             self.metrics_collector.getTimeResponseItemsAPI(),\
                                             self.metrics_collector.getAmountItems(),\
                                             self.metrics_collector.getTimeResponseUsersAPI(),\
                                             self.metrics_collector.getTimeResponseCurrenciesAPI(),\
                                             self.metrics_collector.getTimeResponseConversionAPI(),\
                                             self.metrics_collector.getTotalTimeProcess(),\
                                             self.metrics_collector.getTotalTimeDatabase(),
                                             fecha,fecha)
        cursor.execute(insert_effective)
        self.cnx.commit()
        print("Se insertaron las metricas del proceso")
        cursor.close()
        
    def closeConnection(self):
        self.cnx.close()
        
