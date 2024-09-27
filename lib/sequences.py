#!/usr/bin/env python3



def print_fibonacci(length):
    my_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    my_sequence = []
    for i in range(length):
        my_sequence.append(my_numbers[i]) 
        
    print(my_sequence)
        

print_fibonacci(9)
