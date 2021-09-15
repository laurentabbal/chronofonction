# Estimer la durée moyenne d'éxécution d'une fonction sur une machine.

# Import du module "time" afin d'avoir accès à la méthode "time()"
import time


# La fonction ci-dessous donne la moyenne des éléments d'une liste de nombres.
# Utilisation de préconditions avec "assert".

def moyenne(ma_liste):
    # On vérifie que l'argument est bien une liste.
    assert(isinstance(ma_liste, list)), "Il n'y a pas de liste !"
    # On vérifie que la liste n'est pas vide.
    assert(len(ma_liste) != 0), "La liste est vide !"
    # On vérifie que tous les éléments de la liste sont bien des nombres.
    for elem in ma_liste:
        assert(isinstance(elem, int) or isinstance(elem, float)), "Un élément n'est pas un nombre !"

    # Le calcul de la moyenne en lui-même
    somme = 0
    for i in range(0, len(ma_liste)):
        somme = somme + ma_liste[i]
    return somme/len(ma_liste)


# La fonction "duree_execution_moyenne" ci-dessous estime la durée moyenne
# d'exécution d'une fonction. Trois arguments à cette fonction :
#   - prog : le nom de la fonction dont on veut estimer la durée d'exécution ;
#   - args_prog : les arguments de la fonction ci-dessus sous forme de liste ;
#   - n : le nombre d'exécutions souhaitées pour l'estimation de la moyenne.
# Si vous voulez tester la durée d'une fonction "bidule" possedant deux
# arguments : par exemple tester la durée de "bidule(2, -8)" sur 1000
# exécutions, vous devez écrire "duree_execution_moyenne(bidule, [2, -8], 1000)"
# dans votre programme principal.


def duree_execution_moyenne(prog, args_prog, n):

    durees = []

    def duree_une_execution(prog):
        depart = time.time()    # top départ !
        prog(*args_prog)        # on passe la liste d'arguments à la fonction
        duree = time.time() - depart  # durée d'exécution.
        return duree

    for i in range(0, n):
        durees.append(duree_une_execution(prog))
    return moyenne(durees)
