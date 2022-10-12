# 打開(創建)文件
# f = open('FishC.txt', 'r+')
# f.readable()
# f.writable()
# f.write('I love Python.')
# f.writelines(['I love Fish.\n', 'I love my wife.'])

# for each in f:
#     print(each)

# f.close()


# 路徑處理
from pathlib import Path
# 獲取當前目錄路徑
print(Path.cwd())
# 直接給路徑
p = Path('D:\Python\Scripts')
# 判斷路徑是否為文件夾
p.is_dir()
# 判斷路徑是否為文件
p.is_file()
# 檢測路徑存在
p.exists()
# 獲取路徑最後部分
p.name
# 獲取文件名
p.stem
# 獲取文件後墜
p.suffix
# 獲取父層路徑
p.parent
# 獲取列表得父層所有路徑
p.parents
# 拆分路徑變成元祖
p.parts
# 獲取絕對路徑
Path('../abc').resolve()
# 獲取當前路徑下所有文件和子文件夾
p.iterdir()

# 文件操作也可以使用with
with open('./FishC.txt', 'w') as f:
    f.write('I love FishC')






