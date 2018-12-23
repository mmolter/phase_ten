''' 

	Title:		Phase 10 Strategizer

	Author:		M. Molter

	Date:		23 DEC 2018

	Desc:		A platform for testing "Phase 10" card
				game strategies.

'''

import random

class Card:
	''' A class to represent a game card. '''

	def __init__(self, color, value):
		self.color = color
		self.value = value

	def __str__(self):
		return self.value + self.color

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
					self.cards.append(Card(color=c, value=str(v)))

			for i in range(8):
				self.cards.append(Card(color='', value='W'))

			for i in range(4):
				self.cards.append(Card(color='', value='S'))

	def shuffle(self):
		''' Shuffle the deck of cards. '''

		random.shuffle(self.cards)

	def draw(self, n=1):
		''' Draw a card off the top of the deck. '''

		return [self.cards.pop() for i in range(n)]

	def add(self, cards):
		''' Add a cards to deck. '''

		self.cards.extend(cards)

	def __str__(self):
		''' Display deck of cards. '''

		return ', '.join([str(c) for c in self.cards])

	def __len__(self):
		''' Return size of the deck. '''

		return len(self.cards)

deck = Deck(new_deck=True)
deck.shuffle()


hand = Deck(cards=deck.draw(n=10))
print(hand)