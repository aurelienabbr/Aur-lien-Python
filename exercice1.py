from itertools import permutations

def lire_fichier(nom_fichier, separateur=' '):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read() #renvoie un texte avec \n entre chaque mot
    liste_mots = contenu.split("\n") #on crééer la liste de mots avec \n en séparateur
    return liste_mots
dico=lire_fichier("frenchssaccent.dic") #création de notre liste de mots provenant du fichier frenchssaccent
tirage = ['e', 'c', 'v', 'a','b','j','c'] #tirage aléatoire 
n=len(dico)
def combinaison(liste_lettre):
    mots_possibles=[]
    for k in range(2,len(tirage)): #création de toute les combinaisons de toute les tailles possibles
                perm=permutations(tirage,k) # création d'un générateur permutation
                liste_permutations=list(perm) # on le change en liste de tuple (par exemple pour tirage=['a,'b','c'] va crééer la liste[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')])
                mots = [''.join(t) for t in liste_permutations]  #change la liste de tuples en liste de mots (ex change la liste précédente en ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])            
                m=len(mots)
                for i in range(m):
                        if mots[i] in dico: #on vérifie que nos mots sont dans le dico
                            mots_possibles.append(mots[i])
    return(mots_possibles)

def plus_long_mot(tirage):
    mots_possibles=combinaison(tirage)
    if mots_possibles == []:
        return('pas de mots')
    return(mots_possibles[-1]) #renvoie le dernier élément de la liste des mots possible
    
