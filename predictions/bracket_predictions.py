import pandas as pd
from predictions.match_prediction import predict_points

def get_bracket_prediction(team_strength, df_previuos_round, match_number_start, match_number_end):
    df_fixture = pd.read_csv('current_eurocup_matches.csv')
    df_round = df_fixture[match_number_start:match_number_end].copy()  # Parametrize this

    df_round = add_winner_column(df_previuos_round, df_round)

    for index, row in df_round.iterrows():
        home, away = row['home'], row['away']
        points_home, points_away = predict_points(team_strength, home, away)
        if points_home > points_away:
            winner = home
        else:
            winner = away
        df_round.loc[index, 'winner'] = winner
    return df_round

def add_winner_column(df_previuos_round, df_round):
    for index, row in df_previuos_round.iterrows():
        winner = df_previuos_round.loc[index, 'winner']
        match = df_previuos_round.loc[index, 'score']
        df_round.replace({f'Winner {match}':winner}, inplace=True)
    df_round['winner'] = '?'
    return df_round