import psycopg2

DB_NAME = "Hollywood"
USER = "postgres" 
PASSWORD = "DevIns123" 
HOST = "localhost"
PORT = "5432"

import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        with psycopg2.connect(dbname="restaurant", user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (item_name,))
                result = cur.fetchone()
                if result:
                    return MenuItem(*result)
                return None

    @classmethod
    def all_items(cls):
        with psycopg2.connect(dbname="restaurant", user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT item_name, item_price FROM Menu_Items")
                results = cur.fetchall()
                return [MenuItem(name, price) for name, price in results]
