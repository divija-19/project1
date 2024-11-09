def start_game():
    print("Welcome to the adventure game!")
    name = input("Enter your name to proceed: ")
    age = int(input("Enter your age, lil bro: "))
    print("-----------------")
    choice = input("Which direction do you want to go? (left/right): ")  
    
    if choice == "left":
        forest_path()
    elif choice == "right":
        river_path()
    else:
        print("Incorrect entry. Can you not read or something? Choose again from left/right.")
        start_game() 

def forest_path():
    print("You enter a forest and hear strange noises.")
    forest_choice = input("What do you do? (go home/go hear that noise (like you're in a horror movie)): ")
    
    if forest_choice == "go home" or forest_choice == "go home ":
        print("Haha, loser!")
        end_game()
    elif forest_choice == "go hear that noise":
        print("Well, someone wants to rizz up that girl.")
        forest_choice2 = input("You see a bear! What do you do? (run/act dead): ")

        if forest_choice2 == "run" or forest_choice2 == "run ":
            print("Bruh, who do you think you are? You're dead, homie. Bye!")
            end_game()
        elif forest_choice2 == "act dead" or forest_choice2 == "act dead ":
            print("Someone read that story!")
            forest_choice3 = input("You see a chest! Wanna open it? (yes/no): ")
            
            if forest_choice3 == "yes" or forest_choice3 == "yes ":
                print("You won a little cash. In this economy, you should be grateful!")
                end_game()
            elif forest_choice3 == "no" or forest_choice3 == "no ":
                print("Then what are you here for? Bye bye!")
                end_game()
            else:
                print("CAN YOU READ? START AGAIN")
                forest_path()  
        else:
            print("Invalid choice!")
            forest_path()  
    else:
        print("Invalid choice!")
        forest_path()  

def river_path():
    print("First of all, why?")
    river_choice1 = input("How do you want to cross the river? (bridge/boat): ")
    
    if river_choice1 == "boat":
        print("Bruh, there was a crocodile in the river. You're dead. Haha!")
        end_game()
    elif river_choice1 == "bridge":
        print("Well, someone wants to do cardio. It's a long bridge, dude.")
        print("One eternity later~")
        river_choice2 = input("Well, IDK bruh, but you win. (Press Enter to continue)")
        end_game()
    else:
        print("CAN YOU READ? GO AGAIN")
        river_path() 

def end_game():
    print("Game Ended, bye bye!")

start_game()
