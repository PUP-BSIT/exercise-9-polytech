# Group: PolyTech | Data: Roblox Game Directory

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

def add_roblox_game():
    print("---[Add Game(s)]---")
    print("Enter the details of the game you want to add:")
    title = input("Enter Title: ")
    genre = input("Enter Genre: ")
    creator = input("Enter the name of the Creator: ")
    year = int(input("Enter year released: "))

    print("Choose Classification:")
    print("1. All Ages")
    print("2. 9+")
    print("3. 13+")
    print("4. 17+")

    classification_map = {
        "1": "All Ages",
        "2": "9+",
        "3": "13+",
        "4": "17+"
    }

    classification_choice = input("Enter choice (1-4): ")
    classification = classification_map.get(classification_choice, "All Ages") 

    roblox_game = {
        "Title": title,
        "Genre": genre,
        "Creator": creator,
        "Year": year,
        "Game Classification": classification
    }

    roblox.append(roblox_game)

    print(f"'{title}' has been added to the game list with ID {len(roblox)}.") 

def update_roblox_game():
    print("-----[Update Roblox Game]-----")
    title_input = input("Enter the Game Title you want to update: ").lower()

    for index, game in enumerate(roblox):
        if game["Title"].lower() == title_input:
            title = input("Enter new Title: ")
            genre = input("Enter new Genre: ")
            creator = input("Enter new Creator: ")
            year = int(input("Enter new Year: "))

            print("Choose New Classification:")
            print("1. All Ages")
            print("2. 9+")
            print("3. 13+")
            print("4. 17+")

            classification_map = {
                "1": "All Ages",
                "2": "9+",
                "3": "13+",
                "4": "17+"
            }

            classification_choice = input("Enter choice (1-4): ")
            classification = classification_map.get(
                classification_choice, "All Ages"
            )

            roblox[index] = {
                "Title": title,
                "Genre": genre,
                "Creator": creator,
                "Year": year,
                "Game Classification": classification
            }

            print(f"'{title}' has been successfully updated.")
            return

    print("Roblox Game title not found.")

def delete_roblox_game():
    print("-----[Delete Game]-----")
    title_input = input("Enter game title to delete: ").lower()
    for index, game in enumerate(roblox):
        if game["Title"].lower() == title_input:
            deleted = roblox.pop(index)
            print(f"'{deleted['Title']}' has been deleted.")
            return
    print("Roblox Game title not found.")

def search_roblox_game():
    search_title = input("\nEnter title to search: ").lower()
    print("-----[Search Roblox Game]-----")
    for index, game in enumerate(roblox, 1):
        if search_title in game["Title"].strip().lower():
            print(f"\nMatch found in Game ID {index}:")
            for key, value in game.items():
                print(f"{key}: {value}")
            break
    else:
        print("No matching game found.")

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
                list_roblox_games(roblox)
            case 2:
                add_roblox_game()
            case 3:
                update_roblox_game()
            case 4:
                delete_roblox_game()
            case 5:
                search_roblox_game()
            case 6:
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again")

main_menu()