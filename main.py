
# Search cell for useful object
def option2():
    print("You struggle to your feet to search the room.")

    print ("a = pull loose stone from wall")
    print ( "b = find a nail to pick the lock")
    opt2 = input(" Do you want to pull loose stone from wall or find a nail to pick the lock? ")
    
    if opt2 == "a" :
        print (" You pull hard on the stone, your feet scrambling for grip on the hard stone")
        print("Floor, the stone breaks free and sends you tumbling back. ")
        print("The hole reveals you are in a very high turret, towering above the town below")
        print(" from the giant hill it sits on. You see no clear route to escape")
        option2()

    elif opt2 == "b":
        print(" You struggle with the rusty lock but quickly and silently manage to disengage it. ")
        print("  After picking the lock, you slowly open the door and creep out of the dungeon.")
        print(" A long and winding staircase takes you to the bottom of the turret to another wooden arched door.")
        
#option 1: force cell door

def option1():
    print("The screams get louder and closer")
    print("OH! NO! its a really big monster")
    print("ITS HURTS! SOMEONE HELP ME!")
    print("game over")
    playagain = input (" Whould you like to play again? yes or no ")
    if playagain == "NO" or playagain == "no":
        print ("Goodbye")
    elif playagain == "YES" or playagain == "yes":
        intro()

### Players first decison : game starts here
def intro():
    print("You wake up on a cold stone floor.")
    print("Moonlight creeping through an iron barred window reveals skeletons chained to the walls.")
    print(" The room is small and round with one arched door.")
    print("You hear a voice fill the room")
    print("In fear you reply")
    name = input("What is your name: ")
    print()
    print()
    print(name + "! HOPE YOU SLEPT WELL!!!!!")
    print("     ######################")
    print("     |                    |")
    print("     |     HAHAHAHAHA     |")
    print("     |     HAHAHAHAHA     |")
    print("     |     HAHAHAHAHA     |")
    print("     |                    |")
    print("     ######################")
    startgame = input("Would you like to start the game? (Y?N): ")
    if startgame == "n" or startgame == "N":
        print ("Maybe some other time. Bye for now...")
    elif startgame == "y" or startgame == "Y":
        print("Welcome to hells's doom!")
        Choice()

#Escape prision tower
def Choice():
    print("a = Force the door")
    print("b  = Search the room")
    print("c = Go back to sleep")
    start = input("What would you like to do?").lower()
    if start == "a" :
        print("You stand up, shaking from the realisation that you have been captured and run at the door.")
        print("BANG. The door doesn’t budge but creates an almighty noise that bounces through")
        print("the castle. You hear a scream like you have never heard before...")
        print("What is this monster…. ")
        print("The screams get louder and closer")
        intro()


    elif start == "b":
        option2()
        
    elif start == "c":
        print("Go back to sleep and have a nice dream OR MAYBE!!!!!!")
        print("     ######################")
        print("     |                    |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |                    |")
        print("     ######################")
### Start Game - Enter name 



#Main function
intro()
# def optionx():
            # print("The screams get louder and closer")
            # print("OH! NO! its a really big monster")
            # print("ITS HURTS! SOMEONE HELP ME!")
            # print("game over")
            # playagain = input (" Whould you like to play again? ")
            # if playagain == "NO" or "no":
            #     #print (Goodbye)
            # elif playagain == "YES" or "yes":
            #     intro()

