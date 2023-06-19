print('OLA BOM DIA, SOMOS DO DETRAN, IREMOS VERIFICAR O PRECO DA SUA MULTA!!!')
print('Percebemos que voce passou pela BR-105, ONDE O LIMITE MAXIMO DA PISTA E : 100 KM')
km = float(input('Qual foi a velocidade que o Radar capturou? '))
velocidade_amais = km - 100
cor_vermelha = '\033[1;31m'
# cor_vermelha para poder colorir letras em vermelho
def multa():
    print('''Até 20% da velocidade máxima permitida	R$ 130,16	Média
    Até 20% da velocidade máxima permitida	R$ 130,16	GRAVE
    Até 20% da velocidade máxima permitida	R$ 130,16	GRAVISSIMA''')


if km > 100 and km <= 120:
    multa()
    print('Voce atingiu, multa MEDIA = {}R$ 130,16'.format(cor_vermelha))

elif km > 120 and km <= 150:
    multa()
    print('Voce atingiu {}KM, Multa Grave = {}R$ 195,23'.format(velocidade_amais, cor_vermelha))
else:
    multa()
    print('Voce ultrapassou a via a mais de 50% da velocidade maxima da via, MULTA GRAVISSIMA = {}R$ 880,41'.format(cor_vermelha))