from ..utils.arithmetic import add,subtract,multiply,divide

def increment(a):
    """increment. A function to increment a given number by 1.

    :param a: the number to increment. 
    :type a: float or int
    :return: a+1
    :rtype: float or in float or int
    """
    return add(a,1)

def decrement(a):
    """decrement. A function to decrement a given number by 1.

    :param a: the number to decrement. 
    :type a: float or int
    :return: a-1
    :rtype: float or in float or int
    """
    return subtract(a,1)


