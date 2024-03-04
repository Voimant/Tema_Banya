from db_func import add_user
from db_main import conn
import pandas as pd
from pprint import pprint



def search_delo(path_exl):
    df = pd.read_csv(path_exl)
    y = df.to_dict()
    my_list = []
    d_key = y['number@c.us']
    for x in d_key.values():
        my_list.append(x)
   # pprint(my_list)
    for x in my_list:
        add_user(x)
        conn.commit()
   # print(len(my_list))


path = 'new_contacts (2).csv'

#search_delo(path)
