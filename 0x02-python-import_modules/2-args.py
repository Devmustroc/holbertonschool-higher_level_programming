#!/bin/bash
from sys import argv


if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if argv is 0:
        print("{:d} argements".format(args))
    elif argv is 1:
        print("{:d} argement:".format(args))
    else:
        print("{:d} argements".format(args))
    for i in range (1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))