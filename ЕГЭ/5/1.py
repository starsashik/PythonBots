def f(n):
   b = bin(n)[2:]
   ff = b.count('1')
   if ff % 2 == 0:
       b = '10' + b[2:] + '0'
   else:
       b = '11' + b[2:] + '1'
   # b = '1' + str(ff % 2) + b[2:] + str(ff % 2) - то же самое, что с конструкцией if else
   return (int(b, 2))

for i in range(5, 1000):
   if f(i) > 40:
       print(i)
       break