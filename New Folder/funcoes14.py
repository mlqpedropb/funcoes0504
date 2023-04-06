#polindromo - palavra ou frase que se pode ler,
# indiferentemente, da esquerda para a 
#direita ou virce-versa
def verificar_palindromo(texto):
    texto = texto.lower().replace('','')
    return texto == texto [::-1]
    
#texto[::-1] inverte o texto
texto = 'sorram-me, subi no onibus em marrocos'
if verificar_palindromo(texto):
    print(texto, 'é poliedro. ')
else:
    print(texto, 'nao é poliedro')