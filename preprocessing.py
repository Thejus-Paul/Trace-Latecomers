import pickle 

def save_to_file(students_list):
	filename = input("Enter the output filename: ")
	write_file = open("./global/"+filename+".obj", 'wb')
	pickle.dump(students_list, write_file)
	print("\nSaving to the File...COMPLETE")

def preprocessing():
	filename = input("\nEnter the input filename: ")
	with open('./testing_data/'+filename+'.csv', encoding='utf-16') as f:
		contents = f.read()

	# To traverse and get the names
	student_list = []
	for line in contents.split('\n'):
		items = line.split('\t')
		student_list.append(items[0])

	# To remove duplicates
	students_list = list(set(student_list))

	# To remove the empty string
	students_list.remove('')

	# To store the sorted list
	students_list = sorted(students_list)
	print("\nGenerating Student List...COMPLETE\n")

	# To save the processed list to a file
	save_to_file(students_list)

preprocessing()