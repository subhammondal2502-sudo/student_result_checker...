#Q.1 student result checker .....
name=(input("enter your name :"))
math_marks=int(input("marks in mathematics :"))
physics_marks=int(input("marks in physics :"))
computer_marks=int(input("marks in computer science :"))
total_marks = (math_marks+physics_marks+computer_marks)
print("total marks :" , total_marks)
average=(total_marks)/3
print("average marks :" , average)
