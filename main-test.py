# completed option 1

# working on option2
#
'''def option2():
    print("You struggle to your feet to search the room.")

    opt2 = input(" Do you want to pull loose stone from wall or find a nail to pick the lock? ")
    a = "pull loose stone from wall"
    b = "find a nail to pick the lock"
    
    #pull the stone
    if opt2 == "a ":
        print (" You pull hard on the stone, your feet scrambling for grip on the hard stone")
        print("Floor, the stone breaks free and sends you tumbling back. ")
        print("The hole reveals you are in a very high turret, towering above the town below")
        print(" from the giant hill it sits on. You see no clear route to escape")
        option2()
# find a nail and pick the lock
    elif opt2 == "b":
        print(" You struggle with the rusty lock but quickly and silently manage to disengage it. ")
        print("  After picking the lock, you slowly open the door and creep out of the dungeon.")
        print(" A long and winding staircase takes you to the bottom of the turret to another wooden arched door.")
        

        s1 = input ( "Run and barge the door (1)/Silently open the door and creep in (2)")
# forcefully open the door
        if s1 == 1:
            print("The door forcefully opens, Woman turns into vampire and kills you")
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
                opt2_()


def opt2_1():

        


# option 2_b'''
   

#question 9 
def opt2_1_4():
    b = "Sneak to the exit (1)/ Confront the woman (2)"
    if b == "1":
        print("With a deep breath and your back pressed hard against the wall,\n you slowly make you way to the exit. As you open the door the woman hears you,")
        print(" instantly sprouting wings and screaming a high pitched wail. \n You quickly close the door behind you and pull across a big steal bolt. \n
        print("You run as fast as you can down the hill away from the castle.\n With a deep breath and your back pressed hard against the wall, \n you slowly make you way to the exit. \n As you open the door the woman hears you, \n instantly sprouting wings and screaming a high pitched wail.\n  You quickly close the door behind you and pull across a big steal bolt. \n You run as fast as you can down the hill away from the castle.")
        print("FINALLY YOU ARE OUT AND SAFE")
        print("Congratulations you WIN")
    elif b == "2":
        print("You raise your sword to attack the woman but she hears the movement and notices you.\n She lets out a high pitched scream as she sprouts wings and flies toward you.")
        opt2_1_5(): #qst 10

def opt2_1_5(): #qst 10
    print("The creatures flies to the centre of the room and lets out a cry once more")
    print("Attack the creature (1) / Defend the attack (2)")
    b = "Attack the creature (1) / Defend the attack (2)")
    if b == "1":
        print("With a mighty swing of the sword you manage to make contact and slash her wing.\n She lets out a scream more terrifying than before but is grounded and cannot fly")
        opt2_1_6(): #qst 11
    elif b == "2":
        print("Screaming wildly,\n the creature flies at you with incredible speed,\n you hold up your shield.\n She hits the shield with incredible force,\n knocking you to your knees but injuring her greatly.")
        opt2_1_7() #qst 12

def opt2_1_6(): #qst 11
    print("You run toward the grounded creature but see the exit at the other end of the room")
    print("Do you Run for exit (1)/ Attack (2)")
    b = "Do you Run for exit (1)/ Attack (2)"
    if b == "1":
        print("You run for the exit but the creature disappears from view.\n As you approach the door you feel cold hands on your face,\n you feel teeth sinking into your neck.\n The light fades as you take your last breath.\n")
        GameOver()
    elif b == "2":
        print("You run at the beast thrusting your sword wildly but the creature disappears from view.\n As you stand startled and confused,\n you feel cold hands entangle you.\n You feel teeth sinking into your neck.\n The light fades as you take your last breath.")
        GameOver()
    
def opt2_1_7():
    print("As the creature flies around in pain you decide whether to")
    print("Run for the exit (1) / Ready yourself for another attack (2)")

    b = "Run for the exit (1) / Ready yourself for another attack (2)")
    if b == "1":
        print("You run for the exit but the creature disappears from view.\n As you approach the door you feel cold hands on your face,\n you feel teeth sinking into your neck.\n The light fades as you take your last breath.\n")
        print("Enjoy your afterlife.You lose ")
        GameOver()
    elif b == "2":
        print("You run to find a defensive position and ready your sword and shield.\n  As she flies toward you, you break cover and drive your sword directly through her chest. \n The beast screams but is not dead, magic still pumping through her veins")
        opt2_1_8() #qst 13
    
def opt2_1_8(): #qst 13
    print("The creature is clearly injured, writhing around on the floor.")
    print ("Do you Run for the exit (1)/ Finish the kill (2)")
    b = "Do you Run for the exit (1)/ Finish the kill (2)")
    if b == "1" :
        print("You run at the beast thrusting your sword wildly but the creature disappears from view.\n As you stand startled and confused,\n you feel cold hands entangle you.\n You feel teeth sinking into your neck.\n The light fades as you take your last breath.")
        GameOver()
    elif b == "2":
        print("You approach the creature and drive the flag pole directly through the heart. \n The creature instantly regains form as a beautiful woman and begs for you to spare her life.")
        print(" Do you Spare her life (1) / Finish the kill (2)")
        opt2_1_9() #qst 14

def opt2_1_8(): # qst 14
    b = " Do you Spare her life (1) / Finish the kill (2)"
    if b == "1":
        print ("As you turn for the exit, you hear the paranormal scream once more.\n The vampire is still alive and takes your life.")
        GameOver():
    elif b == "2"
        print("You remove the stake and drive it once more hard into the chest.\n The woman let out a human cry.\n Concerned she may return,\n you remove the head with one strike of the sword.\n You rush toward to exit and get out alive!! ")
        print ("YOU WIN")


        










    


    

