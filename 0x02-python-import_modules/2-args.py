#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count_argv = len(argv)
    index = 1
    if count_argv == 0:
        print("{:d} arguments.".format(count_argv))
    elif count_argv == 1:
        print("{:d} argument:".format(count_argv))
        print("{:d}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(count_argv))
        while index <= count_argv:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
