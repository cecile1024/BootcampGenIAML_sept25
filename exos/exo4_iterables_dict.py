#Exercise - Dictionary

#1. Given a list: [("name", "Elie"), ("job", "Instructor")], 
# create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} 
# (Note: The order does not matter).

list_items=[("name", "Elie"), ("job", "Instructor")]
result=dict(list_items)
print(result)

list_items = [("name", "Elie"), ("job", "Instructor")]
result2 = {}
for item in list_items:
    result2[item[0]] = item[1]
print(result2)

#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return 
# a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

abbreviations=["CA","NJ","RI"]
states=["California","New Jersey","Rhode Island"]   
result3=dict(zip(abbreviations,states))
print(result3)

result4={}
for i in range(len(abbreviations)):
    result4[abbreviations[i]]=states[i]    
print(result4)  

# 3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary 
# should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method)
vowels=['a','e','i','o','u']
result5={}
for vowel in vowels:
    result5[vowel]=0    
print(result5)

# 4. Create a dictionary where the key is the position of the letter in the alphabet, 
# and the value is the letter itself. 
list_alphabet=[chr(i) for i in range(ord('A'), ord('Z')+1)]
result6={}
for i in list_alphabet:
    result6[list_alphabet.index(i)+1]=i
print(result6)

#Super Bonus:
#Given the string "awesome sauce", return a dictionary where the keys are vowels, 
# and the values are the count of each # vowel in the string. 
# Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.

vowels=['a','e','i','o','u']
string="awesome sauce"
result7={}
for vowel in vowels:
    result7[vowel]=string.count(vowel)
print(result7)

