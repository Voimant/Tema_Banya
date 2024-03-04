import psycopg2


with psycopg2.connect(database="base_numbers", user="root", password="fm6lxodIxCfY0VGU") as conn:
    with conn.cursor() as cur:


        def create_db():
            """
            Функция, создающая структуру БД (таблицы)
            :return: База данных создана
            """
            cur.execute("""
                CREATE TABLE IF NOT EXISTS numbers(
                    id SERIAL PRIMARY KEY,
                    phone_number TEXT NOT NULL);""")
            return 'База данных создана'

        def delete_db():
            """
            Функция, удаляющая таблицы базы данных
            :return: БД удалена
            """
            cur.execute("""
            DROP TABLE numbers;""")
            return 'БД удалена'

        #print(create_db())
        conn.commit()
