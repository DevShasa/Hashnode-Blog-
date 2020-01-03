#TODO Simple bubble sort script 
import random
import copy

#Use a list to test the bubble sort 
#Initialize the list
unsorted_list = []

#Generate ten random numbers to sort 
for count in range(1,11):
    #random.randint generates a random number between 1 and 100
    random_number =  random.randint(1, 100)
    unsorted_list.append(random_number)
    
#Copy the unsorted list into a new list that is then sorted from high to low using bubble sort 
list_to_sort = copy.deepcopy(unsorted_list)
for out_loop_count in range(0, len(list_to_sort)):
    for in_loop_count in range(0, len(list_to_sort)-1):
        #If the left digit in the list is smaller than the right digit switch them 
        if list_to_sort[in_loop_count] < list_to_sort[in_loop_count+1]:
            temp = list_to_sort[in_loop_count]
            list_to_sort[in_loop_count] = list_to_sort[in_loop_count+1]
            list_to_sort[in_loop_count+1] = temp

#Display the sorted list and the unsorted list 
print('The unsorted list is', unsorted_list)
print('The sorted list is', list_to_sort)

