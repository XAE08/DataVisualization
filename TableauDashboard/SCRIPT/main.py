#importing necessary libraries
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


#Providing database details below
DATABASE_TYPE='postgresql'
DBAPI='psycopg2'
HOST='localhost'
USER='postgres'
PASSWORD='postgres'
DATABASE='olist'
PORT=5432

#Create engine
engine=create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

#Reading files of data folder
csv_files={
    'olist_customer_dataset' :'../Data/OLIST/olist_customers_dataset.csv', 
    'olist_geolocation_dataset':'../Data/OLIST/olist_geolocation_dataset.csv',
    'olist_order_items_dataset':'../Data/OLIST/olist_order_items_dataset.csv', 
    'olist_order_payments_dataset':'../Data/OLIST/olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset':'../Data/OLIST/olist_order_reviews_dataset.csv', 
    'olist_orders_dataset':'../Data/OLIST/olist_orders_dataset.csv', 
    'olist_products_dataset':'../Data/OLIST/olist_products_dataset.csv', 
    'olist_sellers_dataset':'../Data/OLIST/olist_sellers_dataset.csv', 
    'product_category_name_translation':'../Data/OLIST/product_category_name_translation.csv'
}

for table_name,data_path in csv_files.items():
    df=pd.read_csv(data_path)
    df.to_sql(table_name,engine,if_exists='replace',index=False)
    print(f'Table {table_name} created and imported successfully')

engine.dispose()