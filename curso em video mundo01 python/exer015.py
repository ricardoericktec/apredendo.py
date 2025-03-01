dias = int(input('digite quantos dias voce ficou com o carro:'))
qm = int(input('digite quantos quilometros foram percoridos:'))
print(f"foram percoridos {qm}km por {dias} dias o que dar um total de R${(dias * 60) + (qm * 0.15):.3f} a ser pago")
