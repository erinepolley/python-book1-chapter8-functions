# running_kids = ["Pam", "Sam", "Andrea", "Will"]
# swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
# sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
# hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]
# #Need to loop over the above lists
# for kid in running_kids:
#     print(f"{kid} ran so fast today.")

# for kid in swinging_kids:
# # def swing(kid):
#     print(f"{kid} loves to swing.")

# for kid in sliding_kids:
# # def slide(child):
#     print(f"{kid} loves to slide.")

# for kid in hiding_kids:
#     print(f"I played hide and seek with {kid} today.")

#create a variable with a list of numbers 1-100
#iterate over the list. 
#IF numb in list is equal to %5 AND %7, print(f'{num} chickenmonkey')
#elif numb == %5, print numb chicken
#elif numb == %7 print numb Monkey
#else print(numb)

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(f'{i} ChickenMonkey')
    elif(i % 5 == 0):
        print(f'{i} Chicken')
    elif(i % 7 == 0):
        print(f'{i} Monkey')
    else:
        print(f'{i}')