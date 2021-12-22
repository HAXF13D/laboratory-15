#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_setup(start=0):
    def decorator_function(func):
        def wrapper(args):
            result = func(args)
            return result + start

        return wrapper

    return decorator_function


@decorator_setup(start=5)
def individual_func(data):
    digits = list(map(int, data.split()))
    return sum(digits)


def main():
    string = input(
        "Введите строку целых чисел, разделенных пробелом:\n"
    )
    result = individual_func(string)
    print(result)


if __name__ == "__main__":
    main()
