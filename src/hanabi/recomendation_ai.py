import itertools
from hanabi.ai import AI
import sys 




def value_calc(playable,dead,notprecious):
    if playable != []:
        fives=[c for c in playable if c[1]==5]
        #recommendation 1: if there's a playable five play the lowest index
        if fives != []:
            return ('p'+str(fives[0][0]))
        else:
        #recommendation 2: play the lowest indexed playable card
            return ('p'+str(playable[0][0]))
    if dead != [] :
        #recommendation 3 : discard the lowest indexed dead card
        return ('d'+str(dead[0]))
    if notprecious != []:
        #recommendation 4 : discard the highest ranked not precious card with the lowest index
        m=max(c[0] for c in notprecious)
        highestrank=[c[1] for c in notprecious if c[0]==m]
        return( 'd'+str(highestrank[0]) )
    #recommendatio 5: discard the c1
    return 'd1'


def generate_clue(values):
    hint=sum(values)%8
    if hint<4: 
        return ('c1'+str(hint+1))
    else:
        return ('cg'+str(hint-3))



class Recommend (AI):

    def __init__(self,game):
        self.playtimes=0
        self.cluetime=-1
        self.game=game
        self.lastvalues=[0,0,0,0] # each player can only see his value, it s a game between AIs so we will save time 
        
    def  play(self):
        game=self.game
        decode = {0 : "p1",1 : "p2",2 : "p3",3 : "p4",4 : "d1",5 : "d2",6 : "d3",7 :"d4"}
        code= {"p1":0 , "p2":1 , "p3":2 , "p4":3 , "d1":4 , "d2":5 , "d3":6 , "d4":7 }
        current_values=[-1,-1,-1,-1]

        # attribute a value to each player
        for j in range(0,4):

            # a playable card is a card that can be successfully played with the current game state
            playable = [ (i+1, card.number) for (i,card) in
                        enumerate(self.other_hands[j].cards)
                        if game.piles[card.color]+1 == card.number ]

            # a dead card is a card that has the same rank AND suit of a successfully played card
            dead = [ i+1 for (i,card) in
                            enumerate(self.other_hands[j].cards)
                            if ( (card.number <= game.piles[card.color])
                                or (self.other_hands[j].cards.count(card)>1)
                            ) ]
            # a indispensable (precious) card is a card for wich all other id copies have been removed from the game
            # we need the not precious cards
            notprecious = [ (card.number,i+1) for (i,card) in
                          enumerate(self.other_hands[j].cards)
                          if not ((1+game.discard_pile.cards.count(card))== game.deck.card_count[card.number])]            
            
            current_values[j]=code[value_calc(playable,dead,notprecious)]
        
        
        if (self.cluetime not in [0,1,2,3]) :
            #give a clue
            self.playtimes=0
            self.cluetime=0
            self.lastvalues=current_values
            return (generate_clue(current_values))

        action= self.lastvalues[self.cluetime]
                

        if action<4:
            if (self.playtimes==0) or ((self.playtimes==1) and game.red_coins<2):
                self.playtimes+=1
                self.cluetime+=1
                return (decode[action])
            else:
                if game.blue_coins>0:
                    #give a clue
                    self.playtimes=0
                    self.cluetime=0
                    self.lastvalues=current_values
                    return (generate_clue(current_values))
                self.cluetime+=1
                return ('d1')
        else:
            if game.blue_coins>0:
                self.playtimes=0
                self.cluetime=0
                self.lastvalues=current_values
                return (generate_clue(current_values))
            else:
                self.cluetime+=1
                return (decode[action])
            self.cluetime+=1
            return ('d1')
