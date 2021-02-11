# ##########################################################################################################
# # Program:    Remove_odd_or_even_index_elements.py
# # Purpose:    To remove either odd or even index elements from a string based on user choice.
# # Author:     Muralikrishnan Rajendran
# # Date:       24-May-2017
# # Dependencies:
#        Py Version: 3.x
#        Packages:   None
# ##########################################################################################################

new_str1 = str()   ## accumulation variable

def remove_even_index_elem(str_val):
    global new_str1
    for i in range(len(str_val)):
        if i%2 != 0:
            new_str1 += str_val[i]
    return new_str1
    
def remove_odd_index_elem(str_val):
    global new_str1
    for i in range(len(str_val)):
        if i%2 == 0:
            new_str1 += str_val[i]
    return new_str1
    
def main():    # acts as wrapper function for the program control flow
    while True:
        str1 = str(input("Please enter the string: "))
        if len(str1) <= 1:
            print("\033[31;3mInvalid Input! Please enter a string value of length greater than 1\33[0m")
            continue
        else:
            break
        
    while True:
        index_type_to_remove = str(input("\nPlease enter even or odd index elements to remove [Even/Odd]: ")).lower()
        if index_type_to_remove in ['even','odd','e','o']:
            break
        else:
            print("\033[31;3mInvalid Input!! Allowed inputs are: 'even','odd','e','o' \33[0m")
            continue
    
    if index_type_to_remove in ['even','e']:
        new_str1 = remove_even_index_elem(str1)
        index_type_to_remove = 'even'
        print("\n\t\33[37;42;1m{}\33[0m index elements removed! Old string is: \33[37;42;1m{}\33[0m, new string is: \33[37;42;1m{}\33[0m".format(index_type_to_remove.capitalize(),
                                                                                       str1, new_str1))
    else:
        new_str1 = remove_odd_index_elem(str1)
        index_type_to_remove = 'odd'
        print("\n\t\33[37;42;1m{}\33[0m index elements removed! Old string is: \33[37;42;1m{}\33[0m, new string is: \33[37;42;1m{}\33[0m".format(index_type_to_remove.capitalize(),
                                                                                       str1, new_str1))
        
# program execution starts here
main()


###################### End of Scripts ######################
