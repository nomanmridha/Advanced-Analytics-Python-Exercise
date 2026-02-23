# stats.py
# Module to compute statistical functions

def mean(numbers):
    """
    Computes and returns the mean of a list of numbers.
    Returns 0 if the list is empty.
    """
    # Check if the list is empty
    if len(numbers) == 0:
        return 0
    
    # Calculate sum using loop
    total = 0
    for number in numbers:
        total += number
    
    # Calculate mean
    average = total / len(numbers)
    return average

def main():
    """
    Main function to test the mean function.
    """
    test_data = [3, 1, 7, 1, 4, 10]

    result = mean(test_data)

    print("Test Data:", test_data)
    print("Mean:", result)

    # Run main function when file is executed directly
if __name__ == "__main__":
    main()
    