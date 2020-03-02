#TODO Make improovements and upload  
#Turning it into a function 

def reverse_function(input_string):
    #Code below goes in here to turn this into a function
    unreversed_str = input_string
    #Get the lengh of the string 
    strlength =  len(unreversed_str)

    #Reverse the string
    reversed_str = ""
    while strlength > 0:
        reversed_str = reversed_str + unreversed_str[strlength - 1] 
        strlength = strlength - 1

    return reversed_str

#Activating the function
reverse_word = reverse_function("wolan")
print(reverse_word)

