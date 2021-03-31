


""" PLAIN ENGLISH 
create a list to store 5 numvers (float)
caputre user input 5 times for their grades
each time we capture a user'sinput we append to the list
sort the list ascending, then splice the items at index 2
once we have three highest number in the list, we sum and divide up by 3
output a message to the user
end
"""

""" PSUDOCODE
creat list 

caputre input 
append number to list 

caputre input 
append number to list 

caputre input 
append number to list 

caputre input 
append number to list 

caputre input 
append number to list 

sort the list, then splice out the two lowest numbers

print message to user 
""" 

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]
grades = sum(grades)
result = grades / 3

print("Average Grade {0:.2f}%".format(result))
