from pathlib import Path

path = Path('Pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()

# 以下は上と同じ結果になる
# contents = path.read_text().rstrip()
# print(contents)

contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


