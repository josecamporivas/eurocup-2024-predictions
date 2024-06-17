import pandas as pd
from bs4 import BeautifulSoup
import requests
from string import ascii_uppercase
import pickle

EUROCUP_YEARS = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
BASE_URL = 'https://en.wikipedia.org/wiki/UEFA_Euro_'
EUROCUP_YEARS_AND_TABLES = [
    {
        'year': 1980,
        'tables': [7, 14]
    },
    {
        'year': 1984,
        'tables': [6, 13]
    },
    {
        'year': 1988,
        'tables': [9, 16]
    },
    {
        'year': 1992,
        'tables': [10, 17]
    },
    {
        'year': 1996,
        'tables': [10, 17, 24, 31]
    },
    {
        'year': 2000,
        'tables': [15, 22, 29, 36]
    },
    {
        'year': 2004,
        'tables': [16, 23, 30, 37]
    },
    {
        'year': 2008,
        'tables': [16, 23, 30, 37]
    },
    {
        'year': 2012,
        'tables': [19, 26, 33, 40]
    },
    {
        'year': 2016,
        'tables': [19, 26, 33, 40, 47, 54]
    },
    {
        'year': 2020,
        'tables': [22, 29, 36, 43, 50, 57]
    }
]

def get_past_groups():
    print('Getting past groups info...')

    past_group_info = []
    for eurocup_info in EUROCUP_YEARS_AND_TABLES:
        group_info = {}
        year = eurocup_info['year']
        tables = eurocup_info['tables']

        group_info['year'] = year
        all_tables = pd.read_html(BASE_URL + str(year))

        group_info['tables'] = [] 
        for letter, table in zip(ascii_uppercase, tables):
            table_info = {}
            table_info['name'] = 'Group ' + letter
            
            df = all_tables[table]
            df.pop('Qualification')
            table_info['info'] = df
            
            group_info['tables'].append(table_info)
    
        past_group_info.append(group_info)
    
    with open('past_groups_info.pkl', 'wb') as f:
        pickle.dump(past_group_info, f)
    
    print('Past groups info saved in past_groups_info.pkl')


def main():
    get_past_groups()

if __name__ == '__main__':
    main()