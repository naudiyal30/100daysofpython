#Write a python program which will keep adding a stream of numbers inputed bu the user. The adding stops as soon as user presses q key on keyboard

sum = 0
while(True):
    userInput = number = input("Enter the item price or press q to quit: \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your total bill is {sum}. thanks")
        print("Thanks for shopping with us")
        break