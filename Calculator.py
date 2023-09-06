from art import logo
#define all the functions that needs to be performed
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def exponent(n1, n2):
    return n1**n2

#create a dictionary which will hold the operator symbol as 'keys' abd thie function as 'values'
operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "**":exponent
}

#define a function which will be used for recursion
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))  #taking input from user
   
    for symbols in operations:
        print(symbols)   #from opeartions dict print all the keys(operator symbols)

    should_continue = True    #flag should_continue to True

    #create a while loop to perform calculating again and again till the user wants to perform
    while should_continue:    
        operators = input("Which opeartion you want to perform: ")    #asking user to input which opeartion they want to perform

        num2 = float(input("Enter the next number: "))

        #as per user input(operators), will look in the dictionary(operations) to call that function(value) stored at particular key(operator)
        calculation_function = operations[operators]
        answer = calculation_function(num1, num2)     #save that result in aswer variable and passing num1 and num2 into it

        print(f"{num1} {operators} {num2} = {answer}")    #printing the desired result

        #asking user if they want to continue calculating with the answer or start fresh calculation
        continue_performing = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start again: ")
        if continue_performing == 'y':
            num1 = answer
        elif continue_performing == 'n':
            calculator()    #if the user wants to start fresh, we will call the calculator function again(This is called recursion)
        else:       
            should_continue = False    #if the users input is something else from 'y' and 'n', it will end the program and exit

print(calculator())


