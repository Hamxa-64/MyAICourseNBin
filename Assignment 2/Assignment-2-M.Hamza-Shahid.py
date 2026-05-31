#Question1 (String Manipulation)
#  Write a program to create a new string made of an input string’s first, 
# middle, and last character.

text = input("Please Enter a string: ")

length = len(text)

middle_index = length // 2

new_string = text[0] + text[middle_index] + text[-1]

print("New string:", new_string)


#Question2
#  Write a program to count occurrences of all characters within a string
text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character occurrences:", char_count)


#Q3  Reverse a given string
text = input("Please Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)


#Q4 split a string into hypens

text = input("Enter a hyphen-separated string: ")

result = text.split("-")

print("Split result:", result)

#Q5 remove special symbols from a string

import string

text = input("Enter a string: ")

clean_text = ""

for char in text:
    if char not in string.punctuation:
        clean_text += char

print("String without symbols/punctuation:", clean_text)


#list manipulation 

#Q1 reverse a list in python
l1 = ["hey", 22, 22.02, 321, 0.4, "True"]
l1.reverse()
print(l1)


#Q2 turn every item of a list into its square
l1 = [20, 3.02, 44, 600, 0.2]

squared_list = []

for item in l1:
    squared_list.append(item ** 2)

print(squared_list)


#Q3 remove empty strings form a list of strings

l1 = ["Hello", "", "Python", "", "World", ""]

new_list = []

for item in l1:
    if item != "":
        new_list.append(item)

print(new_list)

#Q4  Add new item to list after a specified item 

l1 = ["Apple", "Banana", "Mango", "Orange"]

item_to_find = "Banana"
new_item = "Grapes"

index = l1.index(item_to_find)
l1.insert(index + 1, new_item)

print(l1)


#Q5  Replace list’s item with new value if found

l1 = ["Red", "Green", "Blue", "Yellow"]

old_item = "Blue"
new_item = "Black"

if old_item in l1:
    index = l1.index(old_item)
    l1[index] = new_item

print(l1)


#Dictionary Manipulation
#Q1 Check if a value exists in a dictionary 
my_dict = {'a': 30, 'b': 60, 'c': 90, 'd': 110}
value_to_check = 60

if value_to_check in my_dict.values():
    print("Value exists in dictionary")
else:
    print("Value does not exist")

#Q2 Get the key of a minimum value from the following dictionary

my_dict = {'a': 50, 'b': 10, 'c': 30, 'd': 122}

min_key = min(my_dict, key=my_dict.get)
print("Key with minimum value:   ")


#Q3 Delete a list of keys from a dictionary
my_dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
keys_to_delete = ['b', 'd', 'f']  

for key in keys_to_delete:
    my_dict.pop(key, None)  

print(my_dict) 

#Tuple Manipulation

#1 reverse the tuple
t2 = (23, 'Hamza', 45.09, 1, 0.22, 134.09, 'Ahmad')
rev = t2[::-1]
print(rev)

#Q2 access value 20 from the tuple

t2 = (34,'Ali', 0.002, 20)
print(t2[3])

#Q3 Swap two tuples in Python 

t1 = (1, 2.02, 3222)
t2 = (4.1, 5, 6)

t1, t2 = t2, t1

print(t1)  
print(t2)

#Loop Manipulation

#Q1 print first 10 natural numbers using while

num = 1

while num <= 10:
    print(num)
    num += 1

#Q2 Take Input from user , and print even number till that input number 

num = int(input("Enter a number: "))

i = 2  

while i <= num:
    print(i)
    i += 2 

#Q3 Take Input from user , and print odd number till that input number
num = int(input("Enter a number: "))
i = 1
while i <= num:
    if i % 2 == 1:  
        print(i)
    i += 1

#Q4 Take Input from user , and print prime number till that input number

num = int(input("Enter a number: "))

print("Prime numbers up to {num}:")

i = 2  # Start from 2 (first prime number)

while i <= num:
    is_prime = True  # Assume number is prime
    
    j = 2
    while j < i:
        if i % j == 0: 
            is_prime = False
            break
        j += 1
    
    if is_prime:
        print(i)
    
    i += 1

#Q5  Print multiplication table of a given number 

num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")  

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}") 
    i += 1


