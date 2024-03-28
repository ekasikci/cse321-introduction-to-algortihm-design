import random

def create_rand_array(array_size=100):
    array_size = 100

    # Calculate the number of even and odd elements
    even_count = int(array_size * 0.2)
    odd_count = array_size - even_count

    # Generate even and odd numbers
    even_numbers = [random.randint(1, 1000) * 2 for _ in range(even_count)]
    odd_numbers = [random.randint(1, 1000) * 2 + 1 for _ in range(odd_count)]

    # Combine the even and odd numbers to create the final array
    final_array = even_numbers + odd_numbers

    # Shuffle the array if you want the elements to be in a random order
    random.shuffle(final_array)

    # Print the resulting array
    print(final_array)

    return final_array

def find_first_even(array):
    array = create_rand_array()

    for i in range(len(array)):
        if array[i] % 2 == 0:
            print("The first even number is: ", array[i])
            print(f"The first even number was found on the {i + 1}. try")
            return


array = create_rand_array()
find_first_even(array)