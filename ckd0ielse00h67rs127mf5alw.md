## #CodeChallenges Check if a word is a palindrome in Python

One of the common code challenges that you might encounter is to write code that checks whether a word is a palindrome. A palindrome is a word that reads the same from left to right and right to left. This code snippet will show you one of the ways to check if a word is a palindrome in python. 

One of the ways to approach the code challenge is by first reversing the word, then after reversing compare the reversed word with the original word, if the two are the same then the word is a palindrome. 

Reversing the word 
```
    input_word = word
    #Get the lenghth of the word 
    word_lenght =  len(input_word)
    #Initialize empty string to put reversed word 
    reversed_word = ''
    #Use a while loop to reverse the word 
    while word_lenght > 0:
        reversed_word = reversed_word + input_word[word_lenght - 1]
        word_lenght = word_lenght - 1  

``` 
In the code snippet I first got the length of the word string using the len() function. The while loop then rebuilds the word beginning with the last digit. The length of the string guides the while loop, ensuring a complete reversal. With each pass of the while loop, it decrements the word length by one, this enables the loop to move through each letter of the word in reverse while saving each letter in reversed_word, hence rebuilding the word in reverse 

The next step in is comparing the reversed word with the original word, if the two are the same then the word is a palindrome
```
    if reversed_word == input_word:
        print('The word', input_word, 'Is a palindrome')
    else:
        print('The word', input_word, 'Is not a palindrome')
```
The whole code 
```
def palindrome_checker(word):
    #STEP ONE, reverse the word
    input_word = word
    #Get the lenght of the word 
    word_lenght =  len(input_word)
    #Initialize empty string to put reversed word 
    reversed_word = ''
    #Use a while loop to reverse the word 
    while word_lenght > 0:
        reversed_word = reversed_word + input_word[word_lenght - 1]
        word_lenght = word_lenght - 1  

    #STEP TWO, compare the two words using if statements 
    if reversed_word == input_word:
        print('The word', input_word, 'Is a palindrome')
    else:
        print('The word', input_word, 'Is not a palindrome')

#Activating the function 
palindrome_checker('madam')
```