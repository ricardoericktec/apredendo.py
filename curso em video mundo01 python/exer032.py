from datetime import date
ano = int(input('digite um ano:  , para o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
    print(f'o ano atual é {ano}')
if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
        print('o ano é bissexto')
else:
    print('o ano não é bissexto')