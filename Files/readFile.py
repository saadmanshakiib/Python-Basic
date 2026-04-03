print("Welcome to files")
with open("/Users/saadman/Desktop/PROGRAMMING/Python3/Files/sakib.txt","w") as file:
    file.write("Failure")
   
with open("/Users/saadman/Desktop/PROGRAMMING/Python3/Files/sakib.txt") as file:    
    print(file.read())

