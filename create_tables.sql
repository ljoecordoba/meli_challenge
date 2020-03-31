create database if not exists best_sellers;
use best_sellers;

 create table if not exists results 
 (id varchar(80),
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
 fecha int,
 primary key (id,fecha)
 
 );
 
 
create table if not exists items(
 id varchar(80),
 warranty text,
 fecha int,
  primary key (id,fecha)
 
);

create table if not exists sellers(
 id int,
 nickname text,
 adress text,
 user_type text,
 permalink text,
 level_id text,
 power_seller_status text,
 transactions_canceled int,
 transactions_completed int,
 ratings_negative int,
 ratings_neutral int,
 ratings_positive int,
 fecha int,
 primary key (id,fecha)
 
);

create table if not exists currency_ratio_conversion
(
 id varchar(80),
 ratio double,
 fecha int,
 primary key (id,fecha)
 
);


create table if not exists process_metrics
(
	time_response_search_api double,
	time_response_items_api double,
	amount_items int,
	time_response_users_api double,
	time_response_currencies_api double,
	time_response_conversion_api double,
	total_time_process double,
	total_time_database double,
	fecha int not null,
	index(fecha)
);
