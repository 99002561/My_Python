import argparse
import shutil
import os


parser = argparse.ArgumentParser(description='Copying the file', prog='FileHandling', epilog='copying will be done',
                                 add_help=True)  # add_help=False to disable help options
parser.add_argument("Source", type=str, metavar='S', help="Source Path for %(prog)s program")
parser.add_argument("Destination", type=str, metavar='D', help="Destination path for %(prog)s program")
args = parser.parse_args()
print(args.Source)
print(args.Destination)
if not os.path.exists(args.Destination):
    os.makedirs(args.Destination)
shutil.copy(args.Source, args.Destination)
'''
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)
args = parser.parse_args()
print(args.foo) 


parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_false',)  # store_false = false
args = parser.parse_args()
print(args.foo) 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
args = parser.parse_args() # --foo 1 --foo 2
print(args.foo)'''

parser = argparse.ArgumentParser()
parser.add_argument('--foo' ,type=str, required=True)
args = parser.parse_args() # -foo sai
print(args.foo)
