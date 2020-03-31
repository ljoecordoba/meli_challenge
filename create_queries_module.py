# -*- coding: utf-8 -*-


def create_queries_best_sellers(dir,fecha):
    
    f = open(dir+"/queries_importantes.sql", "w")
    
    query1 = '-- Sellers con mas de 1 item\n\
    select\n\
    a.seller_id,\n\
    b.nickname,\n\
    count(*)\n\
    from results a\n\
    left join sellers b\n\
    on a.seller_id = b.id where a.fecha = <FECHA> and b.fecha = <FECHA>\n\
    group by a.seller_id\n\
    having count(*) > 1;\n\n'
    
    query2 = '--Promedio por vendedor\n\n'
    
    query3 = '--Precio promedio en dolares\n\
    select\n\
    avg(a.price * b.ratio)\n\
    from results a\n\
    left join currency_ratio_conversion b\n\
    on a.currency_id = b.id\n\
    where a.fecha = <FECHA> and b.fecha = <FECHA>;\n\n'
    
    query4 = '--Porcentaje de articulos con garantia\n\
    SELECT\n\
    COUNT(*) / tmp.TOTAL * 100 AS warranty_percentage_items\n\
    FROM items\n\
    INNER JOIN (\n\
            SELECT\n\
            COUNT(*) AS TOTAL\n\
            FROM items where fecha = <FECHA>\n\
            ) AS tmp where fecha = <FECHA> and warranty != \'None\';\n\n'
    query5 = '--Metodos de shipping que ofrecen\n\
    select \n\
    shipping,\n\
    count(*)\n\
    from results\n\
    where fecha = <FECHA>\n\
    group by shipping;'
    
    query = query1 + query2 + query3 + query4 + query5
    query = query.replace("<FECHA>",str(fecha))
    
    f.write(query)
    f.close()
 
def create_queries_metrics(dir,fecha):
    f = open(dir+"/queries_procesos.sql", "w")
    
    query = 'select \n\
    time_response_search_api , \n\
    time_response_items_api , \n\
    amount_items , \n\
    time_response_users_api , \n\
    time_response_currencies_api , \n\
    time_response_conversion_api , \n\
    total_time_process , \n\
    total_time_database ,\n\
    fecha \n\
    from process_metrics;'
    f.write(query)
    f.close()
