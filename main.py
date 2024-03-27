import random

# this is where the dictionaries are entered and put into a long list called word_categories
def generate_categories():
    cars_category = {'category_name': 'cars', 'words': ['Ford', 'Honda', 'Kia', 'Toyota']}
    smelly_category = {'category_name': 'smelly', 'words': ['Stink', 'Rank', 'Reek', 'Stench']}
    leaderboard_category = {'category_name': 'leaderboard', 'words': ['podium', 'Placement', 'Score', 'grading']}
    video_games_category = {'category_name': 'videogames', 'words': ['Halo', 'Minecraft', 'Pokemon', 'Apex']}
    sports_category = {'category_name': 'balls','words':['basketball','soccer','hockey','cricket']}
    chocolate_category = {'category_name':'chocolate','words':['cabury','feastables','hershey','lint']}
    fruits_category = {'category_name':'fruits','words':['apple','orange','banana','pear']}
    elements_category = {'category_name':'elements','words':['fire','water','earth','air']}
    word_categories = [cars_category, smelly_category, leaderboard_category, video_games_category, sports_category, chocolate_category, fruits_category, elements_category]
    random.shuffle(word_categories)

    for category in word_categories:
        random.shuffle(category['words'])

    return word_categories

# this generates a 4x4 grid that just has numbers in it as placeholders
def generate_grid():
    return [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ]

# this will take all the categories and put the words within them into a long list called flattened words
# then this long list will be used to populate the empty grid
def populate_grid_with_words(categories, unpopulated_grid):

    # first of all, just pick 4 out of the x categories
    # then return them with the grid later
    select_four_categories = random.sample(range(0,len(categories)),4)

    chosen_categories = [categories[select_four_categories[0]],
                        categories[select_four_categories[1]],
                        categories[select_four_categories[2]],
                        categories[select_four_categories[3]]]
    
    flattened_words = [word for category in chosen_categories for word in category['words']]
    random.shuffle(flattened_words)

    for i in range(4):
        for j in range(4):
            unpopulated_grid[i][j] = flattened_words.pop(0)

    return chosen_categories, unpopulated_grid

# just takes the grid and makes it look nice
def make_grid_look_nice(populated_grid):
    for row in populated_grid:
        print("|", end=" ")  # Print the starting border of the row
        for cell in row:
            print(cell.center(12), end=" | ")  
        print()  # Move to the next line 

def check_guess(guesses,categories):
    for category in categories:
        if set(guesses) == set(category["words"]):
            return category
    return False
        


# setup the game

categories = generate_categories()
unpopulated_grid = generate_grid()
chosen_categories, populated_grid = populate_grid_with_words(categories, unpopulated_grid)

# main game 
print("\n\nWelcome to Connections!\n")
print("Try and guess sets of four words with a connection.")
print("You have 4 lives.\n")
lives = 4

while lives > 0:
    make_grid_look_nice(populated_grid) # print the grid
    guess = input("\nEnter your guess. Type four words seperated by a comma")
    guesses = guess.split(',')
    check = check_guess(guesses, categories)
    if check == False:
        print("Incorrect, You lose a life")
        lives = lives - 1
        print("You have ", lives, " remaining.")
    else:
        print("Correct, you found a category", check)
    









# #     # Check if the guess is correct
# #     if guess.lower() == 'quit':
# #         print("Thanks for playing!")
# #         break
# #     elif guess in guessed_words:
# #         print("You've already guessed that word. Try another one.")
# #         continue
# #     elif check_guess(guess, categories):
# #         print("Correct!")
# #         guessed_words.add(guess)
# #     else:
# #         print("Incorrect guess. Try again.")
# #         lives -= 1
# #         print("You have", lives, "lives remaining.")

# # # Game over
# # if lives == 0:
# #     print("\nGame over! You've run out of lives.")
