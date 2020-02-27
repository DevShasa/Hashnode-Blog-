#TODO let us reverse a string in python 

#Step one, input the string
normal_string = input('Enter string here: ')

#Step two, get the lenght of the entered string
str_length = len(normal_string)

#Use a while loop to reverse the string 
reverse = ''
while str_length > 0:
    reverse = reverse + normal_string[str_length -1]
    #The loop increments downwards 
    str_length = str_length -1

print(reverse)

#Implementing the same using a for loop 
