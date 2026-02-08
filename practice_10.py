## 10-1

from pathlib import Path
path = Path('leaning_python.txt')

# 1回目：ファイル全体を一度に読む
# print('1回目：ファイル全体を一度に読む')
# contents = path.read_text()
# print(contents)

# 2回目：forループで1行ずつ読む
# print('2回目：forループで1行ずつ読む')
# for line in contents.splitlines():
#     print(line)

# 3回目：リストに格納してから表示
# print('3回目：リストに格納してから表示')
# lines = contents.splitlines()

# for line in lines:
#     print(line)

## 10-2

from pathlib import Path
path = Path('leaning_python.txt')
# contents = path.read_text()
# message = contents.replace('Python', 'C')
# print(message)

## 10-3
for line in path.read_text().splitlines():
    print(line.replace('Python', 'C'))
