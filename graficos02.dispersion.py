import matplotlib.pyplot as plt



x=['Betis','Atlético de Madrid','Barcelona','Real Madrid']

y=[5,2,15,20]




plt.scatter(x,y)

plt.title('Gráfico de dispersión')
plt.xlabel('Equipos')
plt.ylabel('Valor de mercado')
plt.savefig('images/dispersion.png')
plt.show()