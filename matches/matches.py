import pandas as pd
from bs4 import BeautifulSoup
import requests
from resources.constants import BASE_URL, EUROCUP_YEARS_AND_TABLES


def get_past_matches(file_name) -> None:
    print('Getting past matches info...')
    years = map(lambda x: x['year'], EUROCUP_YEARS_AND_TABLES)

    list_df_matches = []
    for year in years:
        df = get_match(year)
        list_df_matches.append(df)

    df_matches = pd.concat(list_df_matches, ignore_index=True)
    df_matches.to_csv(file_name, index=False)
    print(f'Past matches info saved in {file_name}')


def get_match(year) -> pd.DataFrame:
    print(f'Getting matches info for {year}...')
    response = requests.get(BASE_URL + str(year))
    soup = BeautifulSoup(response.text, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home_teams = []
    scores = []
    away_teams = []

    for match in matches:
        home_teams.append(match.find('th', class_='fhome').get_text().strip())
        scores.append(match.find('th', class_='fscore').get_text().strip().replace('\u2013', '-'))
        away_teams.append(match.find('th', class_='faway').get_text().strip())

    dict_matches = {
        'home': home_teams,
        'score': scores,
        'away': away_teams
    }
    df = pd.DataFrame(dict_matches)
    df['year'] = year
    return df

def format_score(file_name) -> None:
    print('Cleaning score format...')
    df = pd.read_csv(file_name)
    
    df['score'] = df['score'].str.replace('[^\\d-]', '', regex=True)
    df[['home_score', 'away_score']] = df['score'].str.split('-', expand=True)
    df.pop('score')
    df = df.astype({'home_score': int, 'away_score': int, 'year': int})
    df.to_csv(file_name, index=False)