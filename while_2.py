from ast import Num


total = 0
while input('Add Number[y] =>'):
    num = int(input('Enter a number'))
    total += num

print(f' total => {total}')