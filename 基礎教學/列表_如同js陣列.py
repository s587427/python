
# 列表可變的, 字符串不可

# 可使用for循環印出裡面的值
from operator import le
from unicodedata import name


rhyme = [1, 2, 3, 4, '上山打老虎']

# print(rhyme[0]) # 1
# print(rhyme[1]) # 2
# print(rhyme[2]) # 3
# print(rhyme[3]) # 4
# print(rhyme[4]) # 上山打老虎

# 獲取列表長度len
# print(len(rhyme)) #5

# # 得到最後一個列表元素
# print(rhyme[len(rhyme) - 1])
# print(rhyme[-1])

# 列表切片類似js slice
# print(rhyme[0:3]) # [1, 2 ,3]
# print(rhyme[3:5]) # [4, '上山打老虎']
# print(rhyme[:3]) # [1, 2 ,3]
# print(rhyme[3:]) # [4, '上山打老虎']
# print(rhyme[:]) # [1, 2, 3, 4, '上山打老虎']
# print(rhyme[0:5:2]) # [1, 3, '上山打老虎'] 跨度2
# print(rhyme[::2]) # [1, 3, '上山打老虎'] 跨度2
# print(rhyme[::-2]) # ['上山打老虎', 3, 1] 跨度-2
# print(rhyme[::-1]) # ['上山打老虎', 4, 3, 2, 1] 跨度-2 (序列反轉)

# 列表尾添加append (只能添加單筆)
# heros = ['鋼鐵俠', '綠巨人']
# heros.append('黑寡婦')
# print(heros)
# extend (可添加多筆也是一個列表)
# heros.extend(['鷹眼', '滅霸', '雷神'])
# print(heros)

# s = [1, 2 ,3 ,4 ,5]
# s[len(s):] = [6] # [1, 2 ,3 ,4 ,6]
# print(s)
# s[len(s):] = [7, 8, 9] # [1, 2 ,3 ,4 ,6, 7, 8, 9]
# print(s)

# 列表插入insert
# s = [1, 3, 4, 5]
# s.insert(1, 2) # [1, 2, 3, 4, 5]
# print(s)

# 列表刪除元素 

# remove
# heros.remove('滅霸') # ['鋼鐵俠', '綠巨人', '黑寡婦', '鷹眼', '雷神']
# print(heros)
# heros.remove('多拉a夢') # 不存在會報錯ValueError: list.remove(x): x not in list

# pop
# heros.pop(2) # ['鋼鐵俠', '綠巨人', '鷹眼', '雷神']
# print(heros)

# clear 刪除整個列表
# heros.clear()
# print(heros) # []

# 列表修改
heros = ['蜘蛛俠', '綠巨人', '黑寡婦', '鷹眼', '滅霸', '雷神']
# heros[4] = '鋼鐵俠'
# print(heros) # ['蜘蛛俠', '綠巨人', '黑寡婦', '鷹眼', '鋼鐵俠', '雷神']
heros[3:] = ['武松', '林沖', '里奎']
# print(heros) # ['蜘蛛俠', '綠巨人', '黑寡婦', '武松', '林沖', '里奎']


# nums = [3, 1, 9, 6, 8, 3, 5, 3]
# # sort 
# nums.sort()
# print(nums) # [1, 3, 3, 3, 5, 6, 8, 9]
# # reverse
# nums.reverse()
# print(nums) # [9, 8, 6, 5, 3, 3, 3, 1]

nums = [3, 1, 9, 6, 8, 3, 5, 3]
nums.sort(reverse=True) # 大到小
# print(nums) # [9, 8, 6, 5, 3, 3, 3, 1]

# 查找元素出現次數
# print(nums.count(3))
# 查找元素索引值
# print(heros.index('綠巨人')) #index(searchElement[, startIndex, endIndex])
# 拷貝列表(淺拷貝)
nums_copy = nums.copy() # [9, 8, 6, 5, 3, 3, 3, 1]
name_copy2 = nums[:] # [9, 8, 6, 5, 3, 3, 3, 1]
# print(nums_copy, name_copy2)

# 列表拼接
s = [1, 2, 3]
t = [4, 5, 6]
# print(s + t) #[1, 2, 3, 4, 5, 6]
# print(s * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 二維列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for each in i:
        print(each, end=' ')
    # print()
# matrix[0] = [1, 2, 3]
# matrix[0][0] = 1
# matrix[0][1] = 2

# 創建二維列表使用for

A = [0] * 3
# print(A) [0, 0, 0]
for i in range(3):
    A[i] = [0] * 3

# print(A) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# is運算符號(用來判斷兩個變數是否指向同一個對象)
x = 'FishC'
y = 'FishC'
# print(x is y) # True
x = [1, 2, 3]
y = [1, 2, 3]
# print(x is y) # False

x = [1, 2, 3]
y = x 
y[0] = 2
# print(x) # [2, 2, 3]

# shallow copy
x = [1, 2, 3]
y = x[:] 
z = x.copy()
y[0] = 3
z[0] = 4
# print(x, y, z) # [1, 2, 3] [3, 2, 3] [4, 2, 3]

# deep copy
x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()
y[0][0] = 9
# print(x, y) # [[9, 2, 3], [4, 5, 6]] [[9, 2, 3], [4, 5, 6]]

import copy
x = [[1, 2, 3], [4, 5, 6]]
y = copy.copy(x) # shallow copy
y[1][1] = 0
# print(x, y) # [[1, 2, 3], [4, 0, 6]] [[1, 2, 3], [4, 0, 6]]

x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x) # deep copy
y[1][1] = 100
# print(x, y) # [[1, 2, 3], [4, 5, 6]] [[1, 2, 3], [4, 100, 6]]

# 列表推導式
# [expression for target in iterble if condition]
oho = [1, 2 ,3 ,4 ,5]
oho = [i * 2 for i in oho]
# print(oho) # [2, 4, 6, 8, 10]

x = [i + 1 for i in range(10)]
# print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [c * 2 for c in 'FishC']
# print(y) # ['FF', 'ii', 'ss', 'hh', 'CC']

code = [ord(c) for c in 'FishC']
# print(code) # [70, 105, 115, 104, 67]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrixLen = len(matrix)
diag = [matrix[i][(matrixLen - 1) - i] for i in range(matrixLen) ]
# print(diag) # [3, 5, 7]

S = [[0] * 3 for i in range(3)]
# print(S) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
S[1][1] = 10
# print(S) # [[0, 0, 0], [0, 10, 0], [0, 0, 0]]

even = [i for i in range(10) if i % 2 == 0] 
# print(even) # [0, 2, 4, 6, 8] 

words = ['Great', 'FishC', 'Brilliant', 'Excellent', 'Fanstistic']
fwords = [w for w in words if w[0] == 'F']
print(fwords) # ['FishC', 'Fanstistic']

bossLevel = [[x, y] for x in range(10) if x % 2 == 0 
                    for y in range(10) if y % 3 == 0]  
# print(bossLevel) 
# [[0, 0], [0, 3], [0, 6], [0, 9], 
# [2, 0], [2, 3], [2, 6], [2, 9], 
# [4, 0], [4, 3], [4, 6], [4, 9], 
# [6, 0], [6, 3], [6, 6], [6, 9], 
# [8, 0], [8, 3], [8, 6], [8, 9]]