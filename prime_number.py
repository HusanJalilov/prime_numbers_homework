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
    for x in range(n):
        