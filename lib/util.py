def is_prime(x):
    """
    Checks if a given number is prime
    """
    if x <= 1:
        # Because any number less than or equal to 1 is neither prime nor 
        # composite.
        return False

    if x <= 3:
        # If the number is 2 or 3, we don't even need to compute if it's prime.
        return True

    # We check if the number is divisible by a certain number, starting with 2.
    i = 2

    while True:
        if x % i == 0:
            # If the number is divisible by a another number except for 1 and 
            # itself, it's composite (not prime).
            return False

        i += 1

        if i * i > x:
            # If we reach the square root of a number and we still cannot find a 
            # divisor, it's prime. No need to divide using the remaining 
            # numbers.
            break

    return True


def is_palindrome(x):
    str_x = str(x)
    str_x_max_index = len(str_x) - 1
    str_x_len_half = len(str_x) / 2

    for i in range(0, str_x_len_half):
        if str_x[i] != str_x[str_x_max_index - i]:
            return False

    return True


def digit_sum(x):
    str_x = str(x)
    sum = 0

    for i in str_x:
        sum += int(i)

    return sum


def factorial(x):
    return 1 if 1 >= x else x * factorial(x - 1)

proper_divisors_dict = {}

def proper_divisors(x):
    if x in proper_divisors_dict:
        return proper_divisors_dict[x]
    
    pd = []

    if x <= 0:
        return pd

    i = 1

    while True:
        if i in pd:
            continue

        if x % i == 0:
            divisor = x / i

            if i not in pd:
                pd.append(i)

            if divisor not in pd and divisor != x:
                pd.append(divisor)

        i += 1

        if i * i > x:
            break
        
    proper_divisors_dict[x] = pd
    
    return pd