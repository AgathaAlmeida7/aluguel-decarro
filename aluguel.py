

quant_km=float(input('digite quantos km o carro rodou:\n'))

quant_dias=int(input('quantos dias voce rodou com esse carro?:\n'))


preço_a_pagar_p_dia=quant_dias*60

preço_a_pagar_por_km=quant_km*0.15

preço_a_pagar_final=preço_a_pagar_p_dia+preço_a_pagar_por_km


print('a quantidade que voce ira pagar pelos dias que voce andou sera de:R${}'.format(preço_a_pagar_p_dia))

print('a quantidade que voce ira pagar pelos km que voce andou sera de:R${}'.format(preço_a_pagar_por_km))


print('juntanto tudo isso ai,o valor final percorrido pelo carro alugado,considerando tanto os dias andados e os km percorrido,sera de : R${}'.format(preço_a_pagar_final))