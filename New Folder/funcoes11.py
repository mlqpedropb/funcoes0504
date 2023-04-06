def fahrenheit_para_celsius(temp_f):
    temp_c = (temp_f - 32)* 5/9
    return temp_c
    
temp_f = 75
temp_c = fahrenheit_para_celsius(temp_f)
print(temp_f, 'graus fahrenheit equivalem a ', temp_c, 'graus Celsius. ')
temp_c_arrendondado = round(temp_c,1)
print(temp_c, ' graus fahrenheit equivalem a ', temp_c_arrendondado,'graus celsius')