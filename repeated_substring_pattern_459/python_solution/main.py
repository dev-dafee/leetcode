import math


def is_prime(n: int) -> bool:

    """
    Check if a number is prime.
    :param n: Integer to check
    :return: True if n is prime, False otherwise
    """

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def return_divisors(n:int) -> set:
    """
    Return a set of divisors of n excluding 1 and n itself.
    :param n: Integer to find divisors for
    :return: set of divisors of n
    """
    return {divisor for i in range(1, int(math.sqrt(n))+ 1) if n % i == 0 for divisor in (i, n//i) if divisor != n and divisor != 1}


def main(a_string: str) -> bool:
    """
    Check if the input string can be constructed by repeating a substring.
    :param a_string: Input string to check
    :return: True if the string can be constructed by repeating a substring, False otherwise
    """
    n = len(a_string)
    
    if n == 1: # Single character strings cannot be constructed by repeating a substring
        return False
    if len(set(a_string)) == 1: # All characters are the same, hence it can be constructed by repeating the character
        return True
    if is_prime(n): # If the length of the string is prime, it cannot be constructed by repeating a substring
        return False
    
    divisors = return_divisors(n)
    
    for divisor in divisors:
        pattern = a_string[:divisor]
        if pattern * (n // divisor) == a_string:
            print(f"Found repeating pattern: '{pattern}' for divisor {divisor}")
            return True
            
    return False    

if __name__ == "__main__":
    test_string = "bb"
    print(f"Can the string '{test_string}' be constructed by repeating a substring? {main(test_string)}")