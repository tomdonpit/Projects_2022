import random

high_score = 0


def dice_game():
    global high_score
    print("Your current High Score:", high_score)
    print("1) Roll the dice")
    print("2) Leave the game")

x = input("Enter your choice")
print("\n")

while True:
    if x == "1":
        roll_dice1 = random.randint(1, 6)
        roll_dice2 = random.randint(1, 6)
        total_roll = roll_dice1 + roll_dice2
        print("You rolled a ", roll_dice1)
        print("You rolled a", roll_dice2)
        print("You have rolled a total of:", total_roll)

    if high_score < total_roll:
        high_score = total_roll
        print("Congrats! Your new high score:", total_roll)

    if total_roll < high_score:
        print("Your high score is", high_score)

    else:
        print("Goodbye!")
    
    break
