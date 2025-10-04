username="John"
age=3
#amount=3.5
#ismarried=False

print(type(username))
sentence=username + " is " +str(age) +" year old"
print(sentence)

age_client_company=45
print(age_client_company)
age_client_company=age_client_company +1
print(age_client_company)
age_client_company+=1
print(age_client_company)
age_client_company*=2 # multiplie par 2 la variable et reassigne cette nouvelle valeur 

#conditionals
amount_bank =10000
car = 3000

if amount_bank>=car:
    print("I buy a car")
    amount_bank-=car
    print(f"Now I have {amount_bank} in my bank account")
else:
    print("I don't buy a car")