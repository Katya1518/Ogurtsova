from random import *
input = open('5-1.txt', 'r')
output = open('5-1-output.txt', 'w')
i = 0
while i <= 1000000:
    i += 1
    a = random()
    c = (((100 *a)*100)//1)/100
    print(c, file=output)
input.close()
output.close()