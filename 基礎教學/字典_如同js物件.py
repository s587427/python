y = {'呂布': '口口布', '關羽': '關羽羽'} 
print(type(y)) # <class 'dict'>

# 讀取
y['呂布'] 
# 新增
y['劉備'] = '劉baby'
print(y) # {'呂布': '口口布', '關羽': '關羽羽', '劉備': '劉baby'}

# 創建字典方式
# a = {'呂布': '口口布', '關羽': '關羽羽', '劉備': '劉baby'}
# b = dict(呂布='口口布', 關羽='關羽羽', 劉備='劉baby')
# c = dict([('呂布', '口口布'), ('關羽', '關羽羽'), ('劉備', '劉baby')])
# d = dict({'呂布': '口口布', '關羽': '關羽羽', '劉備': '劉baby'})
# e = dict({'呂布': '口口布', '關羽': '關羽羽'}, 劉備='劉baby')
# f = dict(zip(['呂布', '關羽', '劉備'], ['口口布', '關羽羽', '劉baby']))
# print(a == b == c == d == e == f) # True

# 新增
# d = dict.fromkeys("Fish", 250)
# print(d) # {'F': 250, 'i': 250, 's': 250, 'h': 250}

# 刪除
# 鍵不存在會報錯KeyError: '狗'
# d.pop('狗') 
# d.pop('F') 
# print(d) # {'i': 250, 's': 250, 'h': 250}
# d.popitem()
# print(d) # {'i': 250, 's': 250}
# del d['s']
# print(d) # {'i': 250}
# d = dict.fromkeys("Fish", 250)
# d.clear()
# print(d) # {}

# 更新
d = dict.fromkeys('FishC', 250)
# d.update({'i': 105, 'h': 104}) 
# d.update(F='70', C='67')
# print(d) # {'F': '70', 'i': 105, 's': 250, 'h': 104, 'C': '67'}

# # 查 
# r = d.get('c', '這裡沒有c')
# print(r) # 這裡沒有c
# d.setdefault('C', 'code')
# d.setdefault('c', 'code')
# print(d) # {'F': '70', 'i': 105, 's': 250, 'h': 104, 'C': '67', 'c': 'code'}

# 字典的視圖對象
# keys = d.keys()
# values = d.values()
# items = d.items()
# print(keys, values, items)

# e = d.copy()
# len(d) # 5
# 'C' in d # True
# list(d) # ['F', 'i', 's', 'h', 'C']
# list(d.values)
# e = iter(d)
# list(reversed(d.values()))

# 深度字典
# d = {
#     '呂布': {
#         '語文': 60,
#         '數學': 100
#     },
#     '關羽':{
#         '語文': 50,
#         '數學': 77
#     }
# }
# d['呂布']['數學'] # 100
# d['關羽']['語文'] # 50

# 字典推導式
# d = {'F': 70, 'i': 105, 's': 115, 'h':104, 'C': 67}
# b = {v:k for k, v in d.items()}
# print(b) # {70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}
# c = {v:k for k, v in d.items() if v > 100}
# print(c) # {105: 'i', 115: 's', 104: 'h'}