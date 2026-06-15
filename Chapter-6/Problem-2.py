# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


# max_marks = float(input("Enter maximum marks per subject: "))

# sub1 = float(input("Enter marks of Subject 1: "))
# sub2 = float(input("Enter marks of Subject 2: "))
# sub3 = float(input("Enter marks of Subject 3: "))

# total_obtained = sub1 + sub2 + sub3
# total_maximum = 3 * max_marks

# percentage = (total_obtained / total_maximum) * 100

# minimum_subject_marks = 0.33 * max_marks

# if percentage >= 40 and sub1 >= minimum_subject_marks and sub2 >= minimum_subject_marks and sub3 >= minimum_subject_marks:
#     print("Pass")
# else:
#     print("Fail")

# print("Percentage:", percentage)


subject1= int(input("Enter the marks of the subject1:"))
subject2= int(input("Enter the marks of the subject2:"))
subject3= int(input("Enter the marks of the subject3:"))

total_average= (subject1+subject2+subject3)/3

if(total_average>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("Pass")
else:
    print("Fail")
                    
                    
                    
