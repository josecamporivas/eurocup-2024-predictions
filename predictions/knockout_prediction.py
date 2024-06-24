import pandas as pd
from predictions.match_prediction import predict_points

def get_knockout_prediction(team_strength, dict_table):
    df_fixture = pd.read_csv('current_eurocup_matches.csv')
    df_fixture_knockout = df_fixture[36:44].copy()
    add_winner_column(df_fixture_knockout, dict_table)

    for index, row in df_fixture_knockout.iterrows():
        home, away = row['home'], row['away']
        points_home, points_away = predict_points(team_strength, home, away)
        if points_home > points_away:
            winner = home
        else:
            winner = away
        df_fixture_knockout.loc[index, 'winner'] = winner
    return df_fixture_knockout


def add_winner_column(df_fixture_knockout, dict_table):
    for group in dict_table:
        group_winner = dict_table[group].loc[0, 'Team']
        runners_up = dict_table[group].loc[1, 'Team']
        df_fixture_knockout.replace({f'Winner {group}':group_winner,
                                    f'Runner-up {group}':runners_up}, inplace=True)

    df_fixture_knockout['winner'] = '?'

    third_place_teams = []

    for group in dict_table.values():
        third_place_teams.append(group.iloc[2])
    
    df_third_place = pd.DataFrame(third_place_teams)

    df_third_place_sorted = df_third_place.sort_values(by='Pts', ascending=False)
    top_third_place_teams = df_third_place_sorted.head(4)

    third_place_teams = top_third_place_teams['Team'].values

    df_fixture_knockout.loc[df_fixture_knockout['away'] == '3rd Group D/E/F', 'away'] = third_place_teams[0]
    df_fixture_knockout.loc[df_fixture_knockout['away'] == '3rd Group A/D/E/F', 'away'] = third_place_teams[1]
    df_fixture_knockout.loc[df_fixture_knockout['away'] == '3rd Group A/B/C', 'away'] = third_place_teams[2]
    df_fixture_knockout.loc[df_fixture_knockout['away'] == '3rd Group A/B/C/D', 'away'] = third_place_teams[3]
