# def 方法名():
#     ...something

# pass 佔位符甚麼事都不做
# 沒有return 會有一個None
def myfunc(name, times):
    for i in range(times):
        print(f'{name}在夜總會')


def div(x ,y):
    if y == 0:
        return '除數不能為0'
    else:
        return x // y

# print(myfunc('陳總', 5))
# print(div(4, 2))
# print(div(4, 0))
# 關鍵字參數可以不用照順序來 func(a='apple', b='banner') 
# 位置參數必須需在關鍵字參數之前
# 默認參數 def func(s, vt, o='小甲魚'):   呼叫方法不傳入o會使用默認參數
# 可以回傳多個值
# *收集參數, 也可用來解包
# **關鍵字參數
# 支持嵌套函數
# nolocal 嵌套函數改變上一層變數
# LEGB規則 Local > Enclosed > Global Build-In
# 支持閉包
# 參數可以傳入func
# 裝飾器
# 支持高階函數
 

# 斜線左邊只能使用位置參數
def func(a, /, b, c):
    print(a, b, c)

# *左邊能使用關鍵也可位置參數，但是右側b和c必須是關鍵字參數
def func2(a, *, b, c):
    print(a, b, c)

#收集參數 
def func3(*args):  
    print(args) # 是元組
    print('有{}個參數'.format(len(args)))
    print('第2個參數是: {}'.format(args[1]))
# func3('陳總', '在夜總會')

def func4():
    return 1, 2, 3
# 解包
# args = (1, 2, 3, 4)  somefunc(*args) 類似js somefunc(...args)
# args = {'a': 1, 'b': 2}  somefunc(**args)
# f = func4() # (1, 2, 3)
# x, y ,z = func4() # x = 1, y = 2, z = 3

#一定要傳關鍵參數
def func5(**kwars):
    print(kwars)
# func5(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3}


# 裝飾器
from re import I
import time
# def time_master(func):
#     def call_func():
#         print('開始運行程式...')
#         start = time.time()
#         func()
#         stop = time.time()
#         print('結束程式運行...')
#         print(f'一共耗費了 {(stop-start):.2f} 秒')
#     return call_func

# # 在定義的方法上加上另一個方法名, 執行此定義方法即可執行另一個方法自動帶入定義的方法作為參數傳進去
# @time_master
# def func6():
#     time.sleep(2)
#     print('I love FishC')
# func6()

# lambda表達式
# squareY = lambda y : y * y
# print(squareY(3)) # 9
# mapped = map(lambda x : ord(x) + 10, 'FishC')
# print(list(mapped)) # [80, 115, 125, 114, 77] 
# print(list(filter(lambda x : x % 2, range(10)))) # [1, 3, 5, 7, 9] 

# 生成器
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
# print(counter) # <function counter at 0x000001E65159F1C0>

# for i in counter():
#     print(i)

c = counter()
next(c) # 1
next(c) # 2
next(c) # 3
next(c) # 4
next(c) # 5

# 生成器表達式 (i ** 2 for i in range(10))

# 類型註釋
def items(s:str, n:int) -> str:
    return s * n

# 內省
# fnc.__name__ get函數名
# fnc.__annotations__ get類型註解
# fuc.__doc__ get函數文檔