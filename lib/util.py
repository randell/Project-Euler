def is_prime(x):
    """
    Checks if a given number is prime
    """
    if x <= 1:
        # Because any number less than or equal to 1 is neither prime nor composite.
        return False

    if x <= 3:
        # If the number is 2 or 3, we don't even need to compute if it's prime.
        return True

    # We check if the number is divisible by a certain number, starting with 2.
    i = 2

    while True:
        if x % i == 0:
            # If the number is divisible by a another number except for 1 and itself, it's composite (not prime).
            return False

        i += 1

        if i * i > x:
            # If we reach the square root of a number and we still cannot find a divisor, it's prime. No need to divide
            # using the remaining numbers.
            break

    return True


def is_palindrome(x):
    strx = str(x)
    strx_max_index = len(strx) - 1
    strx_len_half = len(strx) / 2

    for i in range(0, strx_len_half):
        if strx[i] != strx[strx_max_index - i]:
            return False

    return True