import pickle

def find_absentees():
	# To retreive all students from the given division
	class_division = input("Enter the Division of the class (C or D): ")
	write_file = open("./global/9"+class_division+".obj", 'rb')
	all_students = pickle.load(write_file)

	# To read the contents from the given attendance list
	file_name = input("\nEnter the input filename: ")
	with open('./testing_data/'+file_name+'.csv', encoding='utf-16') as f:
		contents = f.read()

	# To traverse and get the names
	student_list = []
	for line in contents.split('\n'):
		items = line.split('\t')
		student_list.append(items[0])

	# To remove duplicates
	students_list = list(set(student_list[2:]))

	# To remove the empty string
	students_list.remove('')

	# To store the sorted list
	students_list = sorted(students_list)
	
	# To print the Absentees list
	print("\nAbsentees in Maths Class are:")
	for student in all_students:
		if(student not in students_list):
			print(student)

find_absentees()