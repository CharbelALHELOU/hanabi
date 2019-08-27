import hanabi
import hanabi.ai as AI
from recommendation_ai import Recommend #si on veut tester random from ai_Random import Random
'''
	Un algo de stat basique pour etudier l 'AI de recommendation
'''
#on initialise chacune de nos variable
moyenne=0
best_score_count=0
scores=[0]*26
maxi=0

for i in range (1000):#on effectue l'étude statistique sur 1000 parties
	game = hanabi.Game(5)#on lance les parties les une après les autres
	ai = Recommend(game)
	game.ai = ai
	game.run()
	j=game.score
	moyenne=moyenne + game.score#traitement de la moyenne
	
	if j>maxi:#traitement du score maximun
		maxi=j
		best_score_count=1
	if j==maxi:
		best_score_count+=1
	scores[game.score]+=1
	


#on renvoie les résultats
moyenne=moyenne/1000
print("\nL'ai marque en moyenne" , moyenne," points")
print("\nL'ai a marqué",maxi," points au maximum, a", best_score_count ,"reprises")
print("La repartition des scores: ", scores)
