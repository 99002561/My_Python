'''The module defines what arguments it requires, The argparse module also automatically
generates help (-h) and usage messages and issues errors when users give the program invalid arguments.'''
import argparse

# Initialize the Parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Adding Arguments
# metavar -  A name for the argument in usage messages
# type - type to which the command line arguments should be converted.
# nargs - number of command-line arguments that should be consumed
# help - brief description of what the argument does
# dest - The name of the attribute to be added to the object returned by parse_args()
# action - basic type of action to be taken when this argument is encountered at the command line
# const - constant value required by some action and nargs selections
''' store_const - This stores the value specified by const keyword argument
 special cases for store_const are 1)store_true and 2)store_false used to store values true and false.'''
parser.add_argument('integers', metavar='N',
                    type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument(dest='sai',
                    action='store_const',
                    const=sum,
                    help='sum the integers')

args = parser.parse_args()
print(args.sai(args.integers))

