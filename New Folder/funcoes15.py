def romano_para_DECIMAL(num_romano):
    valores = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm': 10000}
    decimal = 0
    for i in range(len(num_romano)):
        if i > 0 and valores[num_romano[i]]> valores[num_romano[i-1]]:
            decimal += valores[num_romano[i]]-2* valores[num_romano[i-1]]
        else:
            decimal += valores [num_romano[i]]
    return decimal
    
num_romano= 'mcmxciv'
decimal = romano_para_DECIMAL(num_romano)
print(num_romano, 'em decimal é', decimal)