from scipy.stats import poisson

def predict_points(team_strength, home, away):
    if home in team_strength.index and away in team_strength.index:
        # goals_scored * goals_conceded
        lamb_home = team_strength.at[home,'GoalsScored'] * team_strength.at[away,'GoalsConceded']
        lamb_away = team_strength.at[away,'GoalsScored'] * team_strength.at[home,'GoalsConceded']
        prob_home, prob_away, prob_draw = 0, 0, 0

        for x in range(0,11): #number of goals home team
            for y in range(0, 11): #number of goals away team
                p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p
        
        points_home = 3 * prob_home + prob_draw
        points_away = 3 * prob_away + prob_draw
        return (points_home, points_away)
    else:
        return (0, 0)