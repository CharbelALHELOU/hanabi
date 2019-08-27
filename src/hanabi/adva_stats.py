import hanabi
import hanabi.ai as AI
from recommendation_ai import Recommend


import statistics
import matplotlib.pyplot as plt

L=[]
game=hanabi.Game(5)

for i in range(1000):
    game.reset()
    game = hanabi.Game(5)
    ai = Recommend(game)
    game.ai = ai
    game.run()
    L.append(game.score)

print(statistics.mean(L))
plt.hist(L)
plt.title('Statistiques ')
plt.savefig('Recommend_stat.png')
plt.show()