# iterating_and_modifying

my_list = [1, 2, 3, 4]

print('my_list BEFORE: ', my_list)

for x in my_list:
    x = x * 10

print('my_list AFTER1: ', my_list)

new_list = []
for x in my_list:
    new_list.append(x*10)
my_list = new_list

del new_list
print('my_list AFTER2: ', my_list)
# print('new_list AFTER2: ', new_list)


