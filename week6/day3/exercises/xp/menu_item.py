import psycopg2

DB_NAME = "Hollywood"
USER = "postgres" 
PASSWORD = "DevIns123" 
HOST = "localhost"
PORT = "5432"

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        with psycopg2.connect(dbname="restaurant", user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)
                """, (self.name, self.price))

    def delete(self):
        with psycopg2.connect(dbname="restaurant", user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM Menu_Items WHERE item_name = %s
                """, (self.name,))

    def update(self, new_name, new_price):
        with psycopg2.connect(dbname="restaurant", user=USER, password=PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s
                """, (new_name, new_price, self.name))
                self.name = new_name
                self.price = new_price


