import pandas as pd
import pickle
from scipy.stats import poisson


def get_team_strength(filename_past_matches):
    df_historical_data = pd.read_csv(filename_past_matches)

    df_home = df_historical_data[['home', 'home_score', 'away_score']]
    df_away = df_historical_data[['away', 'home_score', 'away_score']]

    df_home = df_home.rename(columns={'home':'Team', 'home_score': 'GoalsScored', 'away_score': 'GoalsConceded'})
    df_away = df_away.rename(columns={'away':'Team', 'home_score': 'GoalsConceded', 'away_score': 'GoalsScored'})

    df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby('Team').mean()
    return df_team_strength

