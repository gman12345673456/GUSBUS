# def print_words_from_categories(word_catagories):
#     """
#     Loop through each category to print its words
#     """ 
#     for category in word_categories:
#         for word in category["word"]:
#             print(word)

# def setup_word_categories():
#     """
#     Initialiaze a list to store diffrent categories of words and define each
#     category with a descriptive name and a list of related words
#     """



word_categories = ( )  # set up an empty array for the word categories

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




numbers = ["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]



word_index = 0


# for loop repeats something X times

# print out each row, each of them one by one
for row in range(0,4): #repeat anything inside of me 4 times
    print(grid[row])

for row in grid:
    print(row[0])

# looping though every row and every column using nested for loops
for row in grid:
    for number in row:
        print(numbers)

for row in grid:
    print(row [0])





# find a way of putting each of the words in the categories into
# the grid



# print(grid)

# print(grid[0],[1],[2],[3])






