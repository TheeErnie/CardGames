import random
deck = []
piles = [[0]*4 for _ in range(13)]
stats_remaining_cards = []

# === functions === #
def reset_deck():
  global deck
  deck = []
  for i in range(0,52):
    deck.append(i % 13)

  random.shuffle(deck)

def set_piles():
  global deck
  piles = [[0]*4 for _ in range(13)]
  for i in range(0,52):
    piles[i % 13][i // 13] = deck[i]
  return piles

def game():
  global piles, stats_remaining_cards
  next_card = piles[12].pop()
  while not (next_card == 12 and len(piles[12]) == 0):
    next_card = piles[next_card].pop()
  remaining_cards = 0
  for i in piles:
    remaining_cards += len(i)
  stats_remaining_cards.append(remaining_cards)
  return remaining_cards == 0

# === main === #
reset_deck()
piles = set_piles()

number_of_games = int(input("Games to run: "))
if number_of_games > 100000000:
  number_of_games = 1000000
  
wins = 0
for i in range(number_of_games):
  if(game()):
    wins += 1
  reset_deck()
  piles = set_piles()

print('wins: ' + str(wins), '\tgames:' + str(number_of_games))
print('win percentage: ' + str(round(wins/number_of_games*100, 2)) + '%')