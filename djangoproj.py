import psycopg2
from DjangoConfig import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password=password,
        database = db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM public."OnlineMarket"'
        )
        print(cursor.fetchone())
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")