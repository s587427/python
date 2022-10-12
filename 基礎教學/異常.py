# try:
#     1 / 0
# except:
#     print('出錯了')

# try:
#    520 + '123'
# except ZeroDivisionError :
#     print('出錯了')


# try:
#    1 / 0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     1 / 0
#     50 + '23123'
# except (ZeroDivisionError, ValueError, TypeError):
#     pass

# try:
#     1 / 0
#     50 +'sasas'
# except ZeroDivisionError:
#     print('除數不能為0')
# except ValueError:
#     print('值不正確')
# except TypeError:
#     print('類型不正確')

# try:
#     1 / 1
# except:
#     print('逮到了')
# else:
#     print('沒逮到~')

# try:
#     1 / 0
# except:
#     print('逮到了')
# else:
#     print('沒逮到~')
# finally:
#     print('逮沒逮到都會吱一聲!')


# 可支持嵌套

# 手動自爆
raise ValueError('陳總在夜總會')
# assert 