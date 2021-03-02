import argparse

parser = argparse.ArgumentParser()  # To add arguments ,Parser object is initialized from argparse class
parser.add_argument("--number1",metavar='A', help="First Number")  # --n1 denotes changing to optional arguments
parser.add_argument("--number2", help="Second Number")
parser.add_argument("--operation", help="Operation", \
                    choices = ["add", "mul", "sub"])
args = parser.parse_args()  # Holds the value of arguments passed through command line prompt
print(args.n1)
print(args.n2)
print(args.operation)
num1 = int(args.n1)  # In command line the values are strings comes to pgm so, typecast
num2 = int(args.n2)
result = None
if args.operation == "add":
    result = num1 + num2
elif args.operation == "sub":
    result = num1 - num2
elif args.operation == "mul":
    result = num1 * num2
print("Result : ", result)
