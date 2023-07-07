from utils import get_random_word, get_total_tries, show_difficulty_menu

difficulty_settings = show_difficulty_menu()
selected_word = get_random_word(difficulty_settings=difficulty_settings)
get_total_tries(selected_word=selected_word,difficulty_settings=difficulty_settings)
