football_league = [[None for _ in range(10)] for _ in range(10)]

for team in range(10):
    print(f"Ingrese los resultados del equipo {team}")
    for rival_team in range(10):
        if rival_team != team:
            if football_league[team][rival_team] is not None:
                print(f"Ingrese el resultado del {team} vs {rival_team}")
                team_goals = int(input(f"Goles del {team}: "))
                rival_goals = int(input(f"Goles del {rival_team}: "))
                football_league[team][rival_team] = team_goals
                football_league[rival_team][team] = rival_goals
        else:
            football_league[team][rival_team] = 0