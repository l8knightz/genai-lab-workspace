# Day 3 of 100 Days of Python
# Treasure Island Adventure Game
import sys
print("Welcome to Treasure Island.")
print("""
        _.--.
    _.-'_:-'||
 _.-'_.-::::'||
.-:'_.-::::::'  ||
.'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
\\'.  ||:::::.-!()oo @!()@.-'_.|
'.'-;|:.-'.&$@.& ()$%-'o.'\\U||
 `>'-.!@%()@'@_%-'_.-o _.|'||
  ||-._'-.@.-'_.-' _.-o  |'||
  ||=[ '-._.-\\U/.-'    o |'||
  || '-.]=|| |'|      o  |'||
  ||      || |'|        _| ;
  ||      || |'|    _.-'_.-'
  |'-._   || |'|_.-'_.-'
   '-._'-.|| |' `_.-'
       '-.||_/.-'
""")

print("Your mission is to find the treasure.")
print("Your journey begins on a deserted island where you must make choices to find the treasure.")

direction = input("You're at a crossroad. Do you want to go left or right? ").lower()
if direction == "right":
        print("A gang of really OLD pirates jump out from behind a large rock and enslave you!\nGame Over!")
        sys.exit()
elif direction != "left":
        print("You must choose 'left' or 'right'.")

print("Your journey continues until you reach a wide river. It appears a ferry boat may be operating\n nearby but isn't visible at the moment.")
river = input("Do you want to wait to see if the boat returns, or enjoy a nice swim across the river? (boat/swim)? ").lower()
if river == "swim":
        print("You perform a flawless dive into the crystal clear water, begin your evigorating swim until the returning ferry, \nunaware of your presence, becomes the last thing you see has it sails over your body")
        print("Game Over")
        sys.exit()
elif river != "boat": 
        print("You must choose 'boat' or 'swim'.")

print("You wait patiently for the ferry to return and are greeted by a friendly ferryman who offers you a ride across the river.")
print("You arrive safely on the other side and discover a small path leading to a strange old house covered in vines and moss.")
print("Between the vines you can see three doors, one red, one yellow, and one blue.")
door = input("Which door do you want to open? (red/yellow/blue): ").lower()
if door == "red":
        print("You open the red door and are immediately engulfed in flames! You scream in agony as you are consumed by the fire.")
        print("Game Over!")
        sys.exit()
elif door == "blue":
        print("You open the blue door and are greeted by a pack of hungry wolves! They tear you apart in seconds.")
        print("Game Over!")
        sys.exit()
elif door == "yellow":
        print("You open the yellow door and find a room filled with gold and jewels! You have found the treasure!")
        print("Congratulations, you win!")
        print('''
          
                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
              . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
                 ''')
else:
    print("You must choose 'red', 'yellow', or 'blue'.")

print("Thank you for playing Treasure Island!")