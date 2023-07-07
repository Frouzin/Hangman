import random

difficulty_levels = {
    "1": "facil",
    "2": "normal",
    "3": "dificil"
}

words_length = {
    "1" : (3, 5),
    "2" : (6, 10),
    "3" : (11, 100)
}

print("Escolha o Nivel de Dificuldade:")
difficulty_settings = ""

while not difficulty_settings:
    
    for k,v in difficulty_levels.items():
        print(f"{k} - {v.upper()}")

    difficulty_settings = input("Escolha sua dificuldade:")
    
    if difficulty_settings not in difficulty_levels.keys():
        print(f"{difficulty_settings} nao é uma opção valida")
        difficulty_settings = ""


with open("static\words.txt", mode="r") as f_words:
    words = []
    for word in f_words.readlines():
        w = word.strip()
        min,max = words_length[difficulty_settings]

        if min <= len(w) <= max:
            words.append(w)

max_index = len(words)-1
random_index = random.randint(0,max_index)
selected_word = words[random_index]

print(selected_word)

total_tries = 2* len(selected_word)
if difficulty_settings == "1":
    total_tries += 2
elif difficulty_settings == "3":
    total_tries -= 2

print(f"A quantidade de chance para advinhar a palavra é: {total_tries}")