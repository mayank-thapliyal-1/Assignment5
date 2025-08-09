dic = {'Alice':30,'Jack':60,'Rahul':70,'Ravi':80,'Raman':98}
name = input("Enter  The Student's name: ")
if(name in dic):
    print(name,"'s marks :",dic[name] )
else:
    print("Student not found")