#Q.1 student result checker .....
name=(input("enter your name :"))
bengali=int(input("enter marks in bengali :"))
english=int(input("enter marks in english :"))
mathematics=int(input("enter marks in mathematics :"))
science=int(input("enter marks in physics :"))
computer=int(input("enter marks in computer :"))
total_marks = (bengali + english + mathematics + science + computer)
average=float(total_marks / 5)
if bengali<0 or bengali>100 or english<0 or english>100 or mathematics<0 or mathematics>100 or science<0 or science>100 or computer<0 or computer>100 :
    print("invalid marks")
else:
    if(bengali<33 or english<33 or mathematics<33 or science<33 or computer<33):
        print("result : fail")  
    else:
         print("result : pass") 
    if(average>=60):
        print("result : excellent")
    elif(average>=50):
        print("result : very good")
    elif(average>=40):
        print("result : good")
    elif(average>=30):
        print("result : pass")
    else:
        print("result : fail")
