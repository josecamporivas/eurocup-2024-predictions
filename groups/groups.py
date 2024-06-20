import pandas as pd
import pickle
from string import ascii_uppercase
from resources.constants import BASE_URL, EUROCUP_YEARS_AND_TABLES

def get_past_groups(file_name) -> None:
    print('Getting past groups info...')

    past_group_info = []
    for eurocup_info in EUROCUP_YEARS_AND_TABLES:
        year = eurocup_info['year']
        tables = eurocup_info['tables']

        group_info = get_group(year, tables)
    
        past_group_info.append(group_info)
    
    with open(file_name, 'wb') as f:
        pickle.dump(past_group_info, f)
    
    print(f'Past groups info saved in {file_name}')

def get_group(year, tables) -> dict:
    print(f'Getting groups info for {year}...')
    group_info = {}
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
    
    return group_info