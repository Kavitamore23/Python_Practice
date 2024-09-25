#!/usr/bin/env python
# coding: utf-8



#find the seacond largest number
#remove Duplicates form the list
#Calculate the factorial of number, take input from user
#check if a number is prime
#sum of Digit in number (1+2+5=125)
#find the largest number in list



#Q1)find the largest number in list
list=[1,34,5,42,3,2,8,9]
print("Largest element is:",max(list))





#Q5)sum of Digit in number (1+2+5=125)

num1=str(input("Enter num1:"))
num2 =str(input("Enter num2:"))
num3 =str(input("Enter num3:"))
Sum_of_digit=num1+num2+num3
print(Sum_of_digit)





#Q4)check if a number is prime
num = int(input("Enter number:"))
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")





#Q1)find the seacond largest number

a=2
b=6
c=7
largest=max(a,b,c)
if largest==a:
    second_largest=max(b,c)
elif largest == b:
    second_largest=max(a,c)
else:
    second_largest=max(a,b)
print("the second largest value",second_largest)




#Q3)Calculate the factorial of number, take input from user

n = int(input("Enter Number:"))
fact = 1

for i in range(1, n+1): 
    fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)





#sum of Digit in number (1+2+5=125)
#find the largest number in list

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def find_largest_number(numbers):
    return max(numbers)

number = 125
numbers_list = [1, 2, 5, 10, 50, 100]

# Calculate sum of digits
digit_sum = sum_of_digits(number)
print(f"Sum of digits in {number} is: {digit_sum}")

# Find the largest number in the list
largest_number = find_largest_number(numbers_list)
print(f"Largest number in the list is: {largest_number}")



