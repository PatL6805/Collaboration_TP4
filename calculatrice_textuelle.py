#1. Créez une fonction add qui prend un str et renvoie un str:
#   1) La méthode peut prendre 0, 1 ou 2 nombres séparés par une virgule, et renvoie leur somme.
#   2) Une chaîne vide renverra “0”.
def add(numbers_str)-> str:
    # condition si le nombre n'est pas un nombre retourner 0
    if not numbers_str:
        return "0"
    # si c'est une chaine vide (sans nombre et sans rien) retourner 0
    if numbers_str == '':
        return "0"
    # si ce sont des nombres en string séparer les nombres qui sont à coté d'une virgule
    numbers_list = numbers_str.split(",")
    # compteur ou le resultat la somme est initialisé à 0
    somme = 0
    # pour tous les nombres dans la liste des nombres on additionne chaque nombres à la somme des nombres précédents
    for number in numbers_list:
        somme += int(number)
    # on retourne le resultat (la somme) qui est un nombre en string
    return str(somme)


#2. (Plusieur nombres) Permettre à la fonction de gérer un nombre arbitraire de nombres à l’entrée.
def add_many(number_str)-> str:
    # On sépare les nombres les un des autres si si il ya une "," entre eux
    number_list = number_str.split(",")
    # Notre résultat (somme) commence par le nombre à la premiere position de notre liste
    somme = int(number_list[0])
    # On recherche tous le nombres de chaque positions de notre listes pour ensuite les additionner à la somme du nombre précédent
    for position in range(1, len(number_list)):
        somme += int(add(number_list[position]))
    # on retourne la somme qui est un nombre en string
    return str(somme)


#3. Permettre à la fonction de gérer les nouvelles lignes comme séparateurs.
def add_return(number_str):
    # on retourne la fonction add mais en changeant les nombres en parametres qui sont séparés par une "," en remplacant la virgule par \n
    return add(number_str.replace("\n", ","))


#4. (Nombre manquant à la dernière position) Permettre que l’entrée finisse par un séparateur.
def add_float_end(number_str)-> str:
    # condition: si la derniere position de la liste (-1) est une ",", on retourne la fonction add() avec tous les nombre jusqu'à la derniere position (-1) en parametre
    if number_str[-1] == ",":
        return add_return(number_str[:-1])
    # on execute la fonction add() qui est la somme des number_str
    return add_return(number_str)

