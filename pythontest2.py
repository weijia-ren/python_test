#%%
list = [1,2,3]
print (list)

list = ["This","is",3]
print (list)
len(list)
#%%
list = ["This","is",3]
list 
len(list)
#%%
list_1 = [1, 2, [2, 3], [3, 4, 5]]
list_2 = [2, 3, list_1]
list_3 = [list_2]

# 想一想list_1, list_2和list_3的长度分别是多少？
print (len(list_1), len(list_2), len(list_3))
#%%
my_list = [2, 0, 1, 7, 0, 6, 2, 5]
# 读取my_list中的第一个元素
a = my_list[0]
# 读取my_list中的第三个元素
b = my_list[2]
# 读取my_list中的最后一个元素
c = my_list[-1]
# 读取my_list中的倒数第二个元素
d = my_list[-2]
print (a,b,c,d)
print (my_list[1:4])
print (my_list[:4])
print (my_list[0:4])
print (my_list[-3:])
print (my_list[1:6:2])
list_1=[my_list[i] for i in [3,1,5,7]]
print (list_1)
#逆取
a = my_list[::-1]
print (a)
a = my_list[::-2]
print (a)
list_1 += [4, 8]
print (list_1)