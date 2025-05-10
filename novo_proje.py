km_inicial = input('Digite o km inicial: ')
km_inicial = int(km_inicial)
km_final = input('Digite o km final: ')
km_final = int(km_final)

km_rodado = km_final - km_inicial
km_rodado = int(km_rodado)

print(f'Você rodou {km_rodado} kms')

combustivel = int(input('Digite o valor gasto com combustivel: '))
gasto_var = int(input('Digite o gasto variado: '))

ganho_bruto = float(input('Insira seu ganho Bruto: ').replace(',', '.'))

ganho_liq = ganho_bruto - combustivel - gasto_var
ganho_liq = float(ganho_liq)

corridas = float(input('Insira a quantidade de corridas: '))
media_cor = ganho_bruto / corridas

print(f'Você ganhor {ganho_liq:,.2f} R$')

media_km = ganho_liq / km_rodado
media_kmbruto = ganho_bruto / km_rodado

print(f'Sua média por km liquido foi de {media_km:,.2f} R$')
print(f'Sua média por km bruto foi de {media_kmbruto:,.2f} R$')
print(f'Sua média por corrida foi de {media_cor:,.2f} R$')


# ellison