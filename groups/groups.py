import pandas as pd
import pickle
from string import ascii_uppercase
from resources.constants import BASE_URL, CURRENT_EUROCUP_GROUPS

def get_group(year, tables) -> dict:
    print(f'Getting groups info for {year}...')
    all_tables = pd.read_html(BASE_URL + str(year))
 
    group_info = {}
    for letter, table in zip(ascii_uppercase, tables):
        table_info = all_tables[table]
        table_info.rename(columns={table_info.columns[1]:'Team'}, inplace=True)
        table_info['Team'] = table_info['Team'].str.replace(' \\([a-zA-Z]\\)', '', regex=True)
        table_info.pop('Qualification')

        group_info[f'Group {letter}'] = table_info
    
    return group_info

def get_current_groups(filename) -> dict:
    group_info = get_group(CURRENT_EUROCUP_GROUPS['year'], CURRENT_EUROCUP_GROUPS['tables'])

    pickle.dump(group_info, open(filename, 'wb'))