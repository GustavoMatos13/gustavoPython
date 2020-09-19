import csv

cnpj = {'28.504.479/0001-12'}
registro = 0
regidtro1 = 0

with open('inf_diario_fi_202006.csv') as f:
    for l in f:
        vals = l.replace('\n', '').split(';')
        if(vals[0] in cnpj):        
            registro = float(vals[3])
            
with open('inf_diario_fi_202005.csv') as f:
    for l in f:
        vals = l.replace('\n', '').split(';')
        if(vals[0] in cnpj):        
            registro1 = float(vals[3])

resultado = ((registro/registro1)-1)*100
print('Cota do dia 30/06: {}'
      '\n Cota do dia 29/05: {}'
      '\n O calculo da rentabilidade absoluta do mês de junho é: {:.2f} '.format(registro,registro1,resultado))
            
        
            
            

    
