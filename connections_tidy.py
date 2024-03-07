def generate_categories():
    word_categories = []  # set up an empty array for the word categories

    # establish 4 word categories (cars, smelly, leaderboard, videogames)

    cars_category = {
    'category_name': 'lazy',
    'words' : ['Ford', 'Honda','Kia','Toyota']
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

    # put each category in the word category list that i made above
    # append means add to the end of  
    word_categories.append(cars_category) 
    word_categories.append(smelly_category) 
    word_categories.append(leaderboard_category) 
    word_categories.append(video_games_category) 

    return word_categories

def generate_grid():
    # establish a 4x4 grid 
    grid = [
    ["1","2","3","4"],
    ["5","6","7","8"],
    ["9","10","11","12"],
    ["13","14","15","16"],
    ]

    return grid 

def populate_grid_with_words(categories, unpopulated_grid):
    row = 0
    for category in categories:
        col = 0
        for word in category["words"]:
            # put word in correct grid location
            unpopulated_grid[row][col] = word
            col = col + 1
        row = row + 1
    
    return unpopulated_grid


# mainline 



categories = (generate_categories())
unpopulated_grid = generate_grid()
populated_grid = populate_grid_with_words(categories,unpopulated_grid)
print(populated_grid)

for i in populated_grid:
    print(i)

