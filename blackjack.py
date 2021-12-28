from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card_for_dealer (comp_cards):

  while True :
    comp_cards.append(random.choice(cards))

    if sum(comp_cards) > 21:
      print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
      print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
      print("Conputer went over. You Win.")
      break 
  

def draw_card_for_player (pl_cards):

  while True:
    pl_cards.append(random.choice(cards))
    print(f"Your cards: {pl_cards}, current score: {sum(pl_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    if sum(pl_cards) > 21:
      return
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'n':
      break
    
    
while True:
  should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  
  if should_continue == 'n':
    break
  elif should_continue == 'y':
    clear()
    print(logo)

    pl_cards = []
    comp_cards = []

    pl_cards.append(random.choice(cards))
    pl_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    
    print(f"Your cards: {pl_cards}, current score: {sum(pl_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")
    print(f"Computer's Cards{comp_cards}")

    dCard = input("Type 'y' to get another card, type 'n' to pass: ")
    if dCard == 'n':
      print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
      if sum(comp_cards) <= 18 :
        draw_card_for_dealer(comp_cards)
      else:
        print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
    
    elif dCard == "y":
      draw_card_for_player(pl_cards)
      if sum(pl_cards) > 21 :
        draw_card_for_dealer(comp_cards)
        print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
        print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
        print("You went over. You lose.")
        

    # Decalaring Winner
    
    if sum(pl_cards) == sum(comp_cards):
      print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
      print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
      print("Draw")
    elif sum(pl_cards) > sum(comp_cards) and sum(pl_cards) <= 21:
      print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
      print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
      print("Playes Wins.")
    elif sum(pl_cards) < sum(comp_cards) and sum(comp_cards) <= 21:
      print(f"Your final hand: {pl_cards}, current score: {sum(pl_cards)}")
      print(f"Computer's final hand: {comp_cards}, current score: {sum(comp_cards)}")
      print("Computer Wins.")

    
    


    




