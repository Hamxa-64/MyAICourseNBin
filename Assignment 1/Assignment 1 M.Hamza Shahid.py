#Question 1 
# Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
# (Celsius * 9/5) + 32)

celsius = float(input(" Please Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


#Question 2
# Calculate Area of a Rectangle 


width = float(input("Please enter width: "))
height = float(input("Please enter height: "))
area = width*height
print("The Area of rectangle is:",  area)


#Question 3
# Calculate Compound Interest 
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time

P = float(input("Please enter principal: "))
R = float(input("Please enter rate: "))
T = float(input("Please enter time: ")) 

CI = P * (1 + R/100)**T - P
print("The compound interest is:",  CI)

#Question 4
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.


width = float(input("Please enter width: "))
height = float(input("Please enter height: "))
perimeter = 2 * (width + height)
print("The perimeter of rectangle is:",  perimeter)


#Question 5
# Average of Three Numbers - Input three numbers and print their average.

num1 = float(input("Please enter number 1: "))
num2 = float(input("Please enter number 2: "))
num3 = float(input("Please enter number 3: "))
average = (num1 + num2 + num3) / 3
print("The average of numbers is:", average)

#Question 6
# Square and Cube of a Number - Ask the user for a number and display its square and cube.


numb = int(input("Please enter number : "))
square = (numb**2)
cube = (numb**3)
print("The square of number is:", square)
print("The cube of number is:", cube)


#Question 7
# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets 
# how many are left

n = int(input("Enter total number of candies: "))
k = int(input("Enter total number of students: "))
candies_per_student = n // k
remaining_candies = n % k
print("Each student gets:", candies_per_student, "candies")
print("Candies left:", remaining_candies)

#Question 8
# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss

CP = int(input("Enter the cost price: "))
SP = int(input("Enter the selling price: "))

if SP > CP:
    Profit_amount = SP - CP
    print("Profit amount is:", Profit_amount)

elif SP < CP:
    Loss_amount = CP - SP
    print("Loss amount is:", Loss_amount)

else:
    print("No Profit No Loss")

#Question 9
# Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
# Total marks 
# Percentage 
# Average 

Sub1 = int(input("Enter the sub1 marks: "))
Sub2 = int(input("Enter the sub2 marks: "))
Sub3 = int(input("Enter the sub3 marks: "))
Sub4 = int(input("Enter the sub4 marks: "))
Sub5 = int(input("Enter the sub5 marks: "))

total_marks = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
percentage = (total_marks / 500) * 100
average = total_marks / 5

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Average:", average)

#Question 10
#Salary Calculator 
#Input basic salary. Calculate: 
#HRA = 20% of basic 
#DA = 15% of basic 
#Total Salary = Basic + HRA + DA

Basic = int(input("Enter the employee salary: "))
HRA = (Basic * 20) / 100
DA = (Basic * 15) / 100
Total_Salary = Basic + HRA + DA
print("Total HRA is:", HRA)
print("Total DA is:", DA)
print("Total salary is:", Total_Salary)


#Question 11
# Age in Months and Days 
# Input your age in years. Calculate and print age in: 
#  Months 
# Days (approximate)

age_years = int(input("Enter your age in years: "))

age_months = (age_years * 12)
age_days = (age_years * 365)  

print("Age in months:", age_months)
print("Age in days (approximate):", age_days)

#Question 12
# Currency Converter (USD to PKR) 
# Input amount in USD. Convert using a fixed exchange rate.

usd_currency = float(input("Enter your usd amount: "))
pkr_amount = (usd_currency*280)
print("Amount in pkr is :", pkr_amount)

#Question 13
# Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2

n = int(input("Enter a number: "))
sum_natural = n * (n + 1) // 2   # use // for integer result
print("Sum of first", n, "natural numbers is:", sum_natural)


#Question 14
# Percentage of Correct Answers 
# Input total questions and correct answers, and calculate the percentage score.

total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

percentage = (correct_answers / total_questions) * 100

print("Your percentage score is:", percentage, "%")


#Question 15
# Speed, Distance, and Time 
# Input distance and time, and calculate speed.
# distance = int(input("Enter the distance: "))
# time = int(input("Enter the time: "))
# speed = distance/time

print("The speed is: ", speed, "m/s")


#Question 16
# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI = weight / (height ** 2)
print("Your BMI is:", round(BMI, 2))


#Question 17
# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes

total_minutes = int(input("Enter minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(total_minutes, "minutes =", hours, "hours", minutes, "minutes")
