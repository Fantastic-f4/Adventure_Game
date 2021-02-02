import time
import sys
import random

a = 1.7
b = 0.2
c = 0.08


# Search cell for useful object
def option2():
    print("You struggle to your feet to search the room.\n")

    print ("a = pull loose stone from wall\n")
    print ( "b = find a nail to pick the lock\n")
    opt2 = input(" Do you want to pull loose stone from wall or find a nail to pick the lock? \n")
    
    if opt2 == "a" :
        print (" You pull hard on the stone, your feet scrambling for grip on the hard stone\n")
        print("Floor, the stone breaks free and sends you tumbling back. \n")
        print("The hole reveals you are in a very high turret, towering above the town below\n")
        print(" from the giant hill it sits on. You see no clear route to escape\n\n")
        option2()

    elif opt2 == "b":
        print(" You struggle with the rusty lock but quickly and silently manage to disengage it.\n ")
        print("  After picking the lock, you slowly open the door and creep out of the dungeon.\n")
        print(" A long and winding staircase takes you to the bottom of the turret to another wooden arched door.\n\n")
        opt2_0()

def opt2_0():
    s1 = input ( "Run and barge the door (1)\n Silently open the door and creep in (2)")
    for cht in s1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)

# forcefully open the door
    if s1 == "1":
        s1prt = "The door forcefully opens, Woman turns into vampire and kills you"
        for cht in s1prt:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(b)
        time.sleep(1.0)

        option2()
#slowly open the door
    elif s1 == "2":
        print("As you open the door, you see a beautiful woman walking down a corridor to the right")
        print("You run and barge the door and run straight into another dark stone room. ")
        print(" A woman in the distance turns round and as you blink, you hear a scream. ")
        print("You feel warm liquid running down your neck and as you open your eyes, you see a horrible creature as you take you last breath.")
        print("As you watch the woman walk down the corridor, she disappears.")
        
        opt2_1()
#sneak after the woman
        
def opt2_1():
    s2 = input("Sneak after the woman (1)/ Explore the room (2)")
    if s2 == 1:
        print ("You follow the corridor to where the woman disappeared and find two doors")
        print("As you reach the end of the corridor you are faced with two giant doors,")
        print("one of the doors stained red with blood, the other frozen ice white. ")
        opt2_1_1()
    #pick between two doors
def opt2_1_1():
    door = input ("Enter 'a' for the BLOODY door or 'b' for the ICEY door")
    if door == "a":
        print("You open the door and the monster looks you clear in the eye,\n no longer in her human form, she flies toward you.\n Her claws rip into your flesh as the life drains out of you")
        print("What a savory drink have a peaceful afterlife")
    elif door == "b":
        print ("You open the door and are met by a friendly looking ghost. \n")
        print( "“Would you like me to take you to the exit? \n Or would you like me to take you to the weapons room to fight your own way out?”")
        opt2_1_2()
#exit or weapons
def opt2_1_2():
    a = "Take the exit"
    b = "Take me to the weopon"
    if a:
        print("The mischievous young ghost takes you straight to the feasting room.\n As soon as the door opens he monster looks you clear in the eye,\n no longer in her human form,\n she flies toward you.\n Her claws rip into your flesh as the life drains out of you")
    elif b:
        print("The ghost leads you to the weapons room. \nThe room contains hundreds of bows, arrows, swords, shields and everything you could imagine!\n You find some discarded rations and quickly eat them for strength, \ngrab a magic shield, sword and broken wooden flag pole.")
        print("As the ghost disappears he laughs and says “The exit is though the Red door” ")
        print("You make your way back to the Red door and plan your attack")
        print("Do I Sneak into the room (1) / Rush into the room (2)")
        opt2_1_3()

def opt2_1_3:
    if "1" :
        print ("You creep the door open slowly to reveal the woman crouching over a lifeless body,\n draining the blood to feed herself")
        print("The woman doesn’t appear to have noticed you enter")
        print("Sneak to the exit (1)/ Confront the woman (2)")
        opt2_1_4()
    elif "2":
        print("You burst through the bloody door at speed and startle the woman from her feed .\n She rises into the air and reveals her scaly wings. \n With the blink of an eye she has flown thrown you across the room. \n You are injured but still alive")
        print("The creatures flies to the centre of the room and lets out a cry once more")
        print("Attack the creature (1) / Defend the attack (2)")

        opt2_1_5() #question 10.

#question 9
def opt2_1_4:
    print("With a deep breath and your back pressed hard against the wall,\n you slowly make you way to the exit. As you open the door the woman hears you,")
    print(" instantly sprouting wings and screaming a high pitched wail. \n You quickly close the door behind you and pull across a big steal bolt. \n
    print("You run as fast as you can down the hill away from the castle.\n With a deep breath and your back pressed hard against the wall, \n you slowly make you way to the exit. \n As you open the door the woman hears you, \n instantly sprouting wings and screaming a high pitched wail.\n  You quickly close the door behind you and pull across a big steal bolt. \n You run as fast as you can down the hill away from the castle.")
    print("FINALLY YOU ARE OUT AND SAFE")
    print("Congratulations you win")




# search the room
#qst 6
def opt2_2():
    print("Do you want to take the risk? Roll a 6 to teleport home  or leave the orb ")
    min = 1
    max = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(min, max))
    roll_again = input("Roll the dices again?")




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


### Players first decison : game starts here
def intro():
    print("You wake up on a cold stone floor.")
    time.sleep(a)
    print("Moonlight creeping through an iron barred window reveals skeletons chained to the walls.")
    time.sleep(a)
    print(" The room is small and round with one arched door.")
    time.sleep(a)
    print("You hear a voice fill the room")
    time.sleep(a)
    print("In fear you reply")
    time.sleep(a)
    name = input("What is your name: ")
    time.sleep(a)
    print()
    print()

    intro_p1 = name + "! HOPE YOU SLEPT WELL \n hahahahahahahahahahhahahahaha"
    for cht in intro_p1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)

    print()
    print()

    startgame = input("Would you like to start the game? (Y?N): ")
    if startgame == "n" or startgame == "N":
        print ("Maybe some other time. Bye for now...")
    elif startgame == "y" or startgame == "Y":
        print("Welcome to hells's doom!")
        Choice()


### Start Game - Enter name 



#Main function
intro()


