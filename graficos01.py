import matplotlib.pyplot as plt



x=['Betis','Atlético de Madrid','Barcelona','Real Madrid']

y=[5,10,15,20]




plt.bar(x,y)

plt.title('Gráfico de barras')
plt.xlabel('Equipos')
plt.ylabel('Valor de mercado')
plt.savefig('images/barras.png')
plt.show()
