import pandas as pd

print('Primer ejemplo de DataFrame')




datos={
    'nombres':['Lucía','Andrea','Álex','Antonia'],
    'edad':[22,17,48,70],
    'ciudad':['Segovia','Parla','Madrid','Toledo'],
       }

df=pd.DataFrame(datos)
print(df)



print('-------DataFrame filtrado--------')
df_filtrado=df[df['edad']>30]
print(df_filtrado)


print('-------DataFrame ordenado------')
df_sorted=df.sort_values('edad')
print(df_sorted)