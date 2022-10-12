# 十進制模塊
import decimal 

# 浮點數
# python的浮點數不是精確的 
print(0.1 + 0.2 == 0.3) # False

# 借助decimal 模塊達到精確
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)
c = decimal.Decimal('0.3')
print(a + b == c)

print(0.00005) # 5e-05 == 5乘以10的負5次方

# 複數
print(1 + 2j)
x = 1 + 2j
print("實部: ", x.real, ",虛部: ", x.imag)

# 除法
# 有小數點
print(3/2) # 1.5
# 取比目標結果小的最大整數
print(3//2) # 1
print(-3//2) # -2
# 餘數
print(3 % 2) # 1
# divmod => (//結果, 餘數)
print(divmod(3, 2)) #(1, 1)
# abs 絕對值
print(abs(-500)) # 500
# int 轉整數
print(int('520')) # 520
print(int(1.1314520)) # 1
# float 轉浮點數
print(float(3.14)) # 3.14
print(float(520)) # 520.0
print(float('+1E6')) # 1000000.0
# complex 複數
print(complex(1+2j)) # (1+2j)
# pow, ** 次方  pow(2 , 3) == 2 ** 3
print(pow(2, 3)) # 8
print(pow(2, -3)) # 0.125
print(pow(2, 3, 5)) # 3 == 2 ** 3 % 5 , 2的3次方取5餘數
print(2 ** -3) # 0.125