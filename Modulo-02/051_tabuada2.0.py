tabu = int(input('Gostaria de saber a tabuada de qual valor? '))

while tabu >= 0:
    for i in range(11):
        print(f'{tabu} x {i} = {tabu*i}')
    print('='*50)    
    tabu = int(input('Gostaria de saber a tabuada de qual valor? '))
    print('='*50)

print('\033[31mVocê digitou um numero invalido!\033[m')