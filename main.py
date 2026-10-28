import pandas as pd
import psycopg

file = r"C:\Users\asus\.cache\kagglehub\datasets\bartoszpieniak\poland-cars-for-sale-dataset\versions\3\Car_sale_ads.csv"

all_db = pd.read_csv(file)

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="car_data_warehouse",
    user="postgres",
    password=""
)

print(all_db.iloc[0])

conn.close()

