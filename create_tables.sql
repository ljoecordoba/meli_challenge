 create table results 
 (id text,
    site_id text,
    title text,
    seller_id int,
    price double,
    currency_id text,
    available_quantity int,
    sold_quantity int,
    buying_mode text,
    listing_type_id text,
    stop_time text,
    permalink text,
    thumbnail text,
    accepts_mercadopago boolean,
    shipping text,
    original_price double,
    category_id text,
    official_store_id text,
    catalog_product_id text,
 fecha int not null
 ) 
 partition by key(fecha);
 
 
create table items(
 id text,
 warranty text,
 fecha int not null
)
 partition by key(fecha);
