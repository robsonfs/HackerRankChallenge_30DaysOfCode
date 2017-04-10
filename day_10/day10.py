#!/bin/python3

def main(n):
    str_b = bin(n)[2:]
    return max(len(seq) for seq in str_b.split('0') if seq)

if __name__ == '__main__':
    n = int(input().strip())
    print(main(n))
