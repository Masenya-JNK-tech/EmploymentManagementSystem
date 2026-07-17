import psycopg2

def connect_database():

    connection = psycopg2.connect(
        host="localhost",
        database="database_name",
        user="your_username",
        password="password",
        port="5432"
    )

    return connection
