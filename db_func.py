from db_main import conn


def add_user(phone_number: str):
    """
    Функция, позволяющая добавить новый номер в таблицу numbers
    :param phone_number: номер телефон WA формат
    """
    with conn.cursor() as cur:
        cur.execute("""
                        INSERT INTO numbers (phone_number)
                        VALUES (%s);""", (phone_number,))
        return 'Номер внесен'


#print(add_user('89194712977'))
conn.commit()


def search_user():
    """
    Функция, которая проверяет по user_name есть ли такой пользователь в базе
    :param user_name: имя пользователя
    :return: имя пользователя либо None
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT phone_number FROM numbers;""")
        list_1 = []
        for i in cur.fetchall():
            for item in i:
                list_1.append(item)
        return list_1

#print(search_user())


'79257182701@c.us'
