print("Importing required libraries...", "\n")
import sqlite3, os
from tabulate import tabulate
print("Imported required libraries.", 2*"\n")


# the program can input items into a database or output meal ingredients or meals by ingredient or even meals by ingredients

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\mealIngredientsDatabase")


print("Connecting to the database...", "\n")
conn = sqlite3.connect("mealIngredientsDatabase.db", isolation_level =None)
print("Connected to the database", 2 * "\n")


print("Setting up the database...", "\n")
conn.execute("PRAGMA foreign_keys = ON")
conn.executescript("""
CREATE TABLE IF NOT EXISTS meals (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
) STRICT;

CREATE TABLE IF NOT EXISTS ingredients (
    name TEXT,
    meal_id INTEGER,
    PRIMARY KEY (name, meal_id),
    FOREIGN KEY(meal_id) REFERENCES meals(id)
) STRICT;
""")
print("Database ready!", 2 * "\n")

# Show current state of data base
def show_database():
	print("Showing current state of database")
	cursor = conn.execute('SELECT * FROM meals')
	headers = [description[0] for description in cursor.description]
	data = cursor.fetchall()
	print(tabulate(data, headers=headers, tablefmt='grid'), "\n")
	cursor = conn.execute('SELECT * FROM ingredients')
	headers = [description[0] for description in cursor.description]
	data = cursor.fetchall()
	print(tabulate(data, headers=headers, tablefmt='grid'), 2 * "\n")

show_database()
# istructions
print("""
The program will update the database if you give a meal and ingredients like so 
	'meal : ingredient1, ingredient2, ingredient3...' 
else the program wil determine if what you typed is a meal or an ingredient and look up the corresponding items
	input: 'rice'
	output: 'jollof rice, fried rice'
If you type 'quit', the program exits
If you type 'db' or 'show'or 'database', the program shows the database
""")
print()

user_input = ""

while not user_input == "quit":
	user_input = input(">>> ").strip().strip(",.:0!@#$%^&*-_=+").lower()

	# quit logic
	if user_input == "quit":
		conn.close()
		break
	
	# show database logic
	elif user_input == "show" or user_input == "database" or user_input == "db":
		show_database()
		continue


	#parse user_input
	elif len(user_input.split(":")) == 2:
		user_input = user_input.split(":")
		meal, ingredients = user_input
		
		ingredients = ingredients.strip().strip(".").split(",")
		if ingredients[0] == "" or meal == "":
			continue
		# update tables
		user_input = input(f">>> Are you sure you want to update database with meal: '{meal}' and ingredient(s): '{ingredients}' (y/n)?").strip().strip(",.:0!@#$%^&*-_=+").lower()
		if user_input == "y":
			print("\n", f"Updating database with meal: '{meal}' and ingredient(s): '{ingredients}'... ", "\n")
			# Try to insert meal, ignore if exists
			conn.execute("INSERT INTO meals (name) VALUES (?) ON CONFLICT(name) DO UPDATE SET name=excluded.name", (meal,))
			
			# Get the meal_id (whether just inserted or already existed)
			cursor = conn.execute("SELECT id FROM meals WHERE name = ?", (meal,))
			meal_id = cursor.fetchone()[0]
			for ingredient in ingredients:
				ingredient = ingredient.strip()
				conn.execute("INSERT INTO ingredients VALUES (?, ?) ON CONFLICT (name, meal_id) DO UPDATE SET name=excluded.name, meal_id=excluded.meal_id", (ingredient, meal_id))
		else:
			print()
			print("Come back when you're sure")
			print()
	else:
		meals = conn.execute("SELECT ingredients.name FROM meals INNER JOIN ingredients on meals.id = ingredients.meal_id WHERE meals.name = ?", (user_input,))
		meals_results = meals.fetchall()
		if len(meals_results) == 0:
			pass
		else:
			headers = [description[0] for description in meals.description]
			print(tabulate(meals_results, headers=headers, tablefmt='grid'), "\n")
			continue

		ingredients = conn.execute("SELECT meals.name FROM meals INNER JOIN ingredients on meals.id = ingredients.meal_id WHERE ingredients.name = ?", (user_input,))
		ingredients_results = ingredients.fetchall()
		if len(ingredients_results) == 0:
			print("'meal' or 'ingredient' not found", "\n")
			pass
		else:
			headers = [description[0] for description in ingredients.description]
			print(tabulate(ingredients_results, headers=headers, tablefmt='grid'), "\n")