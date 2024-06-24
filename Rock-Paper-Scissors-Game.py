import random
while True:
    user_score= 0
    computer_score= 0
    for i in range(5):
        options = ["Rock", "Paper", "Scissors"]
        user = input("Choose Rock, Paper, or Scissors: ")
        computer = random.choice(options)
        if user.lower() == computer.lower():
            print("It's a tie! Both players chose ", user , ".")
        elif (user.lower() == "rock" and computer.lower() == "scissors") or \
           (user.lower() == "paper" and computer.lower() == "rock") or \
            (user.lower() == "scissors" and computer.lower() == "paper"):
             print("You win! ",user, "beats",computer,".")
             user_score = user_score + 1
        else:
            print("Computer wins!", computer ,"beats", user,".")
            computer_score = computer_score + 1
    if user_score > computer_score:
        print("You won with score ", user_score-computer_score)
    elif user_score < computer_score:
        print("Computer won with score", computer_score-user_score)
    else:
        print("It's a tie....")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
    elif ans == 'y':
        continue
    else:
        print("Entered invalid value")
        exit()
print("Thanks for playing....")
    
