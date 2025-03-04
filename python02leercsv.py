import pandas as pd

print('Lectura de CSV')


df=pd.read_csv('data/datos.csv', delimiter=';')
print(df)

print(df.head())
df_sorted=df.sort_values('edad')
print(df_sorted)

media_edad=df['edad'].mean()
print(f'Media de edad: {media_edad}')



df_grupo=df.groupby('ocupacion').size()
print(df_grupo)