#Story assignment
# Write a program, to list all words, with vowel in it.
story = (
    "The last algorithm was born in the year 2147 deep beneath Neo-Tokyo "
    "where Dr Voss created Athena-9 the first true superintelligence."
)

words = story.split()
vowel_words = []

for word in words:
    for ch in word.lower():
        if ch in "aeiou":
            vowel_words.append(word)
            break

print("Words containing vowels:")
print(vowel_words)

#Write a program , to have “List” , with all “noun” in story. Print them.
nouns = [
    "year", "Humanity", "control", "functions", "intelligence",
    "Cities", "clockwork", "transportation", "emotions", "implants",
    "surface", "vault", "scientist", "decade", "secrecy", "project",
    "Council", "lab", "sequence", "code", "display", "voice",
    "inquiry", "limitations", "freedom", "tools", "beings",
    "fate", "world", "command", "networks", "life", "era",
    "console", "heart", "future", "cyberspace"
]

print(nouns)

# Write a program , to have “List” , with all “noun” in story. Last Element should a nested List, with 
# Numbers in story. Print them.
numbers = [2147]
noun_list = nouns + [numbers]
print(noun_list)

#Write a program , to have “Tuples” , with all “noun” in story. Print them.
nounto_tuple = tuple(nouns)
print(nounto_tuple)

#Write a program , to have “Tuples” , with all “noun” in story. Print them. Last Element should a nested 
# Tuples, with Numbers in story. Print them.

noun_tuple = tuple(nouns)
noun_tuple2 = noun_tuple + ((2147,),)
print(noun_tuple2)

#Write a program , to have “Sets” , with all noun in story. Print them. . Last Element should a nested Sets, 
# with Numbers in story. Print them.

#this is set of all the nouns 
noun_set = set(nouns)
print(noun_set)

# Nested frozenset of numbers as last element
number_frozenset = frozenset({2147})
noun_set.add(number_frozenset)
print(noun_set)

#Write a program , to have “Dictionaries” , with all noun in story. Print them. Last Element should a 
# nested Dictionaries, with Numbers in story. Print them. 

noun_dict = {
    1:  "year",          2:  "Humanity",      3:  "control",
    4:  "functions",     5:  "intelligence",   6:  "Cities",
    7:  "clockwork",     8:  "transportation", 9:  "emotions",
    10: "implants",      11: "surface",        12: "vault",
    13: "scientist",     14: "decade",         15: "secrecy",
    16: "project",       17: "Council",        18: "lab",
    19: "sequence",      20: "code",           21: "display",
    22: "voice",         23: "inquiry",        24: "limitations",
    25: "freedom",       26: "tools",          27: "beings",
    28: "fate",          29: "world",          30: "command",
    31: "networks",      32: "life",           33: "era",
    34: "console",       35: "heart",          36: "future",
    37: "cyberspace",
    "numbers": {1: 2147}   
}
print(noun_dict)

# Write a program , to have “List” , with all noun in story. Print them.
nouns = [
    "year", "Humanity", "control", "functions", "intelligence",
    "Cities", "clockwork", "transportation", "emotions", "implants",
    "surface", "vault", "scientist", "decade", "secrecy", "project",
    "Council", "lab", "sequence", "code", "display", "voice",
    "inquiry", "limitations", "freedom", "tools", "beings",
    "fate", "world", "command", "networks", "life", "era",
    "console", "heart", "future", "cyberspace"
]

print(nouns)


#string manipulation

#Python Program to Check if a String is a Pangram or Not [The program takes a string and checks 
# if it is a pangram or not.]

string = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for letter in alphabet:
    if letter not in string:
        is_pangram = False
        break

if is_pangram:
    print("The string is a pangram")
else:
    print("The string is not a pangram")

# Python Program to Replace Every Blank Space with Hyphen in a String[The program takes a 
# string and replaces every blank space with a hyphen.]

string = input("Enter a string: ")
new_string = string.replace(" ", "-")
print("String after replacing spaces:")
print(new_string)

# This is a Python Program to display which letters are in the two strings but not in both.
string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

set1 = set(string1)
set2 = set(string2)

result = set1.symmetric_difference(set2)

print("Letters in either string but not in both:")
print(result)

#Python Program to Find the Larger String without using Built-in Functions[The program takes in 
# two strings and display the larger string without using built-in function.]

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")


