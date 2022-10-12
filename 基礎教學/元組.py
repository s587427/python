# ()元組括號可選, []列表

# 元組不可修改
rhyme = 1, 2, 3, 4, 5, '上山打老虎'
# print(rhyme)
# rhyme[0] # 1
# rhyme[1] # 2
# rhyme[0] = -1 # TypeError: 'tuple' object does not support item assignment

nums = (3, 1, 9, 6, 8, 3, 5, 3)
# print(nums.count(3)) # 3
# print(nums.index(9)) # 2

s = (1, 2, 3)
t = (4, 5, 6)
# print(s + t) # (1, 2, 3, 4, 5, 6)
# print(s * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
w = s, t
# print(w) # ((1, 2, 3), (4, 5, 6))

# for each in s:
#     print(each)

y = [i * 2 for i in s]
# print(y) # [2, 4, 6]

# 生成一個元組必須在後面加逗號
z = (520,)

# 打包 
t = (123, 'FishC', 3.14)
# 解包 (列表元組字串都可以)
x, y, z = t # 左右兩邊數量必須一致
# print(x ,y ,z) # 123 FishC 3.14

a, b, c, d, e = 'FishC'
# print(a, b, c, d, e ) # F i s h C

a, b, *c = 'FishC'
print(a, b, c) # F i ['s', 'h', 'C']  

# 如果元組的元素是一個列表那還是可以被修改的須注意一下