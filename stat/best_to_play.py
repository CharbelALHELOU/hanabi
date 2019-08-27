import hanabi
'''
    cette aldorithme fait joi la meme commande tout le temps a 100 reprises pour chque play possible et rend
    la moyenne des scores
    de plus il rend le meilleur des scores avec les play qui l'ont marqué (chaque play apparqitera autant de fois qui l'a marque le meilleur score)
'''

choices={"p1":0, "p2":0, "p3":0, "p4":0, "p5":0}
best_score=0
best_scorers=[]

for p in choices:
    moyenne=0
    for i in range (1000):
        game = hanabi.Game(2)
        game.ai = p
        game.run()
        gs=game.score
        moyenne=moyenne + gs
        if gs==best_score:
            best_scorers.append(p)
        elif gs>best_score:
            best_score=gs
            best_scorers=[p]
    choices[p]=moyenne/1000

print('\n')
for p in choices:
    print(p,"a un score moyen de",choices[p],"\n")

print("Le meilleur score est de ",best_score,"il a ete marqué par",best_scorers)
