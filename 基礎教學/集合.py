# 無序
# 唯一

# 創建集合
# s1 = {"FishC", 'Python'}
# s2 = {s for s in 'FishC'}
# s3 = set('FishC')

# 'C' in s2 #True
# 'c' in s2 #False

# for each in s3:
#     print(each)

# 去重
# l = [1, 1, 2, 3, 5]
# s4 = set(l)
# print(s4) # {1, 2, 3, 5}
# len(l) == len(set(l)) # True代表沒重複, false代表重複

# 方法
# copy
# isdisjoint (???)
# issubset   (子集) 運算符 <
# issuperset (超集) 運算符 >
# union      (連集) 運算符 |
# intersection (交集) 運算符 &
# difference (差集) 運算符 -
# symmetric_difference (對稱差集) 運算符 ^
# update
# intersection_update
# difference_update
# symmetric_difference_update
# add
# remove
# discard
# pop 隨機彈出
# clear

# 不可變對象冰山美人
t = frozenset({'A', 'B', 'C'})

# hash (集合,字典可哈希的, 列表不可)
print(hash(1))
print(hash(1.0))
print(hash(1.001))