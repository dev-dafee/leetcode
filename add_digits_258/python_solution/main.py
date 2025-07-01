

def addDigits(num: int) -> int:
        
        while num > 9:
            num = sum([int(item) for item in str(num)])
            
        return num

if __name__ == "__main__":
    # Example usage
    print(addDigits(38))  # Output: 2
    print(addDigits(123))  # Output: 6
    print(addDigits(0))    # Output: 0
    print(addDigits(9999)) # Output: 9