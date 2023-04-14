import pandas as pd
import time
from utilities import *

start = time.perf_counter()

#########################
### PRODUCTS DATA #######
#########################
product_df = pd.read_csv('products.csv');

# check for null values
product_nulls = count_null(product_df)

# pad null values, if exists
if product_nulls['sum'] != 0:
    product_df = pad_null(product_df)

# format product_cost and product_price
product_df = product_df.replace({'Product_Cost': r'[$]'},{'Product_Cost': r''}, regex=True)
product_df = product_df.replace({'Product_Price': r'[$]'},{'Product_Price': r''}, regex=True)
product_df = product_df.astype({'Product_Cost': 'float'})
product_df = product_df.astype({'Product_Price': 'float'})

# rename columns
product_df = product_df.rename(columns=
                               {'Product_ID':'id',
                                'Product_Name':'product_name',
                                'Product_Category':'product_category',
                                'Product_Cost':'product_cost',
                                'Product_Price':'product_price'})

#########################
### STORES DATA #########
#########################
stores_df = pd.read_csv('stores.csv');

# check for null values
store_nulls = count_null(stores_df)

# pad null values, if exists
if store_nulls['sum'] != 0:
    stores_df = pad_null(stores_df)

# rename columns
stores_df = stores_df.rename(columns={'Store_ID':'id',
                                      'Store_Name':'store_name',
                                      'Store_City':'store_city',
                                      'Store_Location':'store_location',
                                      'Store_Open_Date':'store_open_date'})

#########################
### SALES DATA ##########
#########################
sales_df = pd.read_csv('sales.csv');

# check for null values
sales_nulls = count_null(sales_df)

# pad null values, if exists
if sales_nulls['sum'] != 0:
    stores_df = pad_null(sales_df)

# rename columns
sales_df = sales_df.rename(columns={'Sale_ID':'id',
                                    'Date':'sale_date',
                                    'Store_ID':'store_id',
                                    'Product_ID':'product_id',
                                    'Units':'units'})

#########################
### INVENTORY DATA ######
#########################
inventory_df = pd.read_csv('inventory.csv');

# check for null values
inventory_nulls = count_null(inventory_df)

# pad null values, if exists
if inventory_nulls['sum'] != 0:
    inventory_df = pad_null(inventory_df)
    
# rename columns
inventory_df = inventory_df.rename(columns={'Store_ID':'store_id',
                                            'Product_ID':'product_id',
                                            'Stock_On_Hand':'stock_on_hand'})

end = time.perf_counter() - start