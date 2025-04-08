# Group: PolyTech | Data: Roblox Game Directory

# TODO: Design Roblox game list and display functions. Assigned to: Zyra  
# TODO: Add Roblox game details from user input. Assigned to: Annie  
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
                pass
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