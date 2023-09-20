#!/usr/bin/env python3

def print_fibonacci(length):
	fib_seq = []
	if length > 0:
		fib_seq.append(0)
	if length >= 2:
		fib_seq.append(1)
		for i in range(2, length):
			fib_seq.append(fib_seq[-1] + fib_seq[-2])

	print(fib_seq)
	
    # i = 0
    # j = 1
    # my_list = []

    # if length > 0:
    #     my_list.append(0)
    
    # if length >= 2:
    #     my_list.append(1)
    #     while len(my_list) < length:
    #         num = i + j
    #         i = j
    #         j = num
    #         my_list.append(num)
    
    # for num in my_list:
    #     print(num)
    # i = 0
    # j = 1
    # my_list = []

    # if length > 0:
    #     my_list.append(0)
    # if length >= 2:
    #     my_list.append(1)
    #     while len(my_list) < length:
    #         num = i + j
    #         i = j
    #         j = num
    #         my_list.append(num)
    # else:
    #      my_list = []
    #      print(my_list)

    # for num in my_list:
    #     print(num)