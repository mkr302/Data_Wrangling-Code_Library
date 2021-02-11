# ##########################################################################################################
# # Program:    Bubble_Sort.py
# # Purpose:    Sorting list elements using "Bubble sort" algorithm.
# # Author:     Muralikrishnan Rajendran
# # Date:       10-May-2017
# # Dependencies:
#        Py Version: 3.x
#        Packages:   time
# ##########################################################################################################

from time import time

def bubblesort(list1):
    sorted_list1 = list(list1)
    
    ### Bubble sort algorithm ----
    for i in range(len(sorted_list1)-1):
        accum_var = 0
        for j in range(len(sorted_list1)-1-accum_var): 
            if sorted_list1[j] > sorted_list1[j+1]:
                sorted_list1[j],sorted_list1[j+1] = sorted_list1[j+1],sorted_list1[j]
            accum_var += 1
        # print(sorted_list1) # bubble sort at each iteration of the list
    
    return sorted_list1

def main():
    print("Welcome to bubble-sort program!")
    
    list1 = input("\n\tPlease enter the numbers to be sorted, separated by comma: ").split(",")
    list1 = [int(x) for x in list1]
    if len(list1) == 0:
        print("\n\tThe list is empty!")
    elif len(list1) == 1:
        print("\n\tNo sort required, as the input list is a single element collection, list is: {}".format(list1))
    else:
        start = time()
        print("\n\tBubble sort complete! Sorted list is: {}".format(bubblesort(list1)))
        end = time()
        total = end-start
        print("\n\tTotal execution time: {} ms".format(round(total*1000,4)))
    
    print("\nEnd of bubble-sort program!")
    
main()
