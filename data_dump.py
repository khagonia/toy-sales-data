import data_extract_transform as data
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
import time

start = time.perf_counter()
print('Script execution start.\n')

DB_HOST = 'localhost:5432'
DB_NAME = 'Toy Sales Data'
DB_USER = 'postgres'
DB_PASS = 'admin'

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}', echo=False)

with engine.connect() as conn:
    # query = f'INSERT INTO products (id, product_name, product_category, product_cost, product_price) VALUES\n'
 
    print('Re-initializing tables...')
    conn.execute(text("CALL initialize_tables()"))
    conn.execute(text("CALL create_views()"))
    conn.commit()
    print('Success!\n')

    print(f'Inserting {len(data.product_df.index)} rows to public.products on {DB_NAME}...')
    data.product_df.to_sql('products', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.product_df.index)} rows.\n')

    print(f'Inserting {len(data.stores_df.index)} rows to public.stores on {DB_NAME}...')
    data.stores_df.to_sql('stores', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.stores_df.index)} rows.\n')
   
    print(f'Inserting {len(data.sales_df.index)} rows to public.sales on {DB_NAME}...')
    data.sales_df.to_sql('sales', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.sales_df.index)} rows.\n')

    print(f'Inserting {len(data.inventory_df.index)} rows to public.inventory on {DB_NAME}...')
    data.inventory_df.to_sql('inventory', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.inventory_df.index)} rows.\n')

end = data.end + time.perf_counter() - start
print(f'Sucessfully executed in {end:.2f} seconds')