# Calculates the volume of a sphere given its radius to 2 d.p
def vol(rad):
    import math
    return round(((4.0 / 3) * math.pi * (rad ** 3)), 2)


# Checks if a given number is in a given range
def ran_check(num, low, high):
    if num in range(low, high + 1):
        return str(num) + ' is in the range between ' + str(low) + ' and ' + str(high)
    else:
        return str(num) + ' is in the range between ' + str(low) + ' and ' + str(high)


def ran_bool(num, low, high):       # Version which returns a boolean
    return num in range(low, high + 1)


# Returns the number of upper and lower case letters in a given string
def up_low(s):
    upper = 0
    lower = 0
    for letter in s:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return 'No. of Upper case characters : ' + str(upper) + ' and the No. of Lower case characters : ' + str(lower)


# Returns new list of unique elements of a given list
def unique_list(lst):
    return list(set(lst))


# Multiplies all numbers in a list
def multiply(numbers):
    x = 1
    for num in numbers:
        x *= num
    return x


# Checks if a given string is a palindrome
def palindrome(s):
    s = s.replace(' ', '')
    for i in range(int((len(s) / 2)) + 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# Checks if a given string is a pangram
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    al = list(alphabet)
    set(str1)
    for letter in str1:
        if letter in al:
            al.remove(letter)
    if len(al) == 0:
        return True
    return False