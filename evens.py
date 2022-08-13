def even_number_of_evens(numbers):
    
    if isinstance(numbers, list):
        # if numbers == []:
        #     return False
        # else:
        # evens = 0

        evens = sum([1 for n in numbers if n % 2 == 0])
        
        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1

        return True if evens and evens % 2 == 0 else False

        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == "__main__":
    even_number_of_evens([2, 1, 4])