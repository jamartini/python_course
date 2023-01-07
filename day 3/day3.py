print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = str(input("You're in a forest and you see a cave, and you feel like you should enter it. After walking "
                      "for a few minutes you can see it goes in two different directions, type 'left' if you want to "
                      "go left or type 'right' if you want to go right."))

if direction == "left":
    print("The cave goes deeper and you can smell something that's not that good and you start to regret your choice, "
          "but it's already too late as you see two fierce eyes get near your face and you realize it's your end. Game "
          "over.")
elif direction == "right":
    yell = str(input("The cave goes forward and you end up in a place that seems like a very large room, you can yell "
                     "something to analyze the echo or to see if something shows up (type 'yes') or you can go further "
                     "and try to recognize the place by hand (type 'no')."))
    if yell == "yes":
        print("You can hear some steps and you start to smell something that's not that good and you regret your "
              "choice, but it's already too late as you turn around and see two fierce eyes get near your face and you "
              "realize it's your end. Game over.")
    elif yell == "no":
        run_or_walk = str(input("You go to the end of the cave to see a chest opened up, revealing its treasure. You "
                                "take the treasure and turn around in order to get out of the cave. You can do it "
                                "silently like nothing happened or you can run to guarantee your treasure quickly. "
                                "Type 'run' or type 'walk'."))
        if run_or_walk == "run":
            print("As you're running you can hear some loud steps getting closer and you regret your choice, but it's "
                  "already too late as you turn around and see two fierce eyes get near your face and you realize it's "
                  "your end. Game over.")
        elif run_or_walk == "walk":
            print("You get out of the cave safely with your treasure. Congratulations, you won the game!")
