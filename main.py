import pickle
from tkinter import *
import tkinter as tk

def find_latecomers(file_name,due_time):
	due_time = due_time.split(":")
	due_time = due_time[0]+due_time[1]

	# To read the contents from the given attendance list
	#file_name = input("\nEnter the input filename: ")
	with open('./'+file_name+'.csv', encoding='utf-16') as f:
		contents = f.read()

	# To traverse and get the names
	ontime_students = []
	late_students = []
	for line in contents.split('\n'):
		items = line.split('\t')
		if((len(items)>= 3) and items[1].split(" ")[0] == "Joined"):
			time = (items[2].split(" ")[1])[:-3].split(":")
			time = time[0] + time[1]
			if((int(time) > int(due_time)) and (items[0] not in ontime_students)):
				late_students.append(items[0])
			elif((int(time) <= int(due_time))):
				ontime_students.append(items[0])
	# To remove duplicates
	late_students = list(set(late_students))

	# To store the sorted list
	late_students = sorted(late_students)
	
	# To print the Absentees list
	res = "\n\nLatecomers in Maths Class are:"
	for student in late_students:
		res += "\n"+ student
	return(res)

def find_absentees(class_division,file_name):
	# To retreive all students from the given division
	#class_division = input("Enter the Division of the class (C or D): ")
	write_file = open("./global/"+class_division+".obj", 'rb')
	all_students = pickle.load(write_file)

	# To read the contents from the given attendance list
	#file_name = input("\nEnter the input filename: ")
	with open('./'+file_name+'.csv', encoding='utf-16') as f:
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
	res = "Absentees in Maths Class are:"
	for student in all_students:
		if(student not in students_list):
			res += "\n"+ student
	return(res)

# create root window
root = Tk()
root.title("Trace Latecomers")
root.geometry('555x620')
 
# adding a label to the root window
division_lbl = Label(root, text = "Enter the Class and Division (eg: 10C, 10D): ")
division = Entry(root, width=23)
division_lbl.grid(column=0, row=0, sticky = W+E, pady = 4)
division.grid(column=1, row=0, sticky = W+E, pady = 4)

# To enter the filename generated by MS Teams
filename_lbl = Label(root, text="Enter the Filename (eg: meetingAttendanceList): ")
filename = Entry(root, width=30)
filename_lbl.grid(column=0, row=1, sticky = W+E, pady = 2)
filename.grid(column=1, row=1, sticky = W+E, pady = 2)

# To enter the due time
time_lbl = Label(root, text="Enter the due time (eg: 7:50, 9:45): ")
time = Entry(root, width=23)
time_lbl.grid(column=0, row=2, sticky = W+E, pady = 2)
time.grid(column=1, row=2, sticky = W+E, pady = 2)

# Output text
output = Text(root, height = 33, width = 69)
output.grid(column=0, row=4, sticky=W+E, rowspan=10, columnspan=2, pady=3)

# Resets and prints the result
def clicked():
	output.delete("1.0","end")
	absentees = find_absentees(division.get(),filename.get())
	latecomers = find_latecomers(filename.get(),time.get())
	output.insert(tk.END, absentees)
	output.insert(tk.END, latecomers)
 
btn = Button(root, text="TRACE" ,fg="black", command=clicked)
btn.grid(column=0, row=3, sticky=W+E, columnspan=2, pady=2)
 
# Running the GUI
root.mainloop()