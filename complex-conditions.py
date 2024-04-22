turn_number = 1
point_number = 0
die_roll = int(input("Enter an integer between 2 and 12"))

if die_roll < 2 or die_roll > 12:
    raise ValueError("You did not enter a valid integer. Enter a value between 2 and 10")
else:
    print("You entered a valid integer between 2 and 12") 
if turn_number==1:
    if die_roll in [2,3,12]:
        print("turn number: ", turn_number)
        print("die roll: ", die_roll)
        print("Player loses")
    elif die_roll in [7,11]:
        print("turn number: ", turn_number)
        print("die roll: ", die_roll)
        print("Player wins")
    elif die_roll not in [2,3,7,11,12]:
        point_number == die_roll
        turn_number += 1
        print("turn number: ", turn_number)
        print("die roll: ", die_roll)
        print("point number: ", die_roll)

