physics =int(input("marks obtained in physics:"))
chemistry=int(input("marks obtained in chemistry:"))
biology=int(input("marks obtained in biology:"))
mathematics=int(input("marks obtained in mathematics:"))
computer=int(input("marks obtained in computer:"))
totalmarks= physics+chemistry+biology+mathematics+computer
percentage=totalmarks/500*100

if percentage >=33:
     print(f"pass with{percentage}%")
     if percentage >=90:
         print("grade A")
     elif percentage >=80:
         print("grade B")
     elif percentage >=70:
         print("grade C")
     elif percentage >=60:
         print("grade D")
     elif percentage >=50:
         print("grade E")
     elif percentage >=40:
         print("grade F")
     elif percentage >=33:
         print("grade G")
else:
    print("failed with {pecentage}%")