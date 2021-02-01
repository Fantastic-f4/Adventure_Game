import time
import sys
import random

a = 2
b = 0.2
c = 0.08


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
        
    s1 = input ( "Run and barge the door (1)/Silently open the door and creep in (2)")
# forcefully open the door
        if s1 == 1:
            print("The door forcefully opens, Woman turns into vampire and kills you")
            option2()
#slowly open the door
        elif s1 == 2:
            print("As you open the door, you see a beautiful woman walking down a corridor to the right")
            print("You run and barge the door and run straight into another dark stone room. ")
            print(" A woman in the distance turns round and as you blink, you hear a scream. ")
            print("You feel warm liquid running down your neck and as you open your eyes, you see a horrible creature as you take you last breath.")
            print("As you watch the woman walk down the corridor, she disappears.")
            s2 = input("Sneak after the woman (1)/ Explore the room (2)")

#sneak after the woman
            if s2 == 1:
                opt2_1()
            if s2 == 2:
                opt2_2()
def opt2_1():
    print ("You follow the corridor to where the woman disappeared and find two doors")
    print("As you reach the end of the corridor you are faced with two giant doors,")
    print("one of the doors stained red with blood, the other frozen ice white. ")

# search the room
def opt2_2():
    print("Do you want to take the risk? Roll a 6 to teleport home  or leave the orb ")




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
    time.sleep(t1)
    print("Moonlight creeping through an iron barred window reveals skeletons chained to the walls.")
    time.sleep(t1)
    print(" The room is small and round with one arched door.")
    time.sleep(t1)
    print("You hear a voice fill the room")
    time.sleep(t1)
    print("In fear you reply")
    time.sleep(t1)
    name = input("What is your name: ")
    time.sleep(t1)
    print()
    print()
    print(name + "! HOPE YOU SLEPT WELL!!!!!")
    time.sleep(time1)
    print("     ######################")
    print("     |                    |")
    print("     |     HAHAHAHAHA     |")
    time.sleep(time3)
    print("     |     HAHAHAHAHA     |")
    time.sleep(time3)
    print("     |     HAHAHAHAHA     |")
    time.sleep(time3)
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

