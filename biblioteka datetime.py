import datetime
import time

today = datetime.date.today()

print(type(today))
print(today)

data1 = today.strftime('Dzisiaj jest %d dzień ...... %m miesiaca')
data2 = today.strftime('%d-%m-%y')
print(data1)
print(data2)

now = datetime.datetime.now()
print(now)

my_now = now.strftime('%B-%b')
print(my_now)

name = 'raport.txt'
for i in range (10):
    now = datetime.datetime.now()
    my_now = now.strftime('%H%M%S')
    print(name[:6] + my_now + name[-4:])
    time.sleep(2)
