#TODO Make improovements and upload  
#Turning it into a function 

def reverse_function(input_string):
    #Code below goes in here to turn this into a function 

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

