first="Hello World"
#this is a comment
print("I AM A COMPUTER")
if 1<2 and 4>2: 
    print("math is fun")
nope = None
print(True and False)
L=len("What is my length?")
texte="I am shouting"
print(texte.upper())
nombre=int("1000")
print(nombre)
concatenate="4"+"real"
print(concatenate)
repeat=3*"cool"
print(repeat)
#error_test=1/0
#print(error_test)
test_type=type([])
print(test_type)
#name=input("what is tour name?")
#print(name)
number=float(input("give me a number "))
if number <0:
    print(f"the number {number} is negative")
elif number>0:
    print(f"the number{number} is positive")
else: print("you picked 0!")

fruit=list("apple") # methode bourrin
for i in range(len(fruit)):
    if fruit[i]=='l':
        print(f"index of l is {i}")
# autre methode avec subfunction .find
name='apple'
result=name.find('l')
print(f"index of l in apple is {result}")

print("y" in"xylophone")

my_string = "my_string"
print(my_string.islower())



