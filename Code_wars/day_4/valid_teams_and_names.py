def valid(s):
    amount_of_teams = ""
    resalt = ""
    a = 0
    for character in s:
        if character == ":":
            a = 1
            continue
        amount_of_teams += character
        if character == ",":
            a += 1
            resalt += amount_of_teams
            amount_of_teams = ''
    return str(a) + ":" + resalt


if __name__ == "__main__":
    print(valid("A:Stefan,Milica,Zvonimir,AndrewH:Richard"))