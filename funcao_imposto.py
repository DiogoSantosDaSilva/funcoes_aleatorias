def custo(imposto, produto):
    custo_final = produto + (produto * imposto / 100)
    return  f'{custo_final:.2f}'


variavel = custo(18, 46)
print(variavel)
