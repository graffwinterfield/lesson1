#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

izd=int(input('izderjka '))
viru=int(input('viruchka '))
if izd>viru:
    print('убыток')
elif izd<viru:
    prib=viru-izd
    print('pribil ', prib)
    ren=prib/viru
    print('rentbl ',ren)
    personal=int(input('personal: '))
    print(prib//personal)
    print('прибыль')