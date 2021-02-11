# ##########################################################################################################
# # Program:    Generate_fibonacci_series.py
# # Purpose:    To generate Fibonacci series for a given length.
# # Author:     Muralikrishnan Rajendran
# # Date:       05-Jun-2017
# # Dependencies:
#        Py Version: 3.x
#        Packages:   None
# ##########################################################################################################

"""
 --- Fibonacci series ---
Fibonacci Sequence is the series of numbers:
   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

# fibonacci generation algorithm ----
def fibonacci(x):
    fib_list = [0,1]
    for i in range(x-2):
        y = fib_list[i]+fib_list[i+1]
        fib_list.append(y)
    return fib_list
        
    
def main():
    print("\t\tWelcome to Fibonacci Series generation program!!")
    while True:
        try:
            fib_len = int(input("\nPlease enter the length of fibonacci series: "))
        except ValueError:
            print("\tInvalid Input! Length value needs to be an integer...")
            continue
        else:
            if fib_len <= 2:
                print("\tInvalid Input! Length value needs to be greater than 2...")
                continue
            else:
                break
    
    fib_series = fibonacci(fib_len)
    print("\nThe Fibonacci series generated for length \'{}\' is: \n {}".format(fib_len, fib_series))
    
main()
            