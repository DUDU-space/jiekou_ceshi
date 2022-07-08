# -*- utf-8 -*-
# @Time: 2019-04-16
# @ Author: chen

def prime(value):
    """判断是否为质数"""
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            return False
    return True


def max_prime(value):
    """不大于（小于或等于）给定值的最大质数"""
    for i in range(value, 2, -1):
        if prime(i):
            return i

if __name__ == '__main__':
    max_prime = max_prime(3)
    print(max_prime)
