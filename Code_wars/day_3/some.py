def valid(s):
    teams = s.split(':')
    team_to_names = {}
    for idx in range(len(teams) - 1):
        team_name = teams[idx][-1]
        team = teams[idx + 1][:-1]
        team_to_names[team_name] = team
    size = 0
    teams = []
    for team_name, members in team_to_names.items():
        if len(members.split(",")) >= 2:
            size += 1
            teams.append(members)

    return f'{size}:{",".join([team for team in teams])}'

if __name__ == "__main__":
    print(valid("A:Stefan,Milica,Zvonimir,AndrewH:Richard"))