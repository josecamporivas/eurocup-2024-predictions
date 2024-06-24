from groups.groups import get_current_groups
from matches.matches import get_past_matches, get_match, format_score
from predictions.team_strength import get_team_strength
from predictions.group_stage_prediction import get_group_stage_prediction
from predictions.knockout_prediction import get_knockout_prediction
from predictions.bracket_predictions import get_bracket_prediction
import pickle

def main():
    print('Get current groups')
    get_current_groups('current_groups_info.pkl')

    print('Get past matches')
    get_past_matches('past_matches.csv')

    print('Get current matches')
    df_current_eurocup_matches = get_match(2024)
    df_current_eurocup_matches.to_csv('current_eurocup_matches.csv', index=False)

    print('Format score')
    format_score('past_matches.csv')

    print('Calculating team strength')
    team_strength = get_team_strength('past_matches.csv')

    print('Predicting group stage')
    current_groups_info = pickle.load(open('current_groups_info.pkl', 'rb'))
    current_groups_info = get_group_stage_prediction(team_strength, current_groups_info)

    print('Predicting knockout stage')
    knockout_result = get_knockout_prediction(team_strength, current_groups_info)
    
    print('Predicting quarter stage')
    quarter_result = get_bracket_prediction(team_strength, knockout_result, 44, 48)

    print('Predicting semifinal stage')
    semifinal_result = get_bracket_prediction(team_strength, quarter_result, 48, 50)

    print('Predicting final stage')
    final_result = get_bracket_prediction(team_strength, semifinal_result, 50, 51)

    print('\nFinal result...')
    print(f'{final_result.iloc[0]['winner']} vs {final_result.iloc[0]["away"]} - and the winner is {final_result.iloc[0]["winner"]}!')

if __name__ == '__main__':
    main()
