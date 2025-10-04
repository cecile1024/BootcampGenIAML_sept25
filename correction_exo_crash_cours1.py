#Exercise 1: List Comprehension

#1. Given a list [1,2,3,4], print out all the values in the list.

for val in [1, 2, 3, 4]:
    print(val)


#2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

for val in [1, 2, 3, 4]:
    print(val * 20)


#3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).

result = []
for person in ["Elie", "Tim", "Matt"]:
    result.append(person[0])
print(result)


#4. Given a list [1,2,3,4,5,6], return a new list of all the even values.

result = []
for val in [1, 2, 3, 4, 5, 6]:
    if val % 2 == 0:
        result.append(val)
print(result)


#5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two [3,4].

result = []
for val in [1, 2, 3, 4]:
    if val in [3, 4, 5, 6]:
        result.append(val)
print(result)


#6. Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).

result = []
for word in ["Elie", "Tim", "Matt"]:
    result.append(word[::-1].lower())
print(result)


#7. Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).

result = ""
for char in "first":
    if char in "third":
        result += char
print(result)


#8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).

result = []
for x in range(1, 101):
    if x % 12 == 0:
        result.append(x)
print(result)


#9. Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).

result = []
for char in "amazing":
    if char not in ["a", "e", "i", "o", "u"]:
        result.append(char)
print(result)


#10. Generate a list with the value [0, 1, 2], [0, 1, 2], [0, 1, 2].

result = []
for _ in range(3):
    result.append([i for i in range(0, 3)])
print(result)


#11. Generate a list with the value [i for i in range(0, 10)] for num in range(0, 10).

result = []
for num in range(0, 10):
    result.append([i for i in range(0, 10)])
print(result)