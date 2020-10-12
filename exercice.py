#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        for i in range(10):
            values.append(input(f"Entrez la valeur #{i+1} : "))

    for i in range(10):
        for j in range(i+1, len(values)):
            if values[i] > values[j]:
                temp = values[j]
                values[j] = values[i]
                values[i] = temp

    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        return False
    
    word1 = words[0]
    word2 = words[1]
    letters_word1 = [i for i in word1]
    for i in word2:
        if i not in letters_word1:
            return False

    return True


def contains_doubles(items: list) -> bool:
    
    for i in range(len(items)):
        if items[i] in items[i+1:]:
            return True

    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    maximum = 0
    best_student = None
    
    for student, grades in student_grades.items():

        student_grades[student] = sum(grades)/len(student_grades[student]) 

        if student_grades[student] > maximum:
            maximum = student_grades[student]
            best_student = {student : student_grades[student]}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    occ_dict = {}

    for i in sentence:
        if i.isalpha():
            occ_dict = occ_dict.get(i, 0) + 1

    h


    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
