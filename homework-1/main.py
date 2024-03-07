"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from utils import read_csv

csv_employees = read_csv('north_data/employees_data.csv')
csv_customers = read_csv('north_data/customers_data.csv')
csv_orders = read_csv('north_data/orders_data.csv')

conn_params = {
    'host': 'localhost',
    'database': 'north',
    'user': 'postgres',
    'password': '1234'
}

try:
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                'INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s)',
                csv_employees
            )
            cur.execute('SELECT * FROM employees')

        with conn.cursor() as cur:
            cur.executemany(
                'INSERT INTO customers VALUES (%s, %s, %s)', csv_customers
            )
            cur.execute('SELECT * FROM customers')

        with conn.cursor() as cur:
            cur.executemany(
                'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', csv_orders
            )
finally:
    conn.close()
