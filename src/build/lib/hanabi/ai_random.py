"""
Artificial intelligence to play hanabi randomly
"""
import itertools
from hanabi.ai import AI
from random import *

class Random(AI):
	"""
	This is a player who plays randomly if there's enough blue coins (bc) he can play or give a clue (if bc=8)
	or chose randomly between the 3 possibilities (bc<8)
	if there's no more blue_coins he will discard a card for sure
	"""

	def play(self):
		game=self.game
		clue = {0:'c1',1:'c2',2:'c3',3:'c4',4:'c5',5:'cr',6:'cw',7:'cb',8:'cg',9:'cy'}
		bc=game.blue_coins
		if bc>0:
			if bc==8:
				p=randint(0,1)
				if p==0:
					return('p'+str(randint(1,5)))
				else:
					return(clue[randint(0,9)])
			else:
				p=randint(0,2)
				if p==0:
					return('p'+str(randint(1,5)))
				elif p==1:
					return(clue[randint(0,9)])
				else:
					return('d'+str(randint(1,5)))
		else:
			return('d'+str(randint(1,5)))
