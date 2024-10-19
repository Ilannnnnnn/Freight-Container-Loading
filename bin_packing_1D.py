import time

# Retourne le nombre de conteneurs nécessaires en utilisant l'algorithme First Fit online
def firstFit(width, n, c):

    # Initialiser le résultat (nombre de conteneurs)
    res = 0

    # Créer un tableau pour stocker l'espace restant dans les conteneurs
    # il peut y avoir au maximum n conteneurs
    bin_rem = [0]*n

    #Initialisation d'une variable pour calculer l'espace non occupé
    espace=0

    # Placer les articles un par un
    for i in range(n):

        # Trouver le premier conteneur qui peut accueillir width[i]
        j = 0
        while (j < res):
            if (bin_rem[j] >= width[i]):
                bin_rem[j] = bin_rem[j] - width[i]
                break
            j += 1

        # Si aucun conteneur ne peut accueillir width[i]
        if (j == res):
            bin_rem[res] = c - width[i]
            res = res + 1

    #Calcule de l'espace non occupé après chargement
    for i in range(n):
      espace = espace + bin_rem[i]
    
    print("Espace non occupé : ",espace, " m.") #Affichage de l'espace restant dans tous les conteneurs à la fin du chargement
    return res

# Retourne le nombre de conteneurs nécessaires en utilisant l'algorithme First Fit Decreasing en offline
def firstFitDec(width, n, c):

    # Trier d'abord tous les poids par ordre décroissant
    width.sort(reverse=True)

    # Maintenant, appeler First Fit pour les articles triés
    return firstFit(width, n, c)
    

# Programme principal
width = [10,9,7.5,1,2,11,3,3,3,4,5,6,7,5,6,5,4,7,9,3,5,6,7,3,1,2,4,6,7,9,6,3,3,4,5,6,6,7,6,7,8,8,8,5,2.2,4.2,3.7,5.6,4.9,8.7,6.1,3.3,2.6,2.9,2,3,6,5,4,6,4,2,4,6,6,3,4,4,2,6,2,4,5,5,4,6,3,3,3,5,5,6,5,3,5,6,6,3,5,3,4,3,3,5,3,4,4,2,2,6]
c = 11.583
n = len(width)
tps = time.time() # Relevé du temps avant l'exécution du programme
print("Nombre de conteneurs nécessaires en 'online' : ", str(firstFit(width, n, c)))
print("Temps d'exécution : ", time.time()-tps, " secondes") # Calcule et affiche le temps d'exécution
tps = time.time() # Relevé du temps avant l'exécution du programme
print("Nombre de conteneurs nécessaires en 'offline' : ", str(firstFitDec(width, n, c)))
print("Temps d'exécution : ", time.time()-tps, " secondes") # Calcule et affiche le temps d'exécution