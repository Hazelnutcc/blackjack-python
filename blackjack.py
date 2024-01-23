import random
import os

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def play_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #hints of bj
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, cpu_score):
    if player_score > 21 and cpu_score > 21:
        return "You both went over, you lose!"

    if player_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "Lose, cpu had a Blackjack"
    elif player_score == 0:
        return "You win with a Blackjack"
    elif player_score > 21:
        return "You went over, you lose"
    elif cpu_score > 21:
        return "CPU went over, you win"
    elif player_score > cpu_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    clear_screen()
    print('''
    .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
    ''')
    print("Welcome to Blackjack!")


    player_card = []
    cpu_card = []

    for _ in range(2): #no var coz all we need is this loop run twice
        player_card.append(play_card())
        cpu_card.append(play_card())

    while True:
        player_score = calculate_score(player_card)
        cpu_score = calculate_score(cpu_card)
        print(f" Your cards: {player_card}, current score: {player_score}")
        print(f" CPU cards: {cpu_card}, current score: {cpu_score}")

        if player_score == 0 or cpu_score == 0 or player_score > 21:
            break
        else:
            player_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_deal == 'y':
                player_card.append(play_card())
            else:
                break

    while cpu_score !=0 and cpu_score < 17:
        cpu_card.append(play_card())
        cpu_score = calculate_score(cpu_card)

    print(f"Your final hand: {player_card}, final score: {player_score}")
    print(f"CPU final hand: {cpu_card}, final score: {cpu_score}")
    print(compare(player_score, cpu_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_game()
