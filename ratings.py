"""Restaurant rating lister."""


# put your code here

def build_dict_restaurants(filename, dictionary):
	"""Takes a file and creates a dictionary of restaurants as keys and ratings as values"""

	with open(filename) as restaurant_ratings:

		for line in restaurant_ratings:
			line = line.strip()
			line = line.split(":")

			dictionary[line[0]] = line[1]
	
	return dictionary



def print_restuarant_ratings(dictionary):
	"""Given a dictionary it alphebatizes the keys"""

	alpha_list = sorted(dictionary.keys())

	for restaurant in alpha_list: 
		print("{} is rated at {}".format(restaurant, dictionary[restaurant]))



def add_rating(dictionary):
	"""add new entry into dictionary"""

	new_restaurant_name = input("What's your new restaurant? ")
	new_restaurant_score = input("What rating would you give it? ")

	dictionary[new_restaurant_name] = dictionary.get(new_restaurant_name, new_restaurant_score)

	return dictionary
	#print("Thank you for your rating!")






# dict_restaurants = {}

def ratings_loop(fname):
	dict_restaurants = {}
	dict_restaurants = build_dict_restaurants(fname, dict_restaurants)
	print_restuarant_ratings(build_dict_restaurants(fname, dict_restaurants))
	add_rating(dict_restaurants)
	print("Here is the new list of restaurant ratings.")
	print_restuarant_ratings(dict_restaurants)

ratings_loop('scores.txt')

# dict[upper_version] = [rating, "string_user_input"]

# dict[upper][0] == rating
# dict[upper][1] == input

# sort(dict) => keys in actual sorted order
# dict[key][1] => printed version