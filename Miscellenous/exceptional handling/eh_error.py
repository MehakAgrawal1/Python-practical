#Q2. Write a Program in Python that infinitely receives positive integer as input and prints its Square.If a negative number is entered 
#then raise an Exception ,displaya relevant Error message and Make a Graceful Exit.

try:
    while 1:
        num=int(input("Enter a Positive Number : "))
        if num>=0:
            print(num**2)
        else:
            raise ValueError("Negative Number")
except ValueError as ve:
    print(ve.args)
