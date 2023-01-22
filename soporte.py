import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, datetime
import calendar
import holidays


#Conversion de columna dteday a formato datetime
df['dteday']=df.dteday.apply(pd.to_datetime, format= "%d-%m-%Y")



#Funcion para redefinir las estaciones de acuerdo a fecha
def get_season(fecha):

  '''Función para categorizar las estaciones del año según la fecha
    Parámetros: año, fecha y estaciones
    Return: estación '''
    

  Y= fecha.year
  estaciones = [('invierno', date(Y,  1,  1),  date(Y,  3, 20)),
                ('primavera', date(Y,  3, 21),  date(Y,  6, 20)),
                ('verano', date(Y,  6, 21),  date(Y,  9, 22)),
                ('otoño', date(Y,  9, 23),  date(Y, 12, 20)),
                ('invierno', date(Y, 12, 21),  date(Y, 12, 31))]

  for estacion, inicio, fin in estaciones:
      if inicio <= fecha <= fin:
        return estacion        

# Aplicacion sobre columna 'season'
df['season']= df.date.apply(get_season)


#Festivos USA
us_festivos= holidays.US()

#Funcion para verificar segun fecha si es festivo o laboral
def detectar_feriados(fecha):
    
        '''Función para extraer si es feriado o laboral segun la fecha
          Parámetros: fecha y diccionario de festivos
          Return: si esta en el diccionario return = festivo sino return =laboral '''

        if fecha in us_festivos:
            return 'festivo'
        else:
            return 'laboral'

## Creacion de la columna 'festivo_o_laboral'
df['festivos_o_laboral']=df['date'].apply(detectar_feriados)

