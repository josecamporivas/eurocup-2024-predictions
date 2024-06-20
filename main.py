from groups.groups import get_past_groups
from matches.matches import get_past_matches, get_match

def main():
    get_past_groups('past_groups_info.pkl')

    get_past_matches('past_matches.csv')

    df_actual_eurocup_matches = get_match(2024)
    df_actual_eurocup_matches.to_csv('actual_eurocup_matches.csv', index=False)

if __name__ == '__main__':
    main()