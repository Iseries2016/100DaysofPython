print("Welcome to Treasure Island. Your mission is to find the treasure.")
decision = input("You come to a fork in the road. Do you go 'Left' or 'Right'?\n")
if decision.lower() == 'left':
    decision = input("Wise decision. You journey down the path until you come across a lake. Do you 'wait' for a boat or 'swim' across?\n")
    if decision.lower() == 'wait':
        print("You waited for the boat and successfully got across")
        print("You got to the island but there in front of you stands a wall with 3 doors.")
        decision = input("Which door do you choose: 'Yellow', 'Red', or 'Blue'?\n")
        if decision.lower() == 'red':
            print("Fire erupts from the door burning you to a crisp. Game Over!")
        elif decision.lower() == 'yellow':
            print("There stands the One Piece and you are crowned king of all. You Win!!")
        elif decision.lower() == 'blue':
            print("Beasts spring forth from the blue door and devour you. Game Over!")
        else:
            print("Not sure what you were trying to do but the rules of the island didn't like it. You were hit by lightening and you died. Game Over!")
    else:
        print("Becauase you were not patient you were devoured by a lake monster. You died!")
    
else:
    print("You turn to the right and fall into a pit of spikes. You died.")
    