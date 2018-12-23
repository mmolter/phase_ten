''' 

	Title:		Phase 10 Strategizer

	Author:		M. Molter

	Date:		23 DEC 2018

	Desc:		A platform for testing "Phase 10" card
				game strategies.

'''

class Card:
	''' A class to represent a game card. '''

	def __init__(self, color, value):
		self.color = color
		self.value = value

class Deck:
	''' A class to hold a series of cards. '''

	def __init__(self, cards=None, new_deck=False):
		''' Create a deck of cards.

			Args:

				cards (list):		accepts a list of cards.
				new_deck(bool):		optionally create a new standard deck.
		'''

		if cards:
			self.cards = cards

		elif new_deck:
			self.cards = []

			for c in ['R', 'R', 'B', 'B', 'G', 'G', 'Y', 'Y']:
				for v in range(1, 12+1):
					self.cards.append(Card(color=c, value=v))

			for i in range(8):
				self.cards.append(Card(color='-', value='W'))

			for i in range(4):
				self.cards.append(Card(color='-', value='S'))

	def __str__(self):
		''' Display deck of cards. '''

		return ', '.join([card.value + card.color for card in self.cards])

	def __len__(self):
		''' Return size of the deck. '''

		return len(self.cards)

deck = Deck(new_deck=True)
print(len(deck))

print(sys.__version__)
