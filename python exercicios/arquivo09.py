lag = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = lag * alt
print('Sua parede tem a dimensão de {} por {} e sua área é de {}m².'.format(lag, alt, área))
tinta = área / 2
print('para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))