# **Projet Hanabi**
### **Charbel ALHELOU et Luc LAPORTE**
-------------------------------------------------
# **I- Statistiques de l'AI Cheater**
  Pour évaluer la performance de l’AI Cheater nous avons ecrit l’algo `statistic.py` .
  Cette algorithme nous permet a travers une itération de 1000 parties de tirer quelques chiffres significatifs, par exemple le score maximal et minimal, ainsi que la moyenne des scores.
  Mais pour approfondir notre étude, nous avons apporté quelques modifications à cette algorithme, en effet on a cherché à comprendre les raisons qui empêche l'AI d’avoir un score maximal. Pour cela, l’algorithme affiche désormais la répartition des scores, celle du nombre de jetons rouges, le nombre de fois où l’AI s’est défaussé d’un 5 et ou le deck s’est épuisé.

  L’execution de ce programme pour l’AI cheater affiche:

  ![statAI](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/testAI.png)

  Une première observation peut être faite sur les scores en effet,

  `Le score maximal est de 25 `

  `Le score minimal est de 20`

  `Le score moyen est de 24.814`

  Ces chiffres montrent une grande performance de l’algorithme, non étonnante puisque en fin de compte il ne respecte pas les règles du jeu.
  On peut aussi remarquer la répartition des scores affichée par le diagramme et le tableau suivants:

  | Scores | 20 | 21 | 22 | 23 | 24 | 25 |
  | --- | --- | --- | --- | --- | --- | --- |
  | Apparition | 1 | 8 | 13 | 23 | 64 | 891 |

  ![graphAI](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/graph1.png)

  La répartition des scores témoigne de la fiabilité de l’algorithme a marqué de hauts  scores à un grand nombre de reprises.
  Mais l'expérience montre que la moyenne quant à elle reste au voisinage proche des 24.8 et ne touche que rarement les 24.9 .
  Donc on a essayé de s'intéresser aux cause induisants les 10.9% de scores imparfaits.

  D’abord on a tenté de voire si l’AI terminait une parti à cause de 3 jetons rouge et on s'est rendu compte que le programme ne commettait une erreur et durant toutes les parties le nombre de jetons rouge demeure zéro.
  Les deux causes possibles restantes qui peuvent faire que la partie se termine avant d’atteindre les 25 points est l'AIR s’est défaussé d’une carte importante (dans notre cas on s'intéresse au 5) ou il ne reste plus de cartes dans le deck.
  Dans notre cas, on retrouve que l’AI se défausse à 37 reprises d’un cinq sur les 109 parties incomplète. Donc sur ⅓ de ces parties l’AI s’est retrouvé obligé de se défausser d’un cinq (alors qu’elle sait que c’en est un) et cela parce que il est rester beaucoup trop longtemps passif (sans clue sur cette carte et injouable) dans sa main.
  Ainsi, un probleme peut etre le fait qu’une partie dur beaucoup trop longtemps.
  Le nombre de fois ou le deck s'épuise ( 412 fois ) vient soutenir ce propos.
  On le voit dans la partie suivante, tiree d'un test de 1000 parties:

  ![endgame](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/endgame.png)

  En conclusion à ces statistiques, les performances de l'AI (malgré sa stratégie) restent impressionnantes. Mais le faite que cette AI cherche la meilleur carte à jouer dans ses cartes en priorité fait que le jeu arrive dans 10.9% a un état bloqué ou les 25 points ne sont plus faisable.
  On peut peut etre ameliorer encore plus les performance de cette AI en lui permettant de choisir la meilleur carte parmi toute les cartes des joeurs et de joeur en fonction.

