#Author: Elise Merrifield
#CIS129 lab11
# Exercises 9.1, 9.2, 9.3

#9.1, Write grades to plain text file
#taking input for grades
def write_grades(filename):
    with open(filename, 'w') as file:
        while True:
            grade = input("Enter grades (or -1 to stop): ")
            if grade == '-1':
                break
            file.write(grade + '\n')
#creating file for use in "filename"
write_grades("grades.txt")

#9.2, Read grades from plain text file
def read_grades(filename):
    with open(filename, 'r') as file:
        grades = [int(line.strip()) for line in file]
    return grades

#9.3, Writing student records to a CSV file

import csv

def write_student_rec():
    # writes students records into csv file
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        #create header row
        writer.writerow(['firstname','lastname','exam1grade','exam2grade','exam3grade'])

        while True:
            # Get student info
            firstname = input("Enter student's first name: ")
            lastname = input("Enter student's last name: ")
            try:
                exam1grade = int(input("Enter student's exam 1 grade: "))
                exam2grade = int(input("Enter student's exam 2 grade: "))
                exam3grade = int(input("Enter student's exam 3 grade: "))
            except ValueError:
                print("Invalid input. Please enter numerical values for grades.")
                continue

            # write student info to csv file
            writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])

            # ask user if they would like to add another record
            another = input("Do you want to enter another record? (yes/no): ")
            if another.lower() != 'yes':
                break

write_student_rec()