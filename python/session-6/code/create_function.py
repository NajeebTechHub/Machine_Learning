def multiply(num1,num2):
    """This function will multiply two number"""
    if type(num1) != int and type(num2) != int:
        return 'please give only numbers'
    else:
        return num1 * num2

print(multiply(5,6))