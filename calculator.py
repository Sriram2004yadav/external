def display(a):
    print("Result")
    value=calculate(a)
    print(value)

def calculate(str_input):
    a=str_input.split()
    value=eval(a)
    return value
a= input("Enter the expression to calculate: ")
display(a)