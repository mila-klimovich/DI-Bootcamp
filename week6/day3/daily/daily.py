import requests
import random
import psycopg2

DB_NAME = "public"
USER = "postgres" 
PASSWORD = "DevIns123" 
HOST = "localhost"
PORT = "5432"

def fetch_random_countries(count=10):
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()
    return random.sample(countries, count)

def insert_country_data(countries):
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as conn:
        with conn.cursor() as cur:
            for country in countries:
                name = country.get("name", {}).get("common", "N/A")
                capital = country.get("capital", ["N/A"])[0]
                flag = country.get("flags", {}).get("png", "N/A")
                subregion = country.get("subregion", "N/A")
                population = country.get("population", 0)

                cur.execute("""
                    INSERT INTO countries (name, capital, flag, subregion, population)
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, capital, flag, subregion, population))

    print("Countries added successfully!")

def fetch_all_countries():
    with psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM countries")
            rows = cur.fetchall()
            for row in rows:
                print(row)

if __name__ == "__main__":
    random_countries = fetch_random_countries()
    insert_country_data(random_countries)
    fetch_all_countries()