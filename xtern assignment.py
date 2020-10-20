import pandas as pd
import csv
import math

data = pd.read_csv (r'C:\Users\Wojtek_ftw\Desktop\2020-XTern-DS.csv')


# Import CSV file and make 2d array with all the data
rows = [0]*2019
i = 0
with open(r'C:\Users\Wojtek_ftw\Desktop\2020-XTern-DS.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if(i != 0):
            rows[i-1] = row
        i += 1



# Get foods into list. index = 3 -----------------------------------------------------
# TODO Keep track of occurance
food_delimeter = ", " 
foods = []
for row in rows:
    exported_foods = (row[3]).split(food_delimeter)
    
    for food in exported_foods:
        if food not in foods:
            foods.append(food)
        else:
            l = 1
foods = sorted(foods)



# Get resturants and ratings ----------------------------------------------------------
# 3=rest, 6=rating, 7=votes
# rating = opening soon, new, -, #.#
# votes = - , ###
# restaurants format = [ID , rating , votes]
restaurants = []
for row in rows:
    exp_rest = row[0]
    exp_rating = row[6]
    exp_votes = row[7]
    rest_item = [exp_rest, exp_rating, exp_votes];
    restaurants.append(rest_item)



# Sort by rating -----------------------------------------------------------------------
# Remove entries with no ratings, occurs when "-", "NEW", or "Opening Soon" is the value
rest_rating_sort = []
for rest in restaurants:
    rating = rest[1]
    if (rating == "-") or (rating == "NEW") or (rating == "Opening Soon"):
        #Do nothing
        l = 1
    else:
        rest_rating_sort.append(rest)
rest_rating_sort = sorted(rest_rating_sort,key=lambda x: x[1])

#Get top 1% rated restaurants
num_rest = len(rest_rating_sort)
num_top = math.trunc(0.01 * num_rest)
i = 0
top_rating_rest = []
while i < num_top:
    rest = rest_rating_sort[num_rest - i - 1]
    top_rating_rest.append([rest[0],rest[1]])
    i += 1
print(top_rating_rest)



# Sort by voting -----------------------------------------------------------------------
rest_vote_sort = []
for rest in restaurants:
    rating = rest[2]
    if (rating == "-") or (rating == "NEW") or (rating == "Opening Soon"):
        #Do nothing
        l = 1
    else:
        rest_vote_sort.append(rest)
rest_vote_sort = sorted(rest_vote_sort,key=lambda x: int(x[2]))
# Get top 1% voted restaurants
num_rest = len(rest_vote_sort)
num_top = math.trunc(0.01 * num_rest)
i = 0
top_vote_rest = []
while i < num_top:
    rest = rest_vote_sort[num_rest - i - 1]
    top_vote_rest.append([rest[0],rest[2]])
    i += 1
print(top_vote_rest)



# Print results thus far
print("Served foods:")
for food in foods:
      print(food)
print("Top Rated Restaurant IDs and Ratings:")
for rest in top_rating_rest:
      print(rest[0] + " with a " + str(rest[1]) + " rating")
print("Top Voted Restaurant IDs and Vote Totals:")
for rest in top_vote_rest:
      print(rest[0] + " with " + str(rest[1]) + " customer votes")


# TODO
# Get ratings for foods
# Iterate over each row, see if food is there, get rating
