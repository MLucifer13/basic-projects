def main():
    print("Welcome to computer quiz")
    playing = input("Do you want to play? ")
    if playing.lower() == "yes":
        print("Let's play")
        quiz()
    else:
        quit()

def quiz():
    score = 0 
    cpu = input("What does CPU stand for? ")
    if cpu.lower().strip() == "central processing unit":
        print("Correct")
        score+= 1
    else:
        print("Incorrect")

    gpu = input("What does GPU stand for? ")
    if gpu.lower().strip() == "graphics processing unit":
        print("Correct")
        score+= 1
    else:
        print("Incorrect")

    ram = input("What does RAM stand for? ")
    if ram.lower().strip() == "random access memory":
        print("Correct")
        score+= 1
    else:
        print("Incorrect")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 3) * 100) + "%.")


if __name__ == "__main__":
    main()

