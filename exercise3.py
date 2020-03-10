# problem - Take two comma seperated inputs from user, count the users name length and count the characar that user inputted with case insensitive count.
# Soluction
name , char = input("Enter comma separated name and character: ").split(",")
print (f"Length of your name is: {len(name)}") 
#print (f"Character count is: {name.lower().count(char.lower())}") 
print (f"Character count is: {name.strip().lower().count(char.strip().lower())}") # to avoid the spave issues while entering the data
# print(len(name)) print(len(char))
print(name.center(len(name)+8, "="))