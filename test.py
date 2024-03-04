import pandas as pd
from pprint import pprint

def get_list(path):
    data = pd.read_csv(path, header=0)

    col = data['number'].tolist()
    return col
#pprint(col)


def get_txt(number):
    with open('number.txt', 'a') as f:
        f.writelines(number + '\n')





    #get_txt(x)