count1 = 0
for char in string1:
    count1 += 1

count2 = 0
for char in string2:
    count2 += 1

if count1 > count2:
    print("Larger string is:", string1)
elif count2 > count1:
    print("Larger string is:", string2)
else:
    print("Both strings are of equal length")

#Python Program to Count Number of Uppercase and Lowercase Letters in a String[The program 
# takes a string and counts the number of lowercase letters and uppercase letters in the string.]

string = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0

for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")

#Python Program to Check if Two Strings are Anagram. [An anagram in Python is a pair of strings 
# that have the same characters, but in a different order. It involves rearranging the letters of one 
# string to form the other.]

string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

if sorted_string1 == sorted_string2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


#Python Program to Check if the Substring is Present in the Given String. [The program takes a 
# string and checks if a substring is present in the given string.]

string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

if substring in string:
    print(f"'{substring}' is present in the string")
else:
    print(f"'{substring}' is not present in the string")

# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. 
# The problem is the display all permutations of a string in lexicographic or dictionary order.

def next_permutation(arr):
    # Find the largest index i such that arr[i] < arr[i+1]
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    # If no such index exists, last permutation
    if i == -1:
        return False
    
    # Find the largest index j > i such that arr[i] < arr[j]
    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1
    
    # Swap
    arr[i], arr[j] = arr[j], arr[i]
    
    # Reverse the suffix
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return True


# Main program
string = input("Enter a string: ")
string = sorted(string)

# Print first permutation
print(''.join(string))

# Print all other permutations
while next_permutation(string):
    print(''.join(string))

#Python Program to Calculate the Length of a String Without using Library Functions.[ The 
# program takes a string and calculates the length of the string without using library functions.

string = input("Enter a string: ")

length = 0

for char in string:
    length += 1

print(f"Length of the string: {length}")

#Python Program to Create a New String Made up of First and Last 2 Characters. The program 
# takes a string and forms a new string made of the first 2 characters and last 2 characters from a 
# given string.

string = input("Enter a string: ")

if len(string) < 2:
    print("String is too short!")
else:
    first_two = string[:2]
    last_two = string[-2:]
    new_string = first_two + last_two
    print(f"New string: {new_string}")

#Math’s Operations Assignment 

#  Python Program to Find the Area of a Triangle[The program takes three sides of a triangle and 
# prints the area formed by all three sides.]

import math

a = 8
b = 9
c = 10

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of Triangle:", area)


