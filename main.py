import random

def load_args(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def assign_heroes(players, heroes, n):
    assigned = {}
    for player in players:
        assigned[player] = []
        for _ in range(n):
            if heroes:
                hero = random.choice(heroes)
                assigned[player].append(hero)
                heroes.remove(hero)
            else:
                print("Not enough heroes to assign.")
                break
    return assigned

def assign_equipments(assignments, equipments):
    for player in assignments:
        for i in range(6):
            equipment = random.choice(equipments)
            while equipment in assignments[player]:
                equipment = random.choice(equipments)
            assignments[player].append(equipment)


def one_more_equipment(assignments, equipments, player):
    if player in assignments:
        # Assign new equipments
        new_equipment = random.choice(equipments)
        equipments.remove(new_equipment)
        assignments[player].append(new_equipment)
    else:
        print(f"Player {player} not found!")

def display_assignments(assignments):
    for player, heroes in assignments.items():
        print(f"{player}: {', '.join(heroes)}")

def reassign_hero(assignments, heroes, player):
    if player in assignments:
        # Return the current heroes to the pool
        heroes.extend(assignments[player])
        # Assign new heroes
        new_heroes = []
        for _ in range(len(assignments[player])):
            if heroes:
                new_hero = random.choice(heroes)
                new_heroes.append(new_hero)
                heroes.remove(new_hero)
            else:
                print("Not enough heroes to reassign.")
                break
        assignments[player] = new_heroes
    else:
        print(f"Player {player} not found!")
    
def one_more_hero(assignments, heroes, player):
    if player in assignments:
        # Assign new heroes
        if heroes:
            new_hero = random.choice(heroes)
            heroes.remove(new_hero)
        else:
            print("Not enough heroes to reassign.")
        assignments[player].append(new_hero)
    else:
        print(f"Player {player} not found!")


def print_info():
    print("input '1' to reassign heroes to a player")
    print("input '2' to add one more hero to a player")
    print("input '3' to reassign all heroes for all players")
    print("input '4' to assign equipments to all players")
    print("input '5' to assign equipments to one player")
    print("input '-1' to exit")

def print_teams(blue_assignments, red_assignments):
    print("\nBlue Team Assignments:")
    display_assignments(blue_assignments)
    print("Red Team Assignments:")
    display_assignments(red_assignments)
    
def main():
    # Load data
    heroes = load_args('Legends.txt')
    blue_players = load_args('blue.txt')
    red_players = load_args('red.txt')
    equipments = load_args('equipments.txt')

    # Number of heroes per player
    n = int(input("Enter the number of heroes per player: "))

    # Assign heroes
    blue_assignments = assign_heroes(blue_players, heroes, n)
    red_assignments = assign_heroes(red_players, heroes, n)

    # Display assignments
    print_teams(blue_assignments, red_assignments)

    print_info()
    choice=int(input("Enter your choice: "))
    while choice!=-1:
        if choice==1:
            player_name = input("Enter the name of the player to reassign all hero: ")
            if player_name in blue_players:
                reassign_hero(blue_assignments, heroes, player_name)
            else:
                reassign_hero(red_assignments, heroes, player_name)
        elif choice==2:
            player_name = input("Enter the name of the player to reassign one more heroes: ")
            if player_name in blue_players:
                one_more_hero(blue_assignments, heroes, player_name)
            else:
                one_more_hero(red_assignments, heroes, player_name)
        elif choice==3:
            blue_assignments = assign_heroes(blue_players, heroes, n)
            red_assignments = assign_heroes(red_players, heroes, n)
        elif choice==4:
            # Assign equipments
            assign_equipments(blue_assignments, equipments)
            assign_equipments(red_assignments, equipments)
        elif choice==5:
            player_name = input("Enter the name of the player to assign equipments: ")
            if player_name in blue_players:
                one_more_equipment(blue_assignments, equipments, player_name)
            else:
                one_more_equipment(red_assignments, equipments, player_name)
        else:
            continue

        print_teams(blue_assignments, red_assignments)
        print_info()
        choice=int(input("Enter your choice: "))

if __name__ == "__main__":
    main()
