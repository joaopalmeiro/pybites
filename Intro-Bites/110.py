def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        num = int(numerator)
        den = int(denominator)

        return num / den
    except ValueError:
        raise ValueError()
    except ZeroDivisionError:
        return 0


# print(divide_numbers(10, 0))
# print(divide_numbers(1, 2.9))
# print(divide_numbers(1, 2))
# print(divide_numbers(8, 2))
# print(divide_numbers(8.2, 2))
# print(divide_numbers("3", "2"))
