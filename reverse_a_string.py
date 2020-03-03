#Function that will reverse a string when called 
def reverse_function(input_string):
    unreversed_str = input_string

    #Get the lengh of the string 
    strlength =  len(unreversed_str)

    #Reverse the string using a while loop 
    reversed_str = ""
    while strlength > 0:
        reversed_str = reversed_str + unreversed_str[strlength - 1] 
        strlength = strlength - 1

    return reversed_str

#Activating the function
reverse_word = reverse_function("Reverse this")
print(reverse_word)

