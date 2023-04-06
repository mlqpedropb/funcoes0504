def funcoes_detecta(n):
    if(n % 2 ==0):
        return 'é par'
    else:
        return 'é impar'
        
print(funcoes_detecta(int(input('entre com numero: '))))