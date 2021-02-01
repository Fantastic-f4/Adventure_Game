# completed option 1

# working on option2
#
def option2():
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

        


# option 2_b
   


    