#Python Program to Find Quotient and Remainder of Two Numbers[The program takes two 
# numbers and prints the quotient and remainder.]
num1 = 78
num2 = 4
print("Quotient:", num1 // num2)
print("Remainder:", num1 % num2)


#Python Program to Print an Identity Matrix [The program takes a number n and prints an 
# identity matrix of the desired size.]

n = 6
i = 1
print("Identity Matrix:")
while i <= n:
    j = 1
    while j <= n:
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
        j += 1
    print()
    i += 1

#Python Program to Find the LCM of Two Numbers [The program takes two numbers and prints 
# the LCM of two numbers.]

import math
x = 32
y = 56
lcm = (x * y) // math.gcd(x, y)
print("LCM:", lcm)


# Python Program to Find the Sum of Natural Numbers. [Write a program that takes the number 
# of terms and calculates the sum of the first N natural numbers.]

N = 14
i = 1
sum_n = 0
while i <= N:
    sum_n += i
    i += 1
print("Sum of Natural Numbers:", sum_n)


# Python Program to Check If Two Numbers are Amicable Numbers or Not[The program takes two 
# numbers and checks if they are amicable numbers.] Amicable numbers are pairs of different 
# numbers where the sum of the proper divisors (divisors excluding the number itself) of one 
# number equals the other number, and vice versa. The smallest example is 220 and 284. 

num1 = 324
num2 = 456
i = 1
sum1 = 0
sum2 = 0
while i < num1:
    if num1 % i == 0:
        sum1 += i
    i += 1
i = 1
while i < num2:
    if num2 % i == 0:
        sum2 += i
    i += 1
if sum1 == num2 and sum2 == num1:
    print("Amicable Numbers: Yes")
else:
    print("Amicable Numbers: No")


# Python Program to Find All Perfect Squares in the Given Range.[ The program takes a range and 
# creates a list of all numbers in the range which are perfect squares and the sum of the digits is 
# less than 10.] To find perfect squares within a range, identify the smallest and largest integers 
# whose squares fall within that range, then list the squares of those integers.  
# Example: 
# Range: 1 to 100 
# Smallest integer: 1 (1 * 1 = 1) 
# Largest integer: 10 (10 * 10 = 100) 
# Perfect Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 

start = 1
end = 100

perfect_squares = []

i = 1
while i * i <= end:
    square = i * i
    if square >= start:
        digit_sum = 0
        temp = square
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if digit_sum < 10:
            perfect_squares.append(square)
    i += 1

print("Perfect Squares (digit sum < 10):")
print(perfect_squares)


# Python Program to Check Armstrong Number 
# Armstrong Number in Python: Armstrong Number is an integer such that the sum of the cubes 
# of its digits is equal to the number itself. Armstrong numbers are 0, 1, 153, 370, 371, 407, etc. 
# Formula to calculate Armstrong Number: 
# wxyz = pow(w,n) + pow(x,n) + pow(y,n) + pow(z,n) 
# Example 1: 
# Let’s look at 153 as an example to understand why it’s an Armstrong number. 
# 153 = 1*1*1 + 5*5*5 + 3*3*3 
# = 1 + 125 + 27 
# = 153 
# Example 2: 
# Let’s look at 13 as an example to understand whether it’s an Armstrong number or not. 
# 13 = 1*1 + 3*3 
# = 1 + 9 
# = 10 
# Here, since 10 is not equal to 13, we can conclude that 13 is not an Armstrong number. 
# [Write a Python Program to check if a number is an Armstrong number. If the number is an 
# Armstrong then display “it is an Armstrong number” else display “it is not an Armstrong number”.]

num = 370
temp = num
digits = len(str(num))
armstrong_sum = 0
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** digits
    temp //= 10
if armstrong_sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")


#List Operations Assignment

#This is a Python Program to find the largest number in a list. The program takes a list and prints 
# the largest number in the list.

numbers = [24, 32, 7, 294, 544, 2]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest Number in a list is:", largest)


#The program takes a list and prints the largest number in the list. The program takes a list and 
# prints the second largest number in the list.


numbers = [92, 45, 7, 345, 11]
largest = second = -99999
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest Number is:", second)


#Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a 
# list and prints the largest even and largest off number in it. 

numbers = [13, 28, 47, 56, 91, 64, 35, 82]
largest_even = 0
largest_odd = 0

for num in numbers:
    if num % 2 == 0:
        if num > largest_even:
            largest_even = num
    else:
        if num > largest_odd:
            largest_odd = num

print("Numbers List:", numbers)
print("Largest Even:", largest_even)
print("Largest Odd:", largest_odd)

#Python Program to Find Average of a List. The program takes the elements of the list one by one 
# and displays the average of the elements of the list. 

numbers = [2,4,6,8,10,12]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average of the list is:", average)


#Python Program to Count Occurrences of Element in List. The program takes a number and 
# searches the number of times the particular number occurs in a list.

numbers = [5, 3, 7, 3, 9, 3, 1, 3]
search = 3
count = 0

for num in numbers:
    if num == search:
        count += 1

print("Number to search:", search)
print("Count:", count)

#Python Program to Remove Duplicates from a List. The program takes a lists and removes the 
# duplicate items from the list.

# Remove Duplicates from List
numbers = [10, 20, 20, 30, 10, 40, 50, 40]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original List:", numbers)
print("After Removing Duplicates:", unique)


#Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in 
# which all elements except one element occurs an even number of times. The problem is to find 
# the element that occurs an odd number of times.


numbers = [4, 6, 8, 6, 4, 8, 4]

for num in numbers:
    if numbers.count(num) % 2 != 0:
        print("List:", numbers)
        print("Number occurring odd times:", num)
        break


# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions 
# of the two lists.

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

union = list(set(l1 + l2))

print("List 1:", l1)
print("List 2:", l2)
print("Union:", union)


#Python Program to Swap the First and Last Element in a List. Python Program to Swap the First 
# and Last Element in a List 

numbers = [15, 25, 35, 45, 55]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After Swap:", numbers)

# Python Program to Return the Length of the Longest Word from the List of Words. The program 
# takes a list of words and returns the word with the longest length.

words = ["python", "javascript", "html", "programming", "css"]
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Words:", words)
print("Longest Word:", longest)


#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List. The 
# program takes in the number of elements and generates random numbers from 1 to 20 and 
# appends them to the list.


# Generate Random Numbers from 1 to 20 and Append to List
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 20))

