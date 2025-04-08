# Group: PolyTech | Data: Roblox Game Directory

# TODO: Design Roblox game list and display functions. Assigned to: Zyra  
roblox = [
    {
        "Title": "Dress to Impress",
        "Genre": "Fashion Roleplay",
        "Creator": "Gigi",
        "Year": 2023,
        "Game Classification": "9+"
    }
]

def list_roblox_games(content_list):
    if content_list:
        print("-----[List of Games]-----")
        for index, game in enumerate(content_list, 1):
            print(f"Roblox Game: {index}")
            for key, value in game.items():
                print(f"\t{key}: {value}")
            print()
    else:
        print("No content available.")

# TODO: Add Roblox game details from user input. Assigned to: Annie 
def add_roblox_game():
    print("---[Add Game(s)]---")

    # Collect game details from user input
    title = input("Enter Title: ")
    genre = input("Enter Genre: ")
    creator = input("Enter the name of the Creator: ")
    year = int(input("Enter year released: "))

    # Display classification options
    print("Choose Classification:")
    print("1. All Ages")
    print("2. 9+")
    print("3. 13+")
    print("4. 17+")

    # Mapping for classification based on user input
    classification_map = {
        "1": "All Ages",
        "2": "9+",
        "3": "13+",
        "4": "17+"
    }

    # Get the user's classification choice with default fallback
    classification_choice = input("Enter choice (1-4): ")
    classification = classification_map.get(classification_choice, "All Ages") 

    # Create dictionary for the new game
    roblox_game = {
        "Title": title,
        "Genre": genre,
        "Creator": creator,
        "Year": year,
        "Game Classification": classification
    }

    # Append the game dictionary to the roblox list
    roblox.append(roblox_game)

    # Confirm that the game was added
    print(f"'{title}' has been added to the game list with ID {len(roblox)}.") 
# TODO: Update a game using its Game ID. Assigned to: Keith  
# TODO: Delete a game by Game ID. Assigned to: Mikee  
# TODO: Search for a game by title. Assigned to: Kalelle  



def main_menu():
    while True:
        print("\n-----[Roblox Game Menu]-----")
        print("1. List Roblox Games")
        print("2. Add Roblox Games")
        print("3. Update Roblox Games")
        print("4. Delete Roblox Games")
        print("5. Search Roblox Games")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                pass
            case 2:
                add_roblox_game()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again")

main_menu()
# TODO: Run program loop to execute all features. Assigned to: Everyone