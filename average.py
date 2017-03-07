""" This program calculates the average of the notes that you have """

# this funtion calculates the average of a list of notes
def cal_average(*args):
	sum_average = 0

	# loop for each note in the list
	for note in args:
		sum_average += note # it sums all the elements

	average = "{0:.2f}".format(sum_average / len(args))# We divide and format to two decimals
	return average


num_notes = int(input("Input the quantity of notes: "))# we see how many notes the user has
notes = []

# loop for inputting notes of the user
for i in range(num_notes):
	notes.append(int(input("Please, input the note: ")))

# call funtion
print(cal_average(notes))