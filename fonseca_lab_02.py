#jordan fonseca lab 02

#2.3
#break down simple expression

expr = "12+27" #hard code

num1 = int(expr[0:2]) #spliced and made 12 into an integer out of hard code
num2 = int(expr[3:]) #spliced and made 27 into an integer out of hard code
op = expr[2] #spliced and identified the operator out of hard code 
sum = num1 + num2 #stored in variable 


print(num1, op, num2, "=", sum) #prints it out 

#2.4

#the way my code came out, i could not get an invalid expression.


#2.5

num1 = int(input("Enter first number")) #asks for first number
operator = input("Enter operator") #asks for operation to be used
num2 = int(input("Enter second number")) #asks for second number

if (operator == "+"): #if the operation chosen is addition 
    print(num1 + num2) #prints the sum of the 2 numbers
elif (operator == "-"): #if the operation chosen is subtraction 
    print(num2 - num1) #prints the difference of the 2 numbers
elif (operator == "*"): #if the operation chosen is multiplication 
    print(num1 * num2) #prints the product of the 2 numbers
else: #if division is chosen
    print(num2 / num1) #prints the quotient of the 2 numbers


#2.6

#I could not figure out how to code in a while loop.
#I did not fully understand what the question was asking.

#2.7

#I could not complete because i did not figure out 2.6.

#3.1

input("Enter 'last'") #makes the code print out last performed calculation 



#3.3

num1 = int(input("Enter first number")) #asks for first number
operator = input("Enter operator") #asks for operation to be used
num2 = int(input("Enter second number")) #asks for second number


print('(' , num1, operator, num2, "=", sum, ')' ) #prints out solution in parenthesis



