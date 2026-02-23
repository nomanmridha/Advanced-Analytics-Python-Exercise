# Function to check if a number is even
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
# Test the function

num = int(input("Enter a number: "))

if even(num):
    print(num, "is even")
else:
    print(num, "is odd")