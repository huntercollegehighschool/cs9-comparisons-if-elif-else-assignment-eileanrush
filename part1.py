'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

num1 = int(input("Enter a number: "))

num2 = int(input("Enter another number: "))

num3 = int(input("Enter another number: "))

if num1 < num2 and num1 < num3:
  print("The smallest number is ", num1)
if num2 < num1 and num2 < num3:
  print("The smallest number is ", num2)
if num3 < num2 and num3 < num2:
  print("The smallest number is ", num3)
