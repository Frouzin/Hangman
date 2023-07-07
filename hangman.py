import random
from constants import DIFFICULTY_LEVELS, WORDS_LENGTH

def show_difficulty_menu():
    """MENU DE DIFICULDADE"""
    print("Escolha o Nivel de Dificuldade:")
    difficulty_settings = ""

    while not difficulty_settings:
        
        for k,v in DIFFICULTY_LEVELS.items():
            print(f"{k} - {v.upper()}")

        difficulty_settings = input("Escolha sua dificuldade:")
        
        if difficulty_settings not in DIFFICULTY_LEVELS.keys():
            print(f"{difficulty_settings} nao é uma opção valida")
            difficulty_settings = ""

    return difficulty_settings

def get_random_word(difficulty_settings):
    """SELECIONA UMA PALAVRA ALEATORIA EM RELAÇÃO AO NIVEL DE DIFICULDADE"""
    with open("static\words.txt", mode="r") as f_words:
        words = []
        for word in f_words.readlines():
            w = word.strip()
            min,max = WORDS_LENGTH[difficulty_settings]

            if min <= len(w) <= max:
                words.append(w)

    max_index = len(words)-1
    random_index = random.randint(0,max_index)
    selected_word = words[random_index]

    print(selected_word)
    return selected_word


def get_total_tries(selected_word, difficulty_settings):
    """EXIBE O TOTAL DE TENTATIVAS PARA RESOLVER O PROBLEMA"""
    total_tries = 2* len(selected_word)
    if difficulty_settings == "1":
        total_tries += 2
    elif difficulty_settings == "3":
        total_tries -= 2

    print(f"A quantidade de chance para advinhar a palavra é: {total_tries}")