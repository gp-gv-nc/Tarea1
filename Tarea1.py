#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


#1 leer el archivo csv “tarea” y mostrar las primeras 5 filas (.head()).
df= pd.read_csv('/Users/gonzalorigirozzi/Desktop/UDESA 2do trim/Ameli/tarea.csv')
df.head()


# In[5]:


#2 leer el archivo csv “tarea” y mostrar las primeras 3 filas (,nrows=3).
df1= pd.read_csv('/Users/gonzalorigirozzi/Desktop/UDESA 2do trim/Ameli/tarea.csv')
df1.head(3)


# In[6]:


#3 Imprime el contenido de una columna como serie (tan sólo imprimí la columna entre corchetes!)
df1[['cut']]


# In[16]:


#4 crear una nueva serie 'calidad-color' (utilizá corchetes para definir el nombre de la serie)
df1['calidad-color']=df['clarity']+df['color']
df1


# In[20]:


#5 encontrar el número de filas y columnas (.shape)) y el tipo de datos de cada columna (.dtypes).
print(df1.shape)
print(df1.dtypes)


# In[73]:


#6 resumir sólo las columnas 'objeto' (.describe(include=['object'])).
df1.describe(include=['object'])


# In[27]:


#7 renombrar dos de las columnas (.rename(columns={…). 
#Imprimir antes y después incluyendo una línea que describa cada una (ej print("Original"))
print('Original')
df1


# In[30]:


#7
print('Rename')
df1=df1.rename(columns={'cut':'Cut level', 'price':'Precio'})
df1


# In[34]:


#8 eliminar la segunda y tercer columna (.drop())
df1.drop(columns=['Cut level','color'])


# In[36]:


#9 eliminar múltiples filas a la vez (usar axis=0 que se refiere a las filas).


# In[23]:


#10 ordenar la columna `cut’ en orden ascendente (tarea.cut.sort_values). 
#¿Qué tipo de objeto es `cut’ usándolo así? 
df1.cut.sort_values()


# In[ ]:





# In[25]:


#Es String 
type('cut') 


# In[26]:


#11 ordenar toda la base por 'carat' en orden descendente.
df1.sort_values('carat', ascending=False)


# In[27]:


#12 filtrar aquellas filas que x>5, y>5 y z>5.
df1[(df1['x']>5) & (df['y']>5) & (df1['z']>5)]


# In[28]:


#13 filtrar las filas para que sólo muestren `carat’ mayor a 0,4 (usar for x in tarea.carat:…


# In[9]:


#14 filtrar filas que son Premium o Ideal (tarea.cut.sin() o usar |).


# In[14]:


#15calcular summary statistics de  `carat’ (.describe). 
df1['carat'].describe()


# In[20]:


#16calcular la media de cada columna numérica (.mean())
print(df.mean())


# In[25]:


#17calcular la media del precio de cada tipo de `cut’ (tarea.groupby().price.mean())
df.groupby(['cut']).mean()


# In[86]:


#18 calcular la cantidad, el mínimo y el máximo precio para cada `cut’ ((tarea.groupby().price.agg([]))).

df.groupby(['cut']).price.agg(['min', 'max','sum'])


# In[33]:


#19 mostrar los valores que puede tomar `cut’ (.unique())
df['cut'].unique()


# In[34]:


#20 contar cuántas veces aparece cada valor de `cut’ ((tarea.cut.value_counts()))
df['cut'].value_counts()


# In[88]:


#21 mostrar los porcentajes de cada valor de `cut’.


# In[39]:


#22 calcular una tabla de doble entrada con `cut’ y `color’ (pd.crosstab)


# In[46]:


#23 crear un histograma de ‘cut’ (.plot(kind=’hist’)).
df['cut'].hist()

# In[47]:


#24 crear un gráfico de barras de 'cut'


# In[54]:


#25 contar el número de missing valies en cada columna (.isnull().sum()).
df1.isnull().sum()


# In[55]:


#26 comprobar el número de filas y columnas y eliminarlas si falta algún valor en una fila (.dropna(how='any')).
df1.dropna(how='any')


# In[56]:


#27 eliminar una fila si faltan todos los valores ((.dropna(how='all'))
df1.dropna(how='all')


# In[68]:


#28 mostrar las filas 0, 2, 5 y todas las columnas (.loc[]).
df1.loc[[0,2,5]]


# In[67]:


#29 mostrar las filas 0 a 2 (inclusive) y las columnas 'color' y 'precio' 
df1.loc[0:2, ['color','price']]


# In[66]:


#30 mostrar las filas en las que la 'cut' es 'Premium' más la columna 'color'
df1[(df1['cut'] == 'Premium') & (df1['color'])]


# In[70]:


#31 obtener 5 filas de muestra al azar (.sample()). 
df1.sample(5)


# In[72]:


#32 obtener una muestra del 75% de las filas sin reemplazarlas (.sample(frac=0.75, random_state=XX))
df1.sample(frac=0.75)


# In[ ]:


#33 contar las filas duplicadas.

