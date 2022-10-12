# 分支
# if 100 < 200:
#     print('if')
# elif 200 > 300:
#     print('elif')
# else:
#     print('else')

# 判斷表達式
# a = 3
# b = 5
# small = a if a < b else b
# print(small) # 3

# 循環
# love = 'yes'
# while love == 'yes':
#     love = input('今天妳還愛我嘛?')

# 手動退出循環break(退出最近的一層循環)
# while True:
#     answer = input('主人, 我可以退出循環了嗎?')
#     if(answer == '可以 !'):
#         break
#     print('唉, 好累~~~')

# 執行下一輪循環 continue
# i = 0
# while i < 10:
#     i += 1
#     if(i % 2) == 0:
#         continue
#     print(i)

# for 循環 需搭配好兄弟 range()
for each in "FishC":
    print(each)

for i in range(11):
    print(i) # 0~10

for i in range(5, 10):
    print(i) # 5~9

for i in range(5, 10, 2):
    print(i) # 5 7 9

for i in range(10, 5, -2):
    print(i) # 10 8 6

# if 
# elif
# else
