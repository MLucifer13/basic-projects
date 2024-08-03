import random

def main():
    number  = random.randint(1,100)
    attempt = 0
    print("Guess the number between 1 to 100")
    while True:
        attempt +=1
        guess = int(input("Enter your guess: "))
        if guess == number:
            print (f"You guessed it right in {attempt} attempts")
            break
        elif guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")



if __name__ == "__main__":
    main()



