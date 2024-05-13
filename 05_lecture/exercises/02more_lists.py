"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **

"""
# Provide your solution here
def list_of_stars(numbers: [int]) -> None:
    #starstring = "*" * 5  #name a variable and define it -> multiply it
    #print(starstring)


    for i in numbers:
        print(i * "*")


    for a in range(0, len(numbers)):
        print(numbers[a] * "*")

list_of_stars([1,2,8])   #placeholder = an empty list





"""
Write a function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""
# Provide your solution here
def anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
word1 = "listen"
word2 = "silent"
print("Are '{}' and '{}' anagrams?".format(word1, word2), anagrams(word1, word2))

word3 = "hello"
word4 = "world"
print("Are '{}' and '{}' anagrams?".format(word3, word4), anagrams(word3, word4))

"""
Write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
# Provide your solution here

def sum_of_positives(input_list):
    pos_nums = [num for num in input_list if num > 0]
    return sum(pos_nums)

numbers= [1, -2, 3, -4, 5]
print("The result is", sum_of_positives(numbers))


"""
Write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""
# Provide your solution here
def even_numbers(input_list):
    # Use list comprehension to filter even numbers from the original list
    even_nums = [num for num in input_list if num % 2 == 0]

    # Return the new list containing even numbers
    return even_nums

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Even numbers:", even_numbers(numbers))

"""
Write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""
# Provide your solution here
def list_sum(list1, list2):

    assert len(list1) == len(list2), "Lists must have the same length"


    result = [list1[i] + list2[i] for i in range(len(list1))]

    return result

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print("Sum of lists:", list_sum(list1, list2))