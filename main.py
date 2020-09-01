#5-1 conditinal test

housemates  = ["jasmine","elyse","steve","john","zack","brock","christina"]


while True:
  search_name = input("please enter the name of your housemates : ")
  if search_name == 'done':
     print("good-bye!")
     break

  if search_name in housemates:
        print(search_name + ", is your housemate!")
  else:
        print(search_name + ", is not your housemate!")

#5-2 More Conditional test
#Tests for equality and inequality with strings
# Tests using the lower() function
# Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

food_list = ["Burgers", "Sandwiches", "Steak", "Chicken", "Tacos", "Noodles"]

ordering = input("please enter what kind of food you want : ")

lower_food_list = [x.lower() for x in food_list]

if ordering.lower() in lower_food_list :
    print("Your chose ", ordering.title())
    nums = int(input("how many do you need? "))

    if nums >= 3 or nums < 1:
        print("you can order less than 3 and more than 0")

else:
    print("Sorry, we don't have what you want")


#5-3,4,5 생략 (similar to privious oens)
#5-6 : stages of life

q = int(input("how old ? "))

if q < 2:
    print("the person is a baby ")
elif q < 4 :
    print("the person is a toddler")
elif q < 13:
    print("the person is a kid")
elif q < 20:
    print("the person is a teenager")
elif q < 65:
    print("the person is an adult")
else:
    print("the person is an elder")


#5-7 favorite fruit
favorite_fruits = []

while True:
    users = input("please enter the name of fruits:")

    if users == 'done':
        break
    else:
        favorite_fruits.append(users)

print("The fruit list is created successfully!Let's find your fav fruit\n")

fruit = input("plz enter your fav fruit : ")
if fruit in favorite_fruits:
    print("you really like", fruit, "!!")

#5-8 : hello admin

name_list  = ["jasmine", "lauren", "rosemary", "admin", "elyse"]

for someone in name_list:
    if someone == "admin":
        print("Hello,",someone,"would like to see a status report?")
    else:
        print("Hello,", someone, "thank you for logging in again")

#5-9 : No users (pass! similar to the previous one)
#5-10 Checking usernames

current_users = ["abc123", "xyz123","aaaa","ssss","tttt","hellow"]
new_users = ["new123","world","fresh","aaaa","ssss"]

lower_current = [lower_current.lower() for lower_current in current_users]
lower_new = [lower_new.lower() for lower_new in new_users]
'''trying....:/
for new in lower_new:
    for curr in lower_current:
        if new == curr:
            print(new, "has been taken. you need to enter a new username!")
            break
    if new not in lower_current:
        print(new, "is available")
'''

for new in lower_new:
    if new in lower_current:
        print(new, "has been taken. you need to enter a new username!")
    else:
        print(new, "is available")

#5-11

numlist = list(range(1,10))

for x in numlist:
    if x == 1:
        print(x,"st")
    elif x == 2:
        print(x,"nd")
    elif x == 3:
        print(x,"rd")
    else:
        print(x,"th")