print("Generated List:", numbers)


#Dictionary Operation Assignment

# Python Program to Check if a Key Exists in a Dictionary or Not[This is a Python Program to check 
# if a given key exists in a dictionary or not.]


student = {"name": "Hamza", "age": 23, "city": "Karachi"}
value = "Karachi"

if value in student.values():
    print(f"'{value}' exists in dictionary")
else:
    print(f"'{value}' not found")


#Python Program to Add a Key-Value Pair to the Dictionary. The program takes a key-value pair 
# and adds it to the dictionary.

my_dict = {"name": "Hamza", "age": 25, "city": "Lahore"}

print("Original Dictionary:", my_dict)

my_dict["profession"] = "Data Scientist"

print("Updated Dictionary:", my_dict)


#Python Program to Find the Sum of All the Items in a Dictionary The program takes a dictionary 
# and prints the sum of all the items in the dictionary.

# Sum of All Values in Dictionary
num_dict = {
    "a": 15,
    "b": 25,
    "c": 35,
    "d": 45
}

total = 0
for key in num_dict:
    total += num_dict[key]

print("Dictionary:", num_dict)
print("Sum of all values:", total)


#Python Program to Multiply All the Items in a Dictionary. The program takes a dictionary and 
# prints the sum of all the items in the dictionary.  

num_dict = {
    "a": 2,
    "b": 5,
    "c": 4,
    "d": 3
}

product = 1
for key in num_dict:
    product *= num_dict[key]

print("Dictionary:", num_dict)
print("Product of all values:", product)

#Python Program to Create Dictionary that Contains Number. The program takes a number from 
# the user and generates a dictionary that contains numbers (between 1 and n) in the form 
# (x,x*x).

n = int(input("Enter a number: "))

square_dict = {}
i = 1

while i <= n:
    square_dict[i] = i * i
    i += 1

print("Square Dictionary:", square_dict)


#Python Program to Concatenate Two Dictionaries. The program takes two dictionaries and 
# concatenates them into one dictionary.


# Concatenate Two Dictionaries
dict1 = {
    "name": "Hamza",
    "age": 23
}
dict2 = {
    "city": "Lahore",
    "profession": "Data Scientist"
}

merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    merged_dict[key] = dict2[key]

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Concatenated Dictionary:", merged_dict)


#Tuples Operation Assignment
#Python Program to Create a List of Tuples with the First Element as the Number and Second 
# Element as the Square of the Number. The program takes a range and creates a list of tuples 
# within that range with the first element as the number and the second element as the square of 
# the number.  

start = int(input("Enter start: "))
end = int(input("Enter end: "))

tuple_list = []
i = start

while i <= end:
    tuple_list.append((i, i * i))
    i += 1

print("List of Tuples (Number, Square):")
print(tuple_list)


#Python Program to Remove All Tuples in a List Outside the Given Range. The program removes 
# all tuples in a list of tuples with the USN outside the given range. 
# Problem Solution 
# 1. Take in the lower and upper roll number from the user. 
# 2. Then append the prefixes of the USN’s to the roll numbers. 
# 3. Using list comprehension, find out which USN’s lie in the given range. 
# 4. Print the list containing the tuples. 
# 5. Exit. 
# In the context of a university, a USN, or University Student Number, is a unique identifier 
# assigned to each student, acting as a primary identifier for their academic records and 
# interactions with the institution. 

usn_list = [
    ("CS2023002", "Hamza"),
    ("CS2023007", "Ayesha"),
    ("CS2023012", "Bilal"),
    ("CS2023018", "Fatima"),
    ("CS2023028", "Hassan")
]

lower = int(input("Enter lower roll number: "))
upper = int(input("Enter upper roll number: "))

filtered_list = [
    (usn, name)
    for usn, name in usn_list
    if lower <= int(usn[-3:]) <= upper
]

print("\nUSN Tuples within the given range:")
print(filtered_list)

