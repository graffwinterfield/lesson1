#2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time=int(input())
h=time//3600
m=time%3600//60
s=time%60
print("%02d:%02d:%02d"%(h,m,s))