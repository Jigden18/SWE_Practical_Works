# EXERCISE 1 : Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
# SOLUTION :

def fib_itr(n) :
    # Base case ; fibonacci sequence starts from 0 
    if n < 0 :
        return []
    elif n == 0 :
        return [0]
    elif n == 1 :
        [0 , 1]
    
    # For n > 1 :
    fib_sequence = [0, 1] # list is initialized to first two number in fibonacci sequence
     # loop starts from two(second term) and ends at n ,(n+1) as python returns values only for second-last _ in range
    for _ in range(2, n + 1):
        # a = b and b = a + b with negative index
        next_fib = fib_sequence[-1] + fib_sequence[-2] 
        fib_sequence.append(next_fib) # adding next number to the list
    return fib_sequence

# testing the result:
n = 10 # n+1th fib number(11th term in this case)
print(f"Fibonacci sequence up to {n}: {fib_itr(n)}")


# EXERCISE 2 : Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
# SOLUTION :

def index_of_first_fib_exceeding(value):
    if value < 0:
        return 0 # for negative numbers

    a, b = 0, 1  # Initialize fibonacci numbers
    index = 1  # Start with the index of the second fibonacci number

    while b <= value:
        a, b = b, a + b  # Shift to next fibonacci number
        index += 1  # increse the index counter by 1

    return index

# testing the function
print(index_of_first_fib_exceeding(13))

# EXERCISE 3 :
#
def is_fibonacci_number(x):# x is the number to be checked
    if x < 0:
        return False  # fib numbers are not negative
    a, b = 0, 1  # Initialize the first two fib numbers respectively
    
    while b < x:
        a, b = b, a + b   

    # If b matches x , then x is a fib number
    return b == x

# testing the function
print(is_fibonacci_number(13)) 


# EXERCISE 4 : Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.
# SOLUTION :
# Golden ratio ; ϕ≈1.6180339887

def fibonacci_ratios(n):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    
    for _ in range(n):
        if a != 0 :  
            ratio = b / a
            print(f"Ratio of {b} / {a} = {ratio}")
        a, b = b, a + b  # Move to the next pair of Fibonacci numbers

# ratios of fib till a larger term number like 100 to observe the golden ratio
fibonacci_ratios(100)
