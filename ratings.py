"""Restaurant rating lister."""


# put your code here
dict_restaurants = {}

def build_dict_restaurants(filename):
	"""Takes a file and creates a dictionary of restaurants as keys and ratings as values"""

	with open(filename) as restaurant_ratings:

		

		for line in restaurant_ratings:
			line = line.strip()
			line = line.split(":")

			dict_restaurants[line[0]] = line[1]
	
	return dict_restaurants



def print_restuarant_ratings(dictionary):
	"""Given a dictionary it alphebatizes the keys"""

	alpha_list = sorted(dictionary.keys())

	for restaurant in alpha_list: 
		print("{} is rated at {}".format(restaurant, dictionary[restaurant]))



def add_rating():
	"""add new entry into dictionary"""



	new_restaurant_name = input("What's your new restaurant? ")
	new_restaurant_score = input("What rating would you give it? ")

	dict_restaurants[new_restaurant_name] = dict_restaurants.get(new_restaurant_name, new_restaurant_score)

	print("Thank you for your rating!")









print_restuarant_ratings(build_dict_restaurants("scores.txt"))
add_rating()
print("Here is the new list of restaurant ratings.")
print_restuarant_ratings(dict_restaurants)