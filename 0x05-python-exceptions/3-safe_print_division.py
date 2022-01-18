#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resl = a / b
    except ZeroDivisionError:
        resl = None
    finally:
        print("Inside result: {}".format(resl))
        return resl
