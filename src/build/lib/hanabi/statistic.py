import hanabi
import hanabi.ai as AI
from recomendation_ai import Recommend #si on veut tester random from ai_Random import Random
'''
	cette Algo sert a faire qulque stat sur les AIs consideres en donnant le meilleur score et son nbre d'apparition,le score le plus bas
	et la moyenne des scores.
	de plus il rend aussi le nbre de fois ou le jeu s'est termine a cause de 3 jetons rouge le nbre de fois ou le deck est fini et le nombre de
	fois ou l'AI s'est debarasser d'un 5 de n'importe quelle couleur
'''
#on initialise chacune de nos variable
moyenne=0
best_score_count=0
mini=25
maxi=0
redc=[0,0,0,0]
scores=[0]*26
cartecinq=0
no_more_cards=0

for i in range (1000):#on effectue l'étude statistique sur 1000 parties
	game = hanabi.Game(5)#on lance les parties les une après les autres
	ai = Recommend(game)
	game.ai = ai
	game.run()
	j=game.score
	moyenne=moyenne + game.score#traitement de la moyenne
	if j <mini:#traitement du score minimun
		mini=j
	if j>maxi:#traitement du score maximun
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


#on renvoie les résultats
moyenne=moyenne/1000
print("\nL'ai marque en moyenne" , moyenne," points")
print("\nL'ai a marqué",maxi," points au maximum, a", best_score_count ,"reprises")
print("\nL'ai a marqué ",mini," points au minimum")
print("Le nombre de jetons rouge de chaque parti est reparti :",redc)
print("La repartition des scores: ", scores)
print("L'ai s'est defoce d'au moins un 5 a ",cartecinq,"reprises")
print("le deck s'est fini a ",no_more_cards,"reprises")
