def valid(s):
    """
    TODO: UNDERSTAND THE SOLUTION!!!
    :param s:
    :return:
    """
    # amount_of_teams = ""
    # resalt = ""
    # a = 0
    # for character in s:
    #     if character == ":":
    #         a = 1
    #         continue
    #     amount_of_teams += character
    #     if character == ",":
    #         a += 1
    #         resalt += amount_of_teams
    #         amount_of_teams = ''
    # return str(a) + ":" + resalt
    teams = s.split(':')

    print(teams)

    team_to_names = {}

    for idx in range(len(teams) - 1):
        team_name = teams[idx][-1]
        team = teams[idx + 1][:-1]
        team_to_names[team_name] = team

    size = 0
    teams = []

    for team_name, members in team_to_names.items():
        if len(members.split(',')) >= 2:
            size += 1
            teams.append(members)

    return f'{size}:{",".join([team for team in teams])}'






if __name__ == "__main__":
    print(valid("W:John,John,John,JohnC:Danger,Man"))