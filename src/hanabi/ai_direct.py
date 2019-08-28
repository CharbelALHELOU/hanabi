"""
Artificial intelligence to play hanabi randomly
"""
import itertools
from hanabi.ai import AI

class Direct(AI):
    '''
    Cette AI est un joeur qui joue l'indice qu'on lui donne
    si l'indice porte sur plusieurs cartes l'AI joue l premiere carte indicee partant de la gauche.
    s il n y a pas de cartes indicees il donne un indice au joueur suivant si il ya asse de blue coins.
    sinon il defausse la derniere carte.
    '''
    def play(self):
        plays={0:'p1',1:'p1',3:'p2',4:'p2',6:'p3',7:'p3',9:'p4',10:'p4',12:'p5',13:'p5'}
        game = self.game
        main=game.current_hand.str_clue()
        i=0
        found=False
        while i<len(main) and found==False:
            if main[i] != '*' and main[i] != ' ':
                found=True
            else:
                i=i+1
        if found==True:
            return( plays[i] )
        else:
            precious = [ card for card in
                         self.other_players_cards
                         if (1+game.discard_pile.cards.count(card))
                             == game.deck.card_count[card.number]
                       ]
            if precious:
                clue = False
                for p in precious:
                    if p.number_clue is False:
                        clue = "c%d"%p.number
                        break
                    if p.color_clue is False:
                        clue = "c%s"%p.color
                        clue = clue[:2]
                        break
                if clue:
                    if game.blue_coins>0:
                        return clue

            # if reach here, can't play, can't discard safely, no card to clue-save
            # Let's give a random clue
            if game.blue_coins >0:
                return 'c2' #pour ne pas perdre un 5

            return('d5')
