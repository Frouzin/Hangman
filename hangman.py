import re
from utils import get_random_word, get_total_tries, show_difficulty_menu

difficulty_settings = show_difficulty_menu()
selected_word = get_random_word(difficulty_settings)
total_tries = available_tries = get_total_tries(selected_word, difficulty_settings)
print(f"A quantidade de chance para advinhar a palavra é: {total_tries}")
current_state = ["_" for letter in selected_word]
guessed_letters = []

while "_" in current_state and available_tries:
    print(f"\n\n##tentativa numero {total_tries - available_tries + 1} de {total_tries} ##")
    for char in current_state:
        print(char, end=" ")

    guess = ""
    while not guess:
        guess = input("\nTente uma letra:").lower()
        if len(guess) != 1 and not re.match("[a-z]",guess):
            print("Invalido. tente novamente utilizando 1 letra.")
            guess = ""

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess in selected_word:
            positions = [m.start() for m in re.finditer(guess, selected_word)]

            for index in positions:
                current_state[index] = guess

        else:
                available_tries -= 1
    else:
        print(f"{guess} já foi usada.")
