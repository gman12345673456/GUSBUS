#def generate_categories():
    #word_categories = []  # set up an empty array for the word categories

    # establish 4 word categories (cars, smelly, leaderboard, videogames)

    #cars_category = {
    #'category_name': 'lazy',
    #'words' : ['Ford', 'Honda','Kia','Toyota']
    #}

    #smelly_category = {
       # 'category_name': 'smelly',
       # 'words': ['Stink', 'Rank', 'Reek', 'Stench']
    #}

    #leaderboard_category = {
    #'category_name': 'leaderboard',
    #'words' : ['podium', 'Placement', 'Score', 'grading']
    #}

    #video_games_category = {
    #'category_name': 'videogames',
    #'words' : ['Halo', 'Minecraft', 'Pokemon', 'Apex']
    #}

    # put each category in the word category list that i made above
    # append means add to the end of  
    #word_categories.append(cars_category) 
   #word_categories.append(smelly_category) 
   # word_categories.append(leaderboard_category) 
    #word_categories.append(video_games_category) 

    #return word_categories

#def generate_grid():
    # establish a 4x4 grid 
    #["1","2","3","4"],
    #["5","6","7","8"],
    #["9","10","11","12"],
    #["13","14","15","16"],
    #]

    #return grid 

#def populate_grid_with_words(categories, unpopulated_grid):
    #row = 0
    #for category in categories:
        #col = 0
        #for word in category["words"]:
            # put word in correct grid location
           # unpopulated_grid[row][col] = word
            #col = col + 1
        #row = row + 1
    
    #return unpopulated_grid


# mainline 



#categories = (generate_categories())
#unpopulated_grid = generate_grid()
#populated_grid = populate_grid_with_words(categories,unpopulated_grid)
#print(populated_grid)

#for i in populated_grid:
    #print(i)
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

# Print the populated grid in a tidy format
for row in populated_grid:
    print(" ".join(row))

# Mainline
categories = generate_categories()
unpopulated_grid = generate_grid()
populated_grid = populate_grid_with_words(categories, unpopulated_grid)

# Print the populated grid in a grid format in the terminal
for row in populated_grid:
    print("|", end=" ")  # Print the starting border of the row
    for cell in row:
        print(cell.center(12), end=" | ")  # Adjust the width as needed
    print()  # Move to the next line for the next row

# import random

# def generate_categories():
#     animals_category = {'category_name': 'animals', 'words': ['Lion', 'Elephant', 'Giraffe', 'Tiger']}
#     colors_category = {'category_name': 'colors', 'words': ['Red', 'Blue', 'Green', 'Yellow']}
#     countries_category = {'category_name': 'countries', 'words': ['USA', 'Japan', 'France', 'Brazil']}
#     fruits_category = {'category_name': 'fruits', 'words': ['Apple', 'Banana', 'Orange', 'Grape']}

#     word_categories = [animals_category, colors_category, countries_category, fruits_category]
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

# def print_tidy_grid(grid):
#     for row in grid:
#         print(" ".join(row))

# def print_grid(grid):
#     for row in grid:
#         print("|", end=" ")  # Print the starting border of the row
#         for cell in row:
#             print(cell.center(12), end=" | ")  # Adjust the width as needed
#         print()  # Move to the next line for the next row

# def main():
#     categories = generate_categories()
#     unpopulated_grid = generate_grid()
#     populated_grid = populate_grid_with_words(categories, unpopulated_grid)

#     # Print the populated grid in a tidy format
#     print("Populated Grid:")
#     print_tidy_grid(populated_grid)

#     print("\nCategories:")
#     for category in categories:
#         print(f"{category['category_name']}: {', '.join(category['words'])}")

#     print("\nFind connections between words from different categories!")

# if __name__ == "__main__":
#     main()
