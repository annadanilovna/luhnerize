"""Luherize check and generate algorithms."""

import math


def check(num):
    """Check if a given number conforms to the Luhn algorithm."""
    num = str(num)
    num_digits = len(num)
    sum = 0
    for digit_idx in range(2, num_digits + 1):
        cur_sum = int(num[num_digits - digit_idx])
        if digit_idx % 2 == 0:
            cur_sum = cur_sum * 2
            if cur_sum >= 10:
                cur_sum = int(str(cur_sum)[0]) + int(str(cur_sum)[1])
        sum += cur_sum

    # c=(10−( s mod 10 ) mod 10)
    check_digit = (10 - (sum % 10)) % 10
    return True if check_digit == int(num[num_digits - 1]) else False


def generate(seed, desired_len=16):
    """Generate valid luhn number options based off of a seed."""
    seed = str(seed)
    valid = []
    diff = desired_len - len(seed)
    for i in range(0, int(math.pow(10, diff))):
        num = seed + str(i).zfill(diff)
        if check(num):
            valid.append(num)
    return valid
