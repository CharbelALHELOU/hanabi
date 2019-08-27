import hanabi
import hanabi.ai as AI
'''
	cette Algo sert a faire qulque stat sur les AIs consideres en donnant le meilleur score et son nbre d'apparition,le score le plus bas
	et la moyenne des scores.
	de plus il rend aussi le nbre de fois ou le jeu s'est termine a cause de 3 jetons rouge le nbre de fois ou le deck est fini et le nombre de
	fois ou l'AI s'est debarasser d'un 5 de n'importe quelle couleur
'''

moyenne=0
best_score_count=0
mini=25
maxi=0
redc=[0,0,0,0]
scores=[0]*26
cartecinq=0
no_more_cards=0

for i in range (1000):
	game = hanabi.Game(2)
	ai = hanabi.ai.Cheater(game)
	game.ai = ai
	game.run()
	j=game.score
	moyenne=moyenne + game.score
	if j <mini:
		mini=j
	if j>maxi:
		maxi=j
		best_score_count=1
	if j==maxi:
		best_score_count+=1
	redc[game.red_coins]+=1
	scores[game.score]+=1
	l=game.discard_pile.cards
	j=0
	while (j<len(l)):
		if l[j].number==5:
			cartecinq+=1
			j=len(l)
		j+=1
	if  len(game.deck.cards)==0:
		no_more_cards+=1



moyenne=moyenne/1000
print("\nL'ai marque en moyenne" , moyenne," points")
print("\nL'ai a marqué",maxi," points au maximum, a", best_score_count ,"reprises")
print("\nL'ai a marqué ",mini," points au minimum")
print("Le nombre de jetons rouge de chaque pqrti est reparti :",redc)
print("La repartition des scores: ", scores)
print("L'ai s'est defoce d'au moins un 5 a ",cartecinq,"reprises")
print("le deck s'est fini a ",no_more_cards,"reprises")
