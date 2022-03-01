# Exercise 1
# Create a list of numbers that are less than ten using l_1 and list comprehension
# Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]
l_1 = [1,11,14,5,8,9]
l_2 = [x for x in l_1 if x < 10]
print(l_2)

#--------------------------------------------------
# Exercise 2
# Using list comprehension, create a list of names of 4 letters or more and capitalize each name 

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

long_names = [name.title() for name in names1 if len(name) >= 4]
print(long_names)

# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

bonus_names = [name.title() for name in names2 if type(name) == str and len(name) >= 4]
print(bonus_names)