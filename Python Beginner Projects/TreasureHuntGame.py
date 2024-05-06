print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right':: ")

if direction.upper() == 'LEFT':
    swimOrWait = input("You've come to a lake. There is an island in the middle of the lake. "
                       "Type 'wait' to wait for a boat. Type 'swim to swim across.:: ")
    if swimOrWait.upper() == 'WAIT':
        color = input("You arrive at the island unharmed. There is a house with 3 doors. "
                      "One red, one yellow and one blue. Which colour do you choose?:: ")
        if color.upper() == 'RED':
            print("Burned by fire. Game Over.")
        elif color.upper() == 'BLUE':
            print("Eaten by beasts. Game Over.")
        elif color.upper() == 'YELLOW':
            print("You Win !!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
    pass
else:
    print("Fall into a hole. Game Over.")
