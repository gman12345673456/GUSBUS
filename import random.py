import random

def generate_categories():
    word_categories = []

    cars_category = {
        'category_name': 'cars',
        'words' : ['Ford', 'Honda', 'Kia', 'Toyota']
    }

    smelly_category = {
        'category_name': 'smelly',
        'words': ['Stink', 'Rank', 'Reek', 'Stench']
    }

    leaderboard_category = {
        'category_name': 'leaderboard',
        'words' : ['podium', 'Placement', 'Score', 'grading']
    }

    video_games_category = {
        'category_name': 'videogames',
        'words' : ['Halo', 'Minecraft', 'Pokemon', 'Apex']
    }

    word_categories.append(cars_category)
    word_categories.append(smelly_category)
    word_categories.append(leaderboard_category)
    word_categories.append(video_games_category)

    # Shuffle the categories
    random.shuffle(word_categories)

    # Shuffle the words within each category
    for category in word_categories:
        random.shuffle(category['words'])

    return word_categories

def generate_grid():
    grid = [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ]

    return grid

def populate_grid_with_words(categories, unpopulated_grid):
    row = 0
    for category in categories:
        col = 0
        for word in category["words"]:
            unpopulated_grid[row][col] = word
            col += 1
        row += 1

    return unpopulated_grid

# Mainline
categories = generate_categories()
unpopulated_grid = generate_grid()
populated_grid = populate_grid_with_words(categories, unpopulated_grid)
print(populated_grid)

for i in populated_grid:
    print(i)

