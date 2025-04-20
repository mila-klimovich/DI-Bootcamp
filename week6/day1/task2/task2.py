import psycopg2

DB_NAME = "Hollywood"
USER = "postgres" 
PASSWORD = "DevIns123" 
HOST = "localhost"
PORT = "5432" # or 5433

connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME, port=PORT)
cursor = connection.cursor()

query = "SELECT * FROM actors LIMIT 20;"

cursor.execute(query)
results = cursor.fetchall()

for item in results:
        print(item)

connection.close()

# def create_table(oscars: str): 
#     """create new table with id, num"""

#     query = f'''
#     create table {oscars}(
#         id serial primary key,
#         num integer not null
#     );
#     '''
#     cursor.execute(query) # execute the query
#     connection.commit() # make changes in the database