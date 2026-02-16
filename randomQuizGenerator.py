import random, os

os.chdir(r'C:\Users\Samuel\Desktop\Remote Job\practice\python\randomQuizGenerator')

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_no in range(2):
	# Create the quiz and answer key files.
 	quiz_file = open(f'capitalsquiz{quiz_no + 1}.txt', 'w', encoding='UTF-8')
 	answer_file = open(f'capitalsquiz_answers{quiz_no + 1}.txt', 'w', encoding='UTF-8')

 	# Write out the header for the quiz.
 	quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
 	quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_no + 1})')
 	quiz_file.write('\n\n')

 	# Shuffle the order of the states.
 	states = list(capitals.keys())
 	random.shuffle(states)

 	# Loop through all 50 states, making a question for each.
 	for num in range(50):

 		# Get right and wrong answers.
 		correct_answer = capitals[states[num]]
 		wrong_answers = list(capitals.values())
 		del wrong_answers[wrong_answers.index(correct_answer)]
 		wrong_answers = random.sample(wrong_answers, 3)
 		answer_options = wrong_answers + [correct_answer]
 		random.shuffle(answer_options)
 		quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
 		
 		for i in range(4):
 			quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n") 
 		quiz_file.write('\n')

 		# Write the answer key to a file.
 		answer_file.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}\n")
 	
 	quiz_file.close()
 	answer_file.close()

print(os.getcwd())
input()