#factorial of a number
# for example a factorial is --> 5! = 5x4x3x2x1
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        #recursive case: n x factorial of (n-1), there is no way to do n! so we mltiple the one below 
        return n * factorial(n-1)
    
number = int(input("which factorial would you like to know?"))
print(f"The factorial of {number} is {factorial(number)}")
        
#best case when n=0 or 1 
#recursive case /worst case: when n>1 because it has to call the function again and again taking longer time