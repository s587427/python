# True | False

# bool 轉換布林值
print(bool(250)) # True
print(bool('假')) # True
print(bool('False')) # True
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(0j)) # False
print(bool('')) # False

# 定義為False的對象: None 和 False, 值為0的數字類型, 空的序列和集合: (), [], {}, set(), range(0)

# 邏輯運算符號
# and eg. 3 < 4 and 4 < 5
# or eg. 3 < 4 or 4 < 5
# not ex not True, not False

# 短路邏輯
print(3 and 4) # 4
print(4 or 5) # 4
print('FishC' or 'Love') # FishC
print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)) # 4