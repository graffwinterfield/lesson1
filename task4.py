#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

num=[a.split() for a in input()]
maxx=0
k=0
while k!=len(num):
    if int(num[k][0]) > maxx:
        maxx=int(num[k][0])
    k+=1
print(maxx)