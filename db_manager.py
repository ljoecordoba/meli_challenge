# -*- coding: utf-8 -*-
import mysql.connector


class DBManager:
    
    def __init__(self, user_db, password_db, host, database):
        
        self.cnx = mysql.connector.connect(user=user_db, password=password_db,
                              host=host,
                              database=database)
    
    def insertResults(self,results,fecha):
        insert_command = "insert into results(id,site_id,title,seller_id,price\
        ,currency_id,available_quantity,sold_quantity,buying_mode,listing_type_id,\
        stop_time,permalink,thumbnail,accepts_mercadopago,shipping,original_price,\
        category_id,official_store_id,catalog_product_id,\
        fecha) values\
        (\
                \'%s\', \'%s\',\'%s\',%s,%s,\'%s\',%s,%s,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\
                %s,\'%s\',%s,\'%s\',\'%s\',\'%s\'," \
                + str(fecha)+ ")" 
        
        cursor = self.cnx.cursor()
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
                                                ,i['catalog_product_id'])
           cursor.execute(insert_effective)           
        self.cnx.commit()
        print("Se han insertardo los resultados de busqueda")
        cursor.close()

    def insertItems(self,json_items,fecha):
        print("Esta es la salida: " + str(json_items))
        insert_command = "insert into items(id,warranty,fecha) values ( \'%s\',\'%s\', " +str(fecha)+")" 
        cursor = self.cnx.cursor()
        for i in json_items:
           insert_effective = insert_command % (i['id'],i['warranty'])
           #print("Este es el insert:" + insert_effective)
           cursor.execute(insert_effective)           
        self.cnx.commit()
        print("Se han insertardo los items")
        cursor.close()
    def closeConnection(self):
        self.cnx.close()
