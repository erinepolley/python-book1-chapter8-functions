# create a variable with a list of numbers 1-100
# iterate over the list. 
# IF numb in list is equal to %5 AND %7, print(f'{num} chickenmonkey')
# elif numb == %5, print numb chicken
# elif numb == %7 print numb Monkey
# else print(numb)

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(f'{i} ChickenMonkey')
    elif(i % 5 == 0):
        print(f'{i} Chicken')
    elif(i % 7 == 0):
        print(f'{i} Monkey')
    else:
        print(f'{i}')