def pagamento(horas, taxa):
    extra = horas - 40
    if extra > 0:
        preco_final = (40*taxa) + (extra * taxa * 1.5) 
        return f'{preco_final:.2f}'
    else:
        return f'{horas * taxa:.2f}'
    

variavel = pagamento(80, 10)
print(variavel)
