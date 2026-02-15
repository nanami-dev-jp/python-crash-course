## 10-1

# from pathlib import Path
# path = Path('leaning_python.txt')

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

# from pathlib import Path
# path = Path('leaning_python.txt')
# contents = path.read_text()
# message = contents.replace('Python', 'C')
# print(message)

## 10-3
# for line in path.read_text().splitlines():
#     print(line.replace('Python', 'C'))


## 10-5
# from pathlib import Path
# path = Path('guest_book.txt')


# while True:
#     name = input('Enter your name!')
#     if name == 'quit':
#         break
#     path.write_text(path.read_text() + name + '\n')

#     print(f"Welcome, {name}!")


## 10-6
# try:
#     first_numer = input('Enter the first number: ')
#     second_number = input('Enter the second number: ')

#     result = int(first_numer) + int(second_number)
#     print(f"The sum is {result}")

# except ValueError:
#     print("Please enter valid number.")


## 10-7
# while True:
#     try:
#     first_numer = input('Enter the first number: ')
#     if first_numer == 'q':
#         break

#     second_number = input('Enter the second number: ')
#     if second_number == 'q':
#         break

#     try:
#         result = int(first_numer) + int(second_number)
#         print(f"The sum is {result}.")
        
#     except ValueError:
#         print("Please enter valid number.")


# ## 10-8
# from pathlib import Path
# files = ['cats.txt', 'dogs.txt']

# for filename in files:
#     path = Path(filename)

#     try:
#         contents = path.read_text()
#         print(f"\Contents of {filename}:")
#         print(contents)

#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")


## 10-9　省略

## 10-10 省略

## 10-14
import json

filename = 'username.json'

def get_stored_username():
    """保存されているユーザー名を取得する。"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """新しいユーザー名を取得して保存する"""
    username = input("What is your name?")

    with open(filename, 'w') as f:
        json.dump(username, f)

    return username

def greet_user():
    """ユーザーに挨拶する(確認つき)"""
    username = get_stored_username()

    if username:
        correct = input(f"Are you {username}? (y/n)")

        if correct.lower() == 'y':
            print('Welcome back, {username}!')
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")
    
greet_user()