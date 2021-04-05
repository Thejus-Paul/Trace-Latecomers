import pickle

def find_absentees():
  class_division = input("Enter the Division of the class (C or D): ")
  write_file = open("./global/9"+class_division+".obj", 'rb')
  students_list = pickle.load(write_file)
  file_name = input("\nEnter the input filename: ")
	f = open("./testing_data/"+file_name+".csv", encoding="utf-16")
	contents = f.read()
	current_session_list = []
	for line in contents.split('\n'):
		items = line.split('\t')
		current_session_list.append(items[0])
  print(current_session_list)

find_absentees()