import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
dictionnary = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dictionnary[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    f = fname.split('.')
    if len(f) > 1:
        try:
            print(dictionnary[f[-1].lower()])
        except KeyError:
            print("UNKNOWN")
        except IndexError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
