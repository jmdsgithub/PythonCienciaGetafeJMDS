import matplotlib.pyplot as plt



x=['Betis','Atlético de Madrid','Barcelona','Real Madrid']

y=[5,10,15,20]




plt.plot(x,y)

plt.title('Gráfico de lineas')
plt.xlabel('Equipos')
plt.ylabel('Valor de mercado')
plt.savefig('images/lineas.png')
plt.show()