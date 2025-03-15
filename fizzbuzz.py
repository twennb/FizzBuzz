"""A python FizzBuzz application"""
# plan:
# Get user input for how many numbers to print
# Print 1 - user defined max
# Any number divisible by 3 = Fizz
# Any number divisible by 5 = Buzz
# Any number divisible by both = FizzBuzz


def get_input():
    """Function gets user defined max number"""
    while True:
        try:
            range_max = int(input("\nHow high should I count: "))
            return range_max
        except ValueError:
            print("Invalid input! Please enter a number.")


def count_and_evaluate_numbers(range_max, altered_range):
    """Function counts through all numbers up to user defined max and decides whether to replace"""
    for num in range(1, range_max+1):
        if num % 5 == 0 and num % 3 == 0:
            fizzbuzz(altered_range)
        elif num % 5 == 0:
            buzz(altered_range)
        elif num % 3 == 0:
            fizz(altered_range)
        else:
            altered_range.append(num)


def fizz(altered_range):
    """Function prints Fizz instead of a number divisible by 3"""
    altered_range.append("Fizz")


def buzz(altered_range):
    """Function prints Buzz instead of a number divisible by 5"""
    altered_range.append("Buzz")


def fizzbuzz(altered_range):
    """Function prints FizzBuzz instead of a number divisible by 3 and 5"""
    altered_range.append("FizzBuzz")


def main():
    """the main function"""
    altered_range = []

    range_max = get_input()
    count_and_evaluate_numbers(range_max, altered_range)

    for num in altered_range:
        print(num)


if __name__ == "__main__":
    main()
