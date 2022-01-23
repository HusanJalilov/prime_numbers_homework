from is_prime import is_prime
#Define function, Find the all prime numbers which are less than n.
def prime_list(n:int)->list:
    """
    Find the all prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        list: List of prime numbers
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
    return s