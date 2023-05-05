import math
num = int(input('Informe um número para descobrir a raiz: '))
raiz = math.sqrt(num)
print('A raiz quadra de {} é: {}'.format(num, math.ceil(raiz)))