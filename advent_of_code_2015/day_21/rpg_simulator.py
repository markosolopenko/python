from itertools import combinations


weapons = [["Dagger", 8, 4, 0],
           ["Shortsword", 10, 5, 0],
           ["Warhammer", 25, 6, 0],
           ["Longsword", 40, 7, 0],
           ["Greataxe", 74, 8, 0]]

armors = [["Leather", 13, 0, 1],
          ["Chainmail", 31, 0, 2],
          ["Splintmail", 53, 0, 3],
          ["Bandedmail", 75, 0, 4],
          ["Platemail", 102, 0, 5]]

rings = [["Damage +1", 25, 1, 0],
         ["Damage +2", 50, 2, 0],
         ["Damage +3", 100, 3, 0],
         ["Defense +1", 20, 0, 1],
         ["Defense +2", 40, 0, 2],
         ["Defense +3", 80, 0, 3]]

boss = {'Hit Points': 103, 'Damage': 9, 'Armor': 2}
player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}


def parse_items():
    global boss
    global player
    timing = 0
    money_wasted = 0
    wins_money_wasted = []
    for weapon in weapons:
        for armor in armors:
            if timing == 0:
                money_wasted = weapon[1] + armor[1]
                player['Damage'] = weapon[2]
                player['Armor'] = armor[3]
                res_of_fight = fight(boss, player)
                timing = 1
                if res_of_fight == 'player':
                    wins_money_wasted.append(money_wasted)

            for ring in rings:
                player['Damage'] = weapon[2]
                player['Armor'] = armor[3]
                money_wasted = weapon[1] + armor[1] + ring[1]
                if ring <= 2:
                    player['Damage'] = player['Damage'] + ring[2]
                else:
                    player['Armor'] = player['Armor'] + ring[3]
                res_of_fight = fight(boss, player)
                timing = 1
                if res_of_fight == 'player':
                    wins_money_wasted.append(money_wasted)
    print(wins_money_wasted)


def fight(boss_items, player_items):
    is_alive = True
    winner = ''
    while is_alive:
        if player_items['Hit Points'] == 0:
            winner = 'player'
            is_alive = False
        elif boss_items['Hit Points'] == 0:
            winner = 'boss'
            is_alive = False
        else:
            if boss_items['Damage'] < player_items['Armor']:
                player_items['Hit Points'] -= 1
            elif player_items['Damage'] < boss_items['Armor']:
                boss_items['Hit Points'] -= 1
            else:
                player_items['Hit Points'] -= (boss_items['Damage'] - player_items['Armor'])
                boss_items['Hit Points'] -= (player_items['Damage'] - boss_items['Armor'])
    return winner


if __name__ == '__main__':
    parse_items()