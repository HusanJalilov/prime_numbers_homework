from is_prime import is_prime
#Define function, Find the number of prime numbers which are less than n.

def prime_number(n:int)->int:
    """
    Find the number of prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        int: Number of prime numbers
    """
    s = []
    m = 0
    for i in range (2, n):
        for j in range (2, i):
            if i % j == 0:
                m += 1
        if m == 0:
            s.append(i)
        else:
            m = 0
    return len(s)
print(prime_number(10))