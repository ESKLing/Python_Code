#Returns the lesser of two numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


#Takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    out = text.split()
    return out[0][0].lower() == out[1][0].lower()


#Returns True if the sum of the integers is 20 or if one of the integers is 20. If not, returns False
def makes_twenty(n1,n2):
    return n1+n2 == 20 or n1 == 20 or n2 == 20


#Capitalizes the first and fourth letters of a name
def old_macdonald(name):
    if len(name) <= 3:
        return name + 'is too short'
    else:
        out = list(name.capitalize())
        out[3] = out[3].upper()
        return ''.join(out)


#Returns sentence with words reversed
def master_yoda(text):
    out = text.split()
    out.reverse()
    return ' '.join(out)


#Returns True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(n) in range(90,111) or abs(n) in range(190, 211)


#Returns True if an array contains two 3s next to each other
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


#Returns string with each letter tripled
def paper_doll(text):
    out = []
    for letter in text:
        out.append(letter*3)
    return ''.join(out)


#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    out = sum([a, b, c])
    if out <= 21:
        return out
    elif out > 21:
        if 11 in (a, b, c):
            out = out - 10
            if out <= 21:
                return out
        return 'BUST'


#Returns the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
def summer_69(arr):
    mysum = 0
    shouldAdd = True
    for num in arr:
        if shouldAdd:
            if num == 6:
                shouldAdd = False
            else:
                mysum += num
        else:
            if num == 9:
                shouldAdd = True
    return mysum


#Takes a list of integers and returns True if it contains 007 in order
def spy_game_2(nums):
    count = 0
    for x in nums:
        if count == 0:
            if x == 0:
                count += 1
        elif count == 1:
            if x == 0:
                count += 1
        elif count == 2:
            if x == 7:
                return True
    return False


#Returns the number and list of prime numbers up to and including a given number
def count_primes(num):
    primes = [2]               #store prime nums
    x = 3                      # counter - keep adding onto x until we hit the input num and then check if x is prime
    if num < 2:                # for the case of num = 0 or 1
        return 0
    while x <= num:            #x is going through every num up to input num
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:       #check if x is prime
                x += 2         #to jump ahead as even nums aren't prime
                break
        else:                  #if you go through for loop and it never breaks (note 'else' after 'for')
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


def count_primes_2(num):           #alternative function that makes use of the prime numbers
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if y <= x / 2:
                if x%y == 0:
                    x += 2
                    break
            else:
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)