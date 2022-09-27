# from art import logo
import random
# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
c_choice = ['y', 'n']
your = []
comp = []

def deal():
  for i in range(2):
    your.append(random.choice(cards))
    comp.append(random.choice(cards))
    
def win():
  if 11 in comp and 10 in comp:
    return "Blackjack Computer Wins"
  elif 11 in your and 10 in your:
    return "Blackjack You Win"
  else:
    return 0

def win2():
  if sum(comp) == 21:
    return 1 
  elif sum(your) == 21:
    return 2
  else:
    return 0

def your_score():
  print(f"  Your cards: {your}, current score: {sum(your)}")
  print(f"  Computer's First Card: {comp[0]}")

def another():
  your.append(random.choice(cards))
  
  
def final():
  s1 = sum(your)
  s2 = sum(comp)
  print(f"  Your final hand: {your}, final score: {s1}")
  print(f"  Computer's final hand: {comp}, final score: {s2}")

def win3():
  s1 = sum(your)
  s2 = sum(comp)
  if s1 > 21:
    print("You Lose😒")
  elif s2 > 21:
    print("You Win😌")
  elif s1 > s2:
    print("You Win😌")
  elif s1 == s2:
    print("Draw")
  else:
    print("You Lose😒")
  
def computer():
  if 11 in comp:
    if sum(comp) > 21:
      your.remove(11)
      your.append(1)
  while sum(comp) < 17:
    comp.append(random.choice(cards))
    if 11 in comp:
      if sum(comp) > 21:
        your.remove(11)
        your.append(1)

def check11():
  if 11 in your:
    if sum(your) > 21:
      your.remove(11)
      your.append(1)
    else:
      return
  else:
    return
   
def blackjack():
#   print(logo)
  deal()
  if 11 in your:
    if sum(your) > 21:
      your.remove(11)
      your.append(1)
  pore = win()
  pore1 = None
  
  if pore == 0:
    your_score()
    
  
    while sum(your) < 22:
      if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        another()
        check11()
        pore1 = win2()
        if pore1 != 0:
          break
        if sum(your) > 21:
          break
        your_score()
      else:
        break
  computer()
  pore1 = win2()
  if pore != 0:
    final()
    print(pore)
  elif pore1 == 1:
    final()
    print("Blackjack Computer Wins")
  elif pore1 == 2:
    final()
    print("Blackjack You Win")
  else:
    final()
    win3()
    
    
ans = 'y'
while ans == 'y':
  ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if ans == 'y':
    # clear()
    blackjack()
    while len(your) > 0:
      your.pop()
    while len(comp) > 0:
      comp.pop()
  