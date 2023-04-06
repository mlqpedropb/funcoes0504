def ano_bi(ano):
    if ano % 4 !=0:
        return False
    elif ano % 100 !=0 :
        return True
    elif ano % 400 !=0:
        return False
    else:
        return False
        
    #ano para comparar
    dados_testes = [100,200,2016,1987,2020]
    #resultado real
    resultados_reais = [False,True,True,False, True]
    #checar funcao
    for i in range(len(dados_testes)):
        yr = dados_testes[1]
        print(yr,'->', end= '')
        result = ano_bi(yr)
        if result == resultados_reais[i]:
            print('ok')
        else:
            print('falha')