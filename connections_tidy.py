
# import random

# def generate_categories():
#     cars_category = {'category_name': 'cars', 'words': ['Ford', 'Honda', 'Kia', 'Toyota']}
#     smelly_category = {'category_name': 'smelly', 'words': ['Stink', 'Rank', 'Reek', 'Stench']}
#     leaderboard_category = {'category_name': 'leaderboard', 'words': ['podium', 'Placement', 'Score', 'grading']}
#     video_games_category = {'category_name': 'videogames', 'words': ['Halo', 'Minecraft', 'Pokemon', 'Apex']}
#     sports_category = {'category_name': 'balls','words':['basketball','soccer','hockey','cricket']}
#     chocolate_category = {'category_name':'chocolate','words':['cabury','feastables','hershey','lint']}

#     word_categories = [cars_category, smelly_category, leaderboard_category, video_games_category, sports_category, chocolate_category]
#     random.shuffle(word_categories)

#     for category in word_categories:
#         random.shuffle(category['words'])

#     return word_categories

# def generate_grid():
#     return [
#         ["1", "2", "3", "4"],
#         ["5", "6", "7", "8"],
#         ["9", "10", "11", "12"],
#         ["13", "14", "15", "16"],
#     ]

# def populate_grid_with_words(categories, unpopulated_grid):
#     flattened_words = [word for category in categories for word in category['words']]
#     random.shuffle(flattened_words)

#     for i in range(4):
#         for j in range(4):
#             unpopulated_grid[i][j] = flattened_words.pop(0)

#     return unpopulated_grid

# # Mainline
# categories = generate_categories()
# unpopulated_grid = generate_grid()
# populated_grid = populate_grid_with_words(categories, unpopulated_grid)

# # Print the populated grid in a tidy format
# for row in populated_grid:
#     print(" ".join(row))

# # Mainline
# categories = generate_categories()
# unpopulated_grid = generate_grid()
# populated_grid = populate_grid_with_words(categories, unpopulated_grid)

# # Print the populated grid in a grid format in the terminal
# for row in populated_grid:
#     print("|", end=" ")  # Print the starting border of the row
#     for cell in row:
#         print(cell.center(12), end=" | ")  # Adjust the width as needed
#     print()  # Move to the next line for the next row


# print("Welcome to connections")
# print("Please type 4 words that you think would be in a categorie")

import random

def generate_categories():
    cars_category = {'category_name': 'cars', 'words': ['Ford', 'Honda', 'Kia', 'Toyota']}
    smelly_category = {'category_name': 'smelly', 'words': ['Stink', 'Rank', 'Reek', 'Stench']}
    leaderboard_category = {'category_name': 'leaderboard', 'words': ['podium', 'Placement', 'Score', 'grading']}
    video_games_category = {'category_name': 'videogames', 'words': ['Halo', 'Minecraft', 'Pokemon', 'Apex']}
    sports_category = {'category_name': 'balls','words':['basketball','soccer','hockey','cricket']}
    chocolate_category = {'category_name':'chocolate','words':['cabury','feastables','hershey','lint']}

    word_categories = [cars_category, smelly_category, leaderboard_category, video_games_category, sports_category, chocolate_category]
    random.shuffle(word_categories)

    for category in word_categories:
        random.shuffle(category['words'])

    return word_categories

def generate_grid():
    return [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ]

def populate_grid_with_words(categories, unpopulated_grid):
    flattened_words = [word for category in categories for word in category['words']]
    random.shuffle(flattened_words)

    for i in range(4):
        for j in range(4):
            unpopulated_grid[i][j] = flattened_words.pop(0)

    return unpopulated_grid

# Mainline
categories = generate_categories()
unpopulated_grid = generate_grid()
populated_grid = populate_grid_with_words(categories, unpopulated_grid)


for row in populated_grid:
    print(" ".join(row))


categories = generate_categories()
unpopulated_grid = generate_grid()
populated_grid = populate_grid_with_words(categories, unpopulated_grid)


for row in populated_grid:
    print("|", end=" ")  # Print the starting border of the row
    for cell in row:
        print(cell.center(12), end=" | ")  
    print()  # Move to the next line 

# import random

# def generate_categories():
#     cars_category = {'category_name': 'cars', 'words': ['Ford', 'Honda', 'Kia', 'Toyota']}
#     smelly_category = {'category_name': 'smelly', 'words': ['Stink', 'Rank', 'Reek', 'Stench']}
#     leaderboard_category = {'category_name': 'leaderboard', 'words': ['podium', 'Placement', 'Score', 'grading']}
#     video_games_category = {'category_name': 'videogames', 'words': ['Halo', 'Minecraft', 'Pokemon', 'Apex']}
#     sports_category = {'category_name': 'balls','words':['basketball','soccer','hockey','cricket']}
#     chocolate_category = {'category_name':'chocolate','words':['cabury','feastables','hershey','lint']}

#     word_categories = [cars_category, smelly_category, leaderboard_category, video_games_category, sports_category, chocolate_category]
#     random.shuffle(word_categories)

#     for category in word_categories:
#         random.shuffle(category['words'])

#     return word_categories

# def generate_grid():
#     return [
#         ["1", "2", "3", "4"],
#         ["5", "6", "7", "8"],
#         ["9", "10", "11", "12"],
#         ["13", "14", "15", "16"],
#     ]

# def populate_grid_with_words(categories, unpopulated_grid):
#     flattened_words = [word for category in categories for word in category['words']]
#     random.shuffle(flattened_words)

#     for i in range(4):
#         for j in range(4):
#             unpopulated_grid[i][j] = flattened_words.pop(0)

#     return unpopulated_grid

# def check_guess(guess, categories):
#     for category in categories:
#         if guess.capitalize() in category['words']:
#             return True
#     return False

# # Mainline
# categories = generate_categories()
# unpopulated_grid = generate_grid()
# populated_grid = populate_grid_with_words(categories, unpopulated_grid)

# # Game setup
# lives = 4
# guessed_words = set()

# print("Welcome to Connections!")
# print("You have 4 lives. Guess words related to the categories.")
# print("Type 'quit' to exit.")

# # Game loop
# while lives > 0:
#     # Print the grid
#     print("\nGrid:")
#     for row in populated_grid:
#         print("|", end=" ")
#         for cell in row:
#             print(cell.center(12), end=" | ")
#         print()

#     # Ask for a guess
#     guess = input("\nEnter your guess: ").strip().capitalize()

#     # Check if the guess is correct
#     if guess.lower() == 'quit':
#         print("Thanks for playing!")
#         break
#     elif guess in guessed_words:
#         print("You've already guessed that word. Try another one.")
#         continue
#     elif check_guess(guess, categories):
#         print("Correct!")
#         guessed_words.add(guess)
#     else:
#         print("Incorrect guess. Try again.")
#         lives -= 1
#         print("You have", lives, "lives remaining.")

# # Game over
# if lives == 0:
#     print("\nGame over! You've run out of lives.")
