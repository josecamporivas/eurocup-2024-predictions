import pandas as pd
import pickle
from predictions.match_prediction import predict_points

def get_group_stage_prediction(team_strength, dict_table):
    df_fixture = pd.read_csv('current_eurocup_matches.csv')
    df_fixture_group_36 = df_fixture[:36].copy()

    """ dict_table = pickle.load(open('current_groups_info.pkl', 'rb')) """

    for group in dict_table:
        dict_table[group]['Pts'] = 0.0
        teams_in_group = dict_table[group]['Team'].values
        df_fixture_group_6 = df_fixture_group_36[df_fixture_group_36['home'].isin(teams_in_group)]
        for index, row in df_fixture_group_6.iterrows():
            home, away = row['home'], row['away']
            points_home, points_away = predict_points(team_strength, home, away)
            dict_table[group].loc[dict_table[group]['Team'] == home, 'Pts'] += points_home
            dict_table[group].loc[dict_table[group]['Team'] == away, 'Pts'] += points_away

        dict_table[group] = dict_table[group].sort_values('Pts', ascending=False).reset_index()
        dict_table[group] = dict_table[group][['Team', 'Pts']]
        dict_table[group] = dict_table[group].round(0)
    
    return dict_table
