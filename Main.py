import random

def number_guess():
    computer_health = 100
    user_health = 100
    computer_number = random.randint(0,100)
    user_number = 0

    while computer_health != 0 :
        print(f"computer_health : {computer_health}")
        print(f"user health : {user_health}")

        user_number = int(input("Enter the number : "))
            
        while 0 < user_number > 100:
            print("Please enter the number in the given range (0 - 100)")
            user_number = int(input("Enter the number : "))

        if user_number > computer_number:
            print("Your number is greater then the computer number")
            user_health -= 10
        elif user_number < computer_number:
            print("Your number is less then the computer number")
            user_health -= 10
        
        if user_number == computer_number:
            computer_health -=10
            computer_number = random.randint(0,100)

        if user_health == 0:
            print("You loose!")
            break

if __name__ == '__main__':
    number_guess()



