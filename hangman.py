import random

print("Escolha o Nivel de Dificuldade:")
dif

with open("static\words.txt", mode="r") as f_words:
    words = []
    for words in f_words.readlines():
        words.append(words.strip())

max_index = len(words)-1
random_index = random.randint(0,max_index)
selected_word = words[random_index]