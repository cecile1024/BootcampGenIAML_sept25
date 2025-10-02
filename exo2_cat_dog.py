human_years=int(input("how many human years do you want to convert?"))
print(f'human_years={human_years}')
if human_years<=0:
    print("error: you cannot chose a negative or null number")
elif human_years==1:
    dog_years=cat_years=15
    print([human_years,cat_years,dog_years])
elif human_years==2:
    dog_years=cat_years=24
    print([human_years,cat_years,dog_years])
else:
    dog_years=24+(human_years-2)*5
    cat_years=24+(human_years-2)*4
    print([human_years,cat_years,dog_years])