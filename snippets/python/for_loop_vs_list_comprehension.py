
my_list = ["a", "b", "c", "d"]
# my_list = [1, 2, 3, 4]
my_list_for = []
my_list_compr = my_list.copy()

for el in my_list:
    my_list_for.append(el * 2)    

my_list_compr = [el * 2 for el in my_list]

print(f"Die ursprüngliche Liste: {my_list}")
print(f"For-Schleife:            {my_list_for}")
print(f"List-Comprehension:      {my_list_compr}")