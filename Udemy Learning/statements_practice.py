#Prints only the words that start with s
st = 'Print only the words that start with s in this sentence'
newstring = st.split()
for word in newstring:
    if word[0].lower() == 's':
        print(word)

#Lists the even numbers from 0 to 10
list(range(0,11,2))             #version 1

for num in range(0,11,2):       #version 2
    print(num)

#Lists all numbers divisible by 3 from 1 to 50
mylist = [num for num in range(1,51) if num%3==0]    #list comprehension

mylist = []                                          #version 2
for num in range(1,51):
    if num%3==0:
        mylist.append(num)
print(mylist)

#Prints every word that has an even number of letters
st = 'Print every word in this sentence that has an even number of letters'
newstring = st.split()
for word in newstring:
    if len(word) % 2 == 0:
        print(word + ' is even!')


#fizzbuzz
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

#Creates a list of the first letters of every word
st = 'Create a list of the first letters of every word in this string'
newst = st.split()

newlist = []                                  #version 1
for word in newst:
    mylist.append(word[0])
print(newlist)

newlist = [word[0] for word in newst]         #list comprehension
print(newlist)