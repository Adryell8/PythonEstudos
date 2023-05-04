import random

ans = random.randrange(1,101)
numtr = 0

tr = int(input('Informe o número para adivinhar entre 1-100: '))
if tr > ans:
    print('O número informado é muito alto.')
elif tr < ans:
    print('O número informado é muito baixo.')
while tr != ans:
    tr = int(input('Informe o número: '))
    numtr += 1
    if tr == ans:
        print('Você acertou! O número era: {} e o número total de tentativas foi: {}'.format(ans, numtr))
        break
    elif tr > ans:
        print('O número informado é muito alto.')
    elif tr < ans:
        print('O número informado é muito baixo.')