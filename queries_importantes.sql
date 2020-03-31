-- Sellers con mas de 1 item
    select
    a.seller_id,
    b.nickname,
    count(*)
    from results a
    left join sellers b
    on a.seller_id = b.id where a.fecha = 20200331 and b.fecha = 20200331
    group by a.seller_id
    having count(*) > 1;

--Promedio por vendedor

--Precio promedio en dolares
    select
    avg(a.price * b.ratio)
    from results a
    left join currency_ratio_conversion b
    on a.currency_id = b.id
    where a.fecha = 20200331 and b.fecha = 20200331;

--Porcentaje de articulos con garantia
    SELECT
    COUNT(*) / tmp.TOTAL * 100 AS warranty_percentage_items
    FROM items
    INNER JOIN (
            SELECT
            COUNT(*) AS TOTAL
            FROM items where fecha = 20200331
            ) AS tmp where fecha = 20200331 and warranty != 'None';

--Metodos de shipping que ofrecen
    select 
    shipping,
    count(*)
    from results
    where fecha = 20200331
    group by shipping;