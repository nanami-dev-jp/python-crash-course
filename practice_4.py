## 4-3

# for value in range(1, 21):
#     print(value)


## 4-4

##以下間違い
# list = []
# for value in range(1, 1000000):
#     list = value

# print(list)

##正しくは以下
# numbers = list(range(1, 1_000_001))

# for number in numbers:
#     print(numbers)


## 4-5

# numbers = list(range(1, 1_000_001))
# #以下は変数はさまなくてもそのまま print(min(numbers))にしても良い
# number_min = min(numbers)
# print(number_min)

# number_max = max(numbers)
# print(number_max)

# number_sum = sum(numbers)
# print(number_sum)


## 4-6
# odd_numbers = list(range(1, 21, 2))

# for number in odd_numbers:
#     print(number)


## 4-7

# threes = list(range(3, 31, 3))

# for number in threes:
#     print(number)


## 4-8 ★自力で解けた！！
# list = []
# for number in range(1, 11):
#     list = number ** 3
#     print(list)


## 4-9
cubes = [number ** 3 for number in range(1, 11)]
for cube in cubes:
    print(cube)