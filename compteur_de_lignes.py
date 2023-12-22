#2. Compter le nombre de ligne dans un document
# En utilisant la méthode du test-driven development, écrire une fonction qui prend le chemin d’un
# fichier en paramêtre et retourne le nombre de lignes dans le document.

def count_number_of_line(filename: str) -> int:
    with open(filename, "rt") as file_:
        return file_.read().count("\n")




# Fixture pour créer un fichier temporaire

