#🌟 Exercise 2: Dictionary
#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

list_items = [("name", "Elie"), ("job", "Instructor")]
result = {}
for item in list_items:
    result[item[0]] = item[1]
print(result)


#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

abbreviations = ["CA", "NJ", "RI"]
states = ["California", "New Jersey", "Rhode Island"]
result = {}
for i in range(len(abbreviations)):
    result[abbreviations[i]] = states[i]
print(result)


#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

vowels = ['a', 'e', 'i', 'o', 'u']
result = {}
for vowel in vowels:
    result[vowel] = 0
print(result)


#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:

result = {}
for i in range(26):
    result[i + 1] = chr(65 + i)
print(result)


#Super Bonus:
#Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.

string = "awesome sauce"
vowels = ['a', 'e', 'i', 'o', 'u']
result = {}
for vowel in vowels:
    result[vowel] = string.count(vowel)
print(result)