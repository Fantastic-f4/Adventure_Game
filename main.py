
def intro():
    print("a = Force the door")
    print("b  = Search the room")
    print("c = Go back to sleep")
    start = input("Would you like to go back to sleep, search the room or force the door?  ").lower()



    if start == "a" :
        print("You stand up, shaking from the realisation that you have been captured and run at the door.")
        print(" BANG. The door doesn’t budge but creates an almighty noise that bounces through")
        print("the castle. You hear a scream like you have never heard before...")
        print("What is this monster…. ")
        option1()
        

    elif start == "b":
        print("You struggle to your feet to search the room, horrified by what you see,")
        print(" you closer inspect the skeleton. You pick up the hand shackles from one of the")
        print(" skeleton and the arm breaks clean off. CRACK. This startles you but reveals an ")
        print("iron shackle pin that you can use to pick the lock. After picking the lock,")
        print(" you slowly open the door and creep out of the dungeon.")
        print("A long and winding staircase takes you to the bottom of the turret to another wooden arched door")
        
    elif start == "c":
        print("Go back to sleep and have a nice dream OR MAYBE!!!!!!")
        print("     ######################")
        print("     |                    |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |                    |")
        print("     ######################")

        def option1():
            print("The screams get louder and closer")
            print("OH! NO! its a really big monster")
            print("ITS HURTS! SOMEONE HELP ME!")
            print("game over")
            playagain = input (" Whould you like to play again? ")
            if playagain == "NO" or "no":
                print (Goodbye)
            elif playagain == "YES" or "yes":
                intro()


#Main Function


print("You wake up on a cold stone floor.")
print( "Moonlight creeping through an iron barred window reveals skeletons chained to the walls.")
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
    intro()


    



