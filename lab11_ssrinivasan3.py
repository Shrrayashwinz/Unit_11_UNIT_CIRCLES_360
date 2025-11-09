"""
Program Name: lab11_ssrinivasan3.py

Author: Shrrayash Srinivasan

Purpose: 1.	Create a function that takes a numeric input representing the degrees of a rotation and adjusts it to remove 
unnecessary rotations if more than a full rotation is entered.  For example, an input of 100 should just return 100, but an 
input of 460 should return 100 to eliminate the full 360-degree rotation

Date: November 4, 2025

"""

def degree_rotation(degrees):

    try: 
        degrees = int(degrees)
        return degrees % 360
    
    except (TypeError, ValueError):
        print("\nIt needs to be numerical\n")
        return None

def main():
    print("You are now in the rotation calendar. Let's get started!")
    print("\nRULES\n")
    print("1) Always type in full numbers (e.g. 360, 250, 90). Decimals are not allowed.")
    print("2) No strings, letters, or symbols allowed.")
    print("3) If you use strings or letters, the code will give you a message and you will need to restart the simulation!")
    print("4) If you want to end the game, just hit N. If you hit anything other than a Y or N, you will have to enter another number to get to the cotinuation prompt.")
    print("5) Enjoy!")

    resume = True

    while resume:
        number_str = (input("Enter a number:"))
        degrees = degree_rotation(number_str)

        number = int(number_str)

        if number < 360 and number >= 0:
            print("This number:", number, "is within the 360 degrees range; no need to simplify it!")
        
        elif number >= 360 or number < 0:
            print("This number:", number, "is equalvalent to", degrees, "when the rotations are used")   
            
        else:
            print("Please give an actual number. Decimals, symbols, and strings are not permitted.")

        choice = input("Hey there dude! Do you want to go again? [Y/N]")
        if choice == 'y':
            resume = True
        
        elif choice == 'n':
            resume = False
            print("See you later!")
            break
        else:
            print("Invalid input.")

            


if __name__ == "__main__": 
    main()



        




    




