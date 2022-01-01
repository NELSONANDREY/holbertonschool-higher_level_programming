#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count_argv = len(argv)
    counter = 1
    total = 0
    while counter <= count_argv:
        total += int(sys.argv[counter])
        counter += 1
    print("{:d}".format(total))
