import random
min = 1
max = 6
roll_again = "yes"
for i in range (0, 3):
    while roll_again == "yes" or roll_again == "y":
        print ("Rolling the dice...")
        print ("You got...")
        rand_num = random.randint
        print (str(rand_num(min, max)))
        roll_again = input("Roll the dices again? ")
        if rand_num(min, max) == "6":
            print("Congratulations you are a lucky duck, you win!")
            break
        else:
            print("Chances are up")
            break
