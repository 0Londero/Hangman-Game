def art():
    print(r"""

  _    _                                            _____                      
 | |  | |                                          / ____|                     
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |  __  __ _ _ __ ___   ___ 
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | | |_ |/ _` | '_ ` _ \ / _ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | | | |__| | (_| | | | | | |  __/
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \_____|\__,_|_| |_| |_|\___|
                      __/ |                                                     
                     |___/                                                      
            
                                      _______
                                     |/      |
                                     |      (_)
                                     |      \|/
                                     |       |
                                     |      / \
                                     |
                                  ___|___ 
    """)


# Menu
def menu():
    print("\n__ HANGMAN GAME MENU __")
    print("1. Play Game")
    print("2. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid choice! Please enter 1 or 2.")