# **II- AI aléatoire**
  Après ces quelques statistiques, on a essayé de développer un programme naïf qui joue aléatoirement.
  Cette algorithme est présent dans le fichier `ai_random` et fonctionne selon la stratégie suivante:

  +Si il n’y a plus de jetons bleus l’AI se défausse d’une carte aléatoirement.<br/>
  +Si il y a au moins un jeton bleu on a 2 cas:<br/>
  1-Il y en a 8 l’AI joue aléatoirement ou donne un indice aléatoire.<br/>
  2-Il y a moins de 8 jetons et l’AI peut choisir une des 3 possibilités.<br/>

  En testant cette AI avec l’algorithme de statistiques du paragraphe précédent on obtient les résultats :


  ![testR](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/oldRandom.png)

  Et on note les chiffres suivants:

  `Le score maximal est de 8`

  `Le score minimal est de 0`

  `Le score moyen est de 1.28`  

  En répétant l'expérience à plusieurs reprises on remarque quelques points intéressants.
  Tout d’abord, la moyenne des scores n’est jamais inférieur à 1 et reste au voisinage des 1.2 points .
  Le score maximal est toujours 7 ou 8 points.
  Les parties se terminent à chaque fois a cause de trois jetons rouges et n’arrive jamais a la fin du deck.

  | Jetons R | 0 | 1 | 2 | 3 |
  | --- | --- | --- | --- | --- |
  | Parties | 0 | 0 | 0 | 1000 |

  On note aussi que l'AI se défausse d’un 5 à 541 reprises .

  D'autre part,la répartition des scores se fait de la façon suivante:

  | Scores | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | -- |
  | Apparition | 335 | 302 | 202 | 102 | 35 | 19 | 3 | 1 | 1 |

  ![graph2](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/graph2.png)

# **III-AI Direct**
  Cette AI est présente dans le fichier `ai_direct`.

  Il fonctionne machinalement et joue l'indice qu'on lui donne.En le testant avec l'algorithme des statistiques on a les résultats suivants :

  ![testDirect](https://github.com/CharbelALHELOU/hanabi/blob/master/statistiques/statDirect.png)

  Donc cette manière de jouer n'est pas du tout pertinante, parce que si l'AI reçoit un indice sur un 5 il va le jouer tout de suite.Ce qui explique les chiffres obtenus.

# **IV- AI Hat Guessing Recommendation**
## **La stratégie**
  Cette IA s'appelle `recommendation_ai.py`

  Cette IA se base sur le jeu du hat guessing, présenté sur le pdf : https://sites.google.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attredirects=1. On attribue à chaque joueur une valeur correspondant au coup que l'on veut qu'il effectue. On fait la somme de ces numéros sur tous les joueurs visibles et cela nous donne un code correspondant à l'indice que l'on doit donner. Chaque joueur sait interpréter cet indice comme consigne individuelle car il voit les valeurs des autres joueurs et en déduit la sienne.

  Chaque joueur se base sur la valeur de son et joue celon les priorités suivantes :

  Si la recommendation la plus récente était de jouer une carte et qu'aucune carte n'a été jouée depuis le dernier indice, jouer la carte recommandée.
  Si la recommendation la plus récente était de jouer une carte et qu'une carte a été jouée depuis le dernier indice, et que les joueurs ont moins de 2 jetons rouges, jouer la carte recommandée.
  Si les joueurs ont un jeton bleu, donner un indice.
  Si la recommendation la plus récente était de défausser une carte, défausser la carte recommandée.
  Défausser la plus vieille carte de sa main (donc d'index 1).
## **Statistiques**
  Sur 1000 parties:

    ![stat1](https://github.com/CharbelALHELOU/hanabi/blob/master/stat/stat1.png)

  On remarque que l'AI a une moyenne légerement inférieur à celle marquée dans le document.

    ![stat2](https://github.com/CharbelALHELOU/hanabi/blob/master/stat/stat2.png)

  Une expliquation possible de cette différence est l'erreur suivante que nous avons rencontré:
  La partie continue même quand le deck est épuisé.

    ![error](https://github.com/CharbelALHELOU/hanabi/blob/master/stat/error.png)


# **Conclusion**
  En conclusion, une stratégie simple comme l'AI aléatoire ou direct ne pourront jamais se rapprocher d'un score maximal et même en utilisant des stratégie un peu plus réfléchie jouable par des humains on reste loin des 25 pts (en moyenne 18 pts) donc il nous faut des stratégies complexes comme la stratégie des Chapeaux pour se rapprocher un peu plus d'un score parfait.
