import random

difficulty_levels = {
    "1": "facil",
    "2": "normal",
    "3": "dificil"
}

print("Escolha o Nivel de Dificuldade:")
difficulty_settings = ""
while not difficulty_settings:
    for k,v in difficulty_levels.items():
        print(f"{k} - {v.upper()}")

    difficulty_settings = input("Escolha sua dificuldade:")
    
    if difficulty_settings not in difficulty_levels.keys():
        difficulty_settings = ""


with open("static\words.txt", mode="r") as f_words:
    words = []
    for words in f_words.readlines():
        words.append(words.strip())

max_index = len(words)-1
random_index = random.randint(0,max_index)
selected_word = words[random_index]