import argparse

parser = argparse.ArgumentParser(description='Printing fibonacci Series.')
parser.add_argument("integer", metavar='N', type=int, help="prints up to N fibonacci numbers")
args = parser.parse_args()
print(args.integer)
count = 0
n1 = 0
n2 = 1
while count < args.integer:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
