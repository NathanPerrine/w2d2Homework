names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']


new_names= []
for name in names:
    if name not in new_names:
        new_names.append(name)
print(new_names)


#---------------------
first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
full_name = []

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
def full_names(firstname, lastname):
    
    for first, last in zip(firstname, lastname):
        full_name.append(f"{first} {last}")
    
    return full_name
    
print(full_names(first_name, last_name))

#------Exercise 1---------------
list_num = [1, 11, 14, 5, 8, 9]
i = 0

while i < len(list_num):
    if list_num[i] >= 10:
        list_num.pop(i)
        continue
    i += 1

print(list_num)

#------Exercise 2---------------
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = []

def merge_sort_lists(l1, l2):
    l_3 = l1 + l2
    l_3.sort()
    return l_3
print(merge_sort_lists(l_1, l_2